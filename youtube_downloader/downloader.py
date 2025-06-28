from youtube_downloader import canehill

def downloadVideo(url, folder):
  return(canehill.download(url, folder))

def downloadVideos(urls, folder):
  tempResult = []
  for url in urls :
    elementTempResult = canehill.download(url, folder)
    print(elementTempResult)
    tempResult.append(elementTempResult)
  return(tempResult)