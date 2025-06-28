from youtube_requester import video

import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Parameters:
# ----------
# url : str
#     The URL of a YouTube video or a playlist containing the desired video.

# folder : str
#     The path to the folder where the downloaded file should be saved. 
#     The folder will be created if it does not already exist.

# Returns:
# -------
# str
#     A message indicating that the file was successfully downloaded, including its final path.
# Downloads an MP3 audio file from a YouTube video URL using an external converter service.
# This function automates a headless Chrome browser using Selenium to interact with the online converter 
# (ytdl.canehill.info). It navigates to the conversion page, clicks the MP3 download button, handles pop-up 
# windows, waits for the download to complete, and renames the downloaded file to remove unnecessary text.
def download(url, folder) :
  if not (checkArgumentsTypeStrGetter(url)) : raise Exception("Unexpected exception from type of arguments")

  parsed_url_video = video.getVideoURLFromVideoinPlaylist(url)
  if not (parsed_url_video['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
  video_UUID = parsed_url_video['url'].split("watch?v=")[1]
  url = "https://ytdl.canehill.info/v/" + video_UUID

  if not os.path.exists(folder):
    os.makedirs(folder)

  options = Options()
  options.add_argument("--headless")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  options.add_experimental_option("prefs", {
    "download.default_directory": folder,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
  })
  driver = webdriver.Chrome(options)

  driver.get(url)
  wait = WebDriverWait(driver, 10)
  mp3_button_waiter = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.cursor-pointer")))
  main_window = driver.current_window_handle
  mp3_button = driver.find_element(By.CSS_SELECTOR, ".border-separate > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4) > button:nth-child(1)")
  mp3_button.click()

  time.sleep(1)
  for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        driver.close()
        driver.switch_to.window(main_window) 

  fichier = wait_for_download_complete(folder)
  driver.quit()
  
  filename = os.path.basename(fichier)
  if "ytdl.canehill.info - " in filename and " (320 KBps)" in filename:
      try:
          cleaned = filename.replace("ytdl.canehill.info - ", "").replace(" (320 KBps)", "")
          cleaned_path = os.path.join(folder, cleaned)
          os.rename(fichier, cleaned_path)
          fichier = cleaned_path
      except Exception as e:
          raise(f"Erreur lors du renommage : {e}")

  return {
    "message": "Fichier téléchargé",
    "chemin": fichier
  }

#Wait and check the donwload file
def wait_for_download_complete(folder, timeout=60):
    # Liste des fichiers .mp3 AVANT le téléchargement
    before = set(f for f in os.listdir(folder) if f.endswith('.mp3'))

    seconds = 0
    while seconds < timeout:
        files = os.listdir(folder)
        downloading = [f for f in files if f.endswith('.crdownload')]
        finished = [f for f in files if f.endswith('.mp3')]

        if not downloading:
            # Liste des fichiers .mp3 APRÈS
            after = set(finished)
            new_files = after - before
            if new_files:
                # Retourner le chemin du nouveau fichier
                new_file = new_files.pop()
                return os.path.join(folder, new_file)

        time.sleep(1)
        seconds += 1

    raise TimeoutError("Le téléchargement n'a pas été terminé dans le délai imparti.")
#Check the argument type STR
def checkArgumentsTypeStrGetter(url) :
  if(type(url) == str) :
    return True
  elif(type(url) != str):
    raise TypeError("Only string are allowed for URL")
  else:
    raise Exception("Unexpected exception from type of arguments")