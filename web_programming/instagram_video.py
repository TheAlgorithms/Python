import json
from datetime import datetime

import requests

if __name__ == "__main__":
    link = input("Enter Video/IGTV url: ").strip()
    url = f"https://downloadgram.net/wp-json/wppress/video-downloader/video?url={link}"
    req = requests.get(url)
    res = req.content
    json_data = json.loads(res)
    print(f"Downloading video from {link} ...")
    video_data = requests.get(json_data[0]["urls"][0]["src"]).content
    file_name = f"{datetime.now():%Y-%m-%d_%H:%M:%S}.mp4"
    with open(file_name, "wb") as fp:
        fp.write(video_data)
    print(f"Done. Video saved to disk as {file_name}.")
