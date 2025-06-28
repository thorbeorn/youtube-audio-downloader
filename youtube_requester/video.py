#entry -> str
#output -> str
#recovers the URL of a playlist from a video
def getPlaylistURLFromVideo(url) :
  if not (checkArgumentsTypeStrGetter(url)) : raise Exception("Unexpected exception from type of arguments")

  result = {'noError': True, 'url': ''}
  if (len(url.split("youtube.com/playlist")) == 2) :
    result['url'] = url.split("&")[0]
    return result 
  if (len(url.split("&list=")) == 2) :
    parsed_url = parsingPlaylistURL(url)
    if not (parsed_url['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
    result['url'] = parsed_url['url']
    return result 
  elif (len(url.split("&list=")) == 1) :
    result['noError'] = False
    raise Exception("Video URL doesn't contain list")
    return result 
  else :
    result['noError'] = False
    raise Exception("Unexpected exception on parsing playlist URL")
    return result 
#entry -> str
#output -> str
#recovers the URL of a video from a video in a list
def getVideoURLFromVideoinPlaylist(url) :
  if not (checkArgumentsTypeStrGetter(url)) : raise Exception("Unexpected exception from type of arguments")

  result = {'noError': True, 'url': ''}
  if (len(url.split("youtube.com/watch")) == 2) :
    result['url'] = url.split("&")[0]
    return result 
  else :
    result['noError'] = False
    raise Exception("Unexpected exception on parsing video URL")
    return result 

#Check the argument type STR
def checkArgumentsTypeStrGetter(url) :
  if(type(url) == str) :
    return True
  elif(type(url) != str):
    raise TypeError("Only string are allowed for URL")
  else:
    raise Exception("Unexpected exception from type of arguments")
#allows you to parse the link (playlist url) with a str to get the playlist URL
def parsingPlaylistURL(link) :
  result = {'noError': True, 'url': ''}
  try :
    result['url'] = "https://www.youtube.com/playlist?list=" + link.split("&list=")[1].split("&")[0]
  except :
    result['noError'] = False
    raise Exception("Unexpected exception on parsing playlist URL")
  finally :
    return result 