from youtube_requester import playlist, video
from YT1Z import downloader

url = "https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=PLvlFnRiNEsRzdyUIy9DftHDfheWGRMkHL"

#############YT################
# print(playlist.getAllVideoURLFromPlaylist(url))
# print(playlist.getVideoURLFromPlaylist(url, 3))

# parsed_url = video.getPlaylistURLFromVideo(url)
# if not (parsed_url['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
# print(parsed_url['url'])
# parsed_url = video.getVideoURLFromVideoinPlaylist(url)
# if not (parsed_url['noError']) : raise Exception("Unexpected exception on parsing playlist URL")
# print(parsed_url['url'])

###############yt1z###############
downloader.download(url)