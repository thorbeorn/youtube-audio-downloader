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

download_dir = os.path.join(os.getcwd(), "downloads")

def download(url) :
  if not (checkArgumentsTypeStrGetter(url)) : raise Exception("Unexpected exception from type of arguments")

  parsed_url_video = video.getVideoURLFromVideoinPlaylist(url)
  if not (parsed_url_video['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
  video_UUID = parsed_url_video['url'].split("watch?v=")[1]
  url = "https://ytdl.canehill.info/v/" + video_UUID

  if not os.path.exists(download_dir):
    os.makedirs(download_dir)

  options = Options()
  options.add_argument("--headless")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
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

  fichier = wait_for_download_complete(download_dir)
  return("Fichier téléchargé :", fichier)

#Wait and check the donwload file
def wait_for_download_complete(folder, timeout=60):
    seconds = 0
    while seconds < timeout:
        files = os.listdir(folder)
        downloading = [f for f in files if f.endswith('.crdownload')]
        finished = [f for f in files if f.endswith('.mp3')]

        if not downloading and finished:
            return os.path.join(folder, finished[0])

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