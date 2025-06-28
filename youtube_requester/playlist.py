import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#entry -> str
#output -> str list
#retrieves a list of URLs of all the videos in a playlist from its URL
def getAllVideoURLFromPlaylist(url) :
  if not (checkArgumentsTypeStrGetter(url)) : raise Exception("Unexpected exception from type of arguments")

  parsed_url = getPlaylistURLFromVideo(url)
  if not (parsed_url['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
  url = parsed_url['url']

  chromedriver_autoinstaller.install()
  soup = getPlaylistPagesHTML(url)
  if not (checkPlaylistAccess(soup)) : raise Exception("Unexpected exception on checking playlist access")
  if not (checkPlaylistIsNotEmpty(soup)) : raise Exception("Unexpected exception on checking playlist size")
  
  return getPlaylistVideosURL(soup)
#entry -> str et int
#output -> str
#retrieves video URL from playlist url and index
def getVideoURLFromPlaylist(url, index) :
  if ((not (checkArgumentsTypeStrGetter(url))) or (not checkArgumentsTypeIntGetter(index))) : raise Exception("Unexpected exception from type of arguments")
  
  parsed_url = getPlaylistURLFromVideo(url)
  if not (parsed_url['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
  url = parsed_url['url']

  chromedriver_autoinstaller.install()
  soup = getPlaylistPagesHTML(url)
  if not (checkPlaylistAccess(soup)) : raise Exception("Unexpected exception on checking playlist access")
  if not (checkPlaylistIsNotEmpty(soup)) : raise Exception("Unexpected exception on checking playlist size")
  
  return getPlaylistVideoURLIndex(soup, index)

#function to scrap youtube
def getPlaylistPagesHTML(url) :
  options = Options()
  options.add_argument("--headless")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  driver = webdriver.Chrome(options)

  driver.get(url)

  button = driver.find_element("xpath", '//button[@aria-label="Tout accepter"]')
  button.click()

  wait = WebDriverWait(driver, 10)
  result_element = wait.until(EC.presence_of_element_located((By.ID, "content")))

  result = result_element.get_attribute("innerHTML")

  driver.quit()

  return BeautifulSoup(result, "html.parser")
#function to process html and get a list of URLs
def getPlaylistVideosURL(soup) :
  content_div = soup.find("div", id="contents")
  videoslinks = content_div.find_all("a", id="thumbnail", href=True)
  links = []
  for link in videoslinks:
    parsed_link = parsingVideoURL(link)
    if not (parsed_link['noError']) : raise Exception("Unexpected exception on parsing video URL")
    links.append(parsed_link['url'])
  return links
#function to process html and get URL of video with the specified index
def getPlaylistVideoURLIndex(soup, index) :
  content_div = soup.find("div", id="contents")
  videoslinks = content_div.find_all("a", id="thumbnail", href=True)
  for link in videoslinks:
    parsed_link = parsingVideoURLIndex(link)
    if not (parsed_link['noError']) : raise Exception("Unexpected exception on parsing video URL")
    if f"&index={index}" in str(parsed_link).lower() :
      return parsed_link['url'].split("&")[0]
  raise Exception("No video with this ID in the playlist")
      
#Check the argument type STR
def checkArgumentsTypeStrGetter(url) :
  if(type(url) == str) :
    return True
  elif(type(url) != str):
    raise TypeError("Only string are allowed for URL")
  else:
    raise Exception("Unexpected exception from type of arguments")
#Check the argument type INT
def checkArgumentsTypeIntGetter(index) :
  if(type(index) == int) :
    return True
  elif(type(index) != int):
    raise TypeError("Only string are allowed for Index")
  else:
    raise Exception("Unexpected exception from type of arguments")
#check that the playlist is accessible
def checkPlaylistAccess(soup) :
  alert_div = soup.find("div", id="alerts")
  tag_children = [child for child in alert_div.children if child.name is not None]
  if(len(tag_children) == 0) :
    return True
  elif(len(tag_children) == 1) :
    if "la playlist n'existe pas." in str(tag_children[0]).lower():
      raise Exception("The playlist is in private mode or not accessible")
    else :
      return True
  else :
    raise Exception("Unexpected exception on checking playlist access")
#check that the playlist is not empty
def checkPlaylistIsNotEmpty(soup) :
  content_div = soup.find("div", id="contents")
  thumbnail_div = content_div.find("div", id="thumbnail")
  if(thumbnail_div != None) :
    tag_children = [child for child in thumbnail_div.children if child.name is not None]
    if(len(tag_children) >=1 ) :
      return True
    elif(len(tag_children) == 0) :
      raise Exception("The playlist is Empty")
    else :
      raise Exception("Unexpected exception on checking playlist size")
  else : 
    return True
#allows you to parse the link (url of the video) with a str to get the URL of the video only
def parsingVideoURL(link) :
  result = {'noError': True, 'url': ''}
  try :
    result['url'] = "https://www.youtube.com" + link["href"].split("&")[0]
    return result 
  except :
    result['noError'] = False
    raise Exception("Unexpected exception on parsing video URL")
    return result 
  finally :
    return result
#allows you to parse the link (url of the video) with a str to get the URL of the video only with index
def parsingVideoURLIndex(link) :
  result = {'noError': True, 'url': ''}
  try :
    result['url'] = "https://www.youtube.com" + link["href"].split("&")[0] + "&index=" + link["href"].split("&index=")[1].split("&")[0]
    return result 
  except :
    result['noError'] = False
    raise Exception("Unexpected exception on parsing video URL")
    return result 
  finally :
    return result