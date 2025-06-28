from youtube_requester import playlist, video
from youtube_downloader import downloader

import os

url = "https://www.youtube.com/watch?v=w8-izVQgNRk&list=PLvlFnRiNEsRzkWVIhUPDBvbpD2mBRrj8n"
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
# print(downloader.downloadVideo(url, download_dir))
# print(downloader.downloadVideos(playlist.getAllVideoURLFromPlaylist(url), download_dir))