from youtube_requester import playlist, video
from youtube_downloader import canehill

import os

url = "https://www.youtube.com/watch?v=yoD7p3qZ3T0&pp=ygUaYm9uYm9uIGEgbGEgbWVudGhlIGpvaydhaXI%3D"
download_dir = os.path.join(os.getcwd(), "downloads")

#############YT################
# print(playlist.getAllVideoURLFromPlaylist(url))
# print(playlist.getVideoURLFromPlaylist(url, 3))

# parsed_url = video.getPlaylistURLFromVideo(url)
# if not (parsed_url['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
# print(parsed_url['url'])
# parsed_url = video.getVideoURLFromVideoinPlaylist(url)
# if not (parsed_url['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
# print(parsed_url['url'])

###############downloader###############
print(canehill.download(url, download_dir))