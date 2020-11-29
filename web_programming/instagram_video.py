from datetime import datetime

import requests


def download_video(url: str) -> bytes:
    url = f"https://downloadgram.net/wp-json/wppress/video-downloader/video?url={url}"
    json_data = requests.get(url).json()
    video_data = requests.get(json_data[0]["urls"][0]["src"]).content
    return video_data

if __name__ == "__main__":
    link = input("Enter Video/IGTV url: ").strip()
    print(f"Downloading video from {link} ...")
    file_name = f"{datetime.now():%Y-%m-%d_%H:%M:%S}.mp4"
    with open(file_name, "wb") as fp:
        fp.write(download_video(link))
    print(f"Done. Video saved to disk as {file_name}.")
