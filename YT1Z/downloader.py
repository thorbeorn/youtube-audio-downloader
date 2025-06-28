from youtube_requester import video

import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download(url) :
  if not (checkArgumentsTypeStrGetter(url)) : raise Exception("Unexpected exception from type of arguments")

  parsed_url_video = video.getVideoURLFromVideoinPlaylist(url)
  if not (parsed_url_video['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
  video_UUID = parsed_url_video['url'].split("watch?v=")[1]
  url = "https://yt1z.net/en/video/" + video_UUID

  chromedriver_autoinstaller.install()

  options = Options()
  # options.add_argument("--headless")
  # options.add_argument("--no-sandbox")
  # options.add_argument("--disable-dev-shm-usage")
  driver = webdriver.Chrome(options)

  driver.get(url)

  wait = WebDriverWait(driver, 10)
  first_step_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Download MP3"]')))
  button = driver.find_element("xpath", '//button[@aria-label="Download MP3"]')
  button.click()

  mp3_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.cursor-pointer")))

  result = first_step_element.get_attribute("innerHTML")

  driver.quit()

  soup =  BeautifulSoup(result, "html.parser")

#Check the argument type STR
def checkArgumentsTypeStrGetter(url) :
  if(type(url) == str) :
    return True
  elif(type(url) != str):
    raise TypeError("Only string are allowed for URL")
  else:
    raise Exception("Unexpected exception from type of arguments")