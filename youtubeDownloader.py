from pytube import YouTube
import os

url = input("url:")
yt = YouTube(url)
yt.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution').desc().first().download('download')
