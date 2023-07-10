import moviepy.editor
from tkinter.filedialog import *
import os
import youtube_dl
import re

def is_video(file_path):
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.flv']
    file_extension = os.path.splitext(file_path)[1].lower()
    return file_extension in video_extensions

def audio_generate(video_file):
    if is_video(video_file):
        video = moviepy.editor.VideoFileClip(video_file)
        audio = video.audio
        audio.write_audiofile("sample.mp3")
    else:
        print("Given file is not a video")

def download_audio(video_link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'sample.mp3',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])


def is_url(text):
    url_pattern = re.compile(
        r"^(http|https|ftp)://([A-Za-z0-9-]+\.)+[A-Za-z]{2,4}(/[A-Za-z0-9-]+)*(\?[A-Za-z0-9-]+=[A-Za-z0-9-]+(&[A-Za-z0-9-]+=[A-Za-z0-9-]+)*)?$"
    )
    return bool(url_pattern.match(text))

video = "https://www.youtube.com/watch?v=LosIGgon_KM"

if is_url(video):
    download_audio(video)

else:
    audio_generate(video)
