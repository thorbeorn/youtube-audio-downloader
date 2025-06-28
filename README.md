# YouTube MP3 Downloader

This project allows you to automatically download MP3 audio files from YouTube videos or playlists using a headless Chrome browser and an external conversion service.  

It is built using Python and Selenium for browser automation.

---

## 🚀 Features

- Extracts video URLs from playlists
- Converts and downloads YouTube videos as MP3
- Automatically handles browser interaction and pop-ups
- Saves downloads to a specified folder
- Renames downloaded files to clean titles

## 🛠️ Requirements

- Python 3.7+
- Google Chrome installed
- ChromeDriver compatible with your Chrome version

## ⚠️ Disclaimer
This project is for educational purposes only.
Downloading copyrighted content from YouTube may violate its Terms of Service.

Always ensure you have permission to download and use the content.

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/thorbeorn/youtube-audio-downloader.git
cd youtube-audio-downloader
```

## 🧪 Usage
### Install dependencies:
```bash
pip install -r requirements.txt
```

Edit the main.py file with your target YouTube URL and Folder (default: Create Download folder in current path):
```python
from youtube_requester import playlist, video
from youtube_downloader import canehill
import os

url = "https://www.youtube.com"
download_dir = os.path.join(os.getcwd(), "downloads")

#For One Video
print(canehill.download(url, download_dir))
#For all playlist video
print(downloader.downloadVideos(playlist.getAllVideoURLFromPlaylist(url), download_dir))
```
Then run:
```bash
python main.py
```
The MP3 file will be saved in the downloads/ directory.

## 🎯 Using Only Playlist and Video URL Extraction Functions
If you want to use only the utility functions to extract URLs from playlists or videos without downloading.

### Install dependencies:
```bash
pip install -r requirements.txt
```
And you can call them directly:

```python
from youtube_requester import playlist, video

url = "https://www.youtube.com/watch?v=yoD7p3qZ3T0"

# Get all video URLs from a playlist
print(playlist.getAllVideoURLFromPlaylist(url))

# Get a specific video URL from a playlist by index
print(playlist.getVideoURLFromPlaylist(url, 3))

# Get the playlist URL from a video URL
parsed_url = video.getPlaylistURLFromVideo(url)
if not parsed_url['noError']:
    raise Exception("Unexpected exception on parsing playlist URL")
print(parsed_url['url'])

# Get the video URL inside a playlist URL
parsed_url = video.getVideoURLFromVideoinPlaylist(url)
if not parsed_url['noError']:
    raise Exception("Unexpected exception on parsing playlist URL")
print(parsed_url['url'])