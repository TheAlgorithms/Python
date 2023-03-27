import os
from pathlib import Path

from pytube import YouTube


def download(requestedLink):
    link = requestedLink
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    filename = stream.title
    downloads_path = str(Path.home() / "Downloads")
    stream.download(output_path=downloads_path)
