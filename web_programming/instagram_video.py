import json
from datetime import datetime

import requests


def get_video(link) -> None:
    url = f"https://downloadgram.net/wp-json/wppress/video-downloader/video?url={link}"
    req = requests.get(url)
    res = req.content
    json_data = json.loads(res)
    information = [
        json_data[0]["urls"][0]["quality"],
        json_data[0]["urls"][0]["ext"],
        json_data[0]["urls"][0]["size"],
        json_data[0]["urls"][0]["src"],
    ]
    print(
        f"""
                This Is Information About Video
        
        Quality : {information[0]}
        Format  : {information[1]}
        Size    : {information[2]} 
        SRC     : {information[3]}
    """
    )
    print(f"Downloading video from {link} ...")
    video_data = requests.get(information[3]).content
    file_name = f"{datetime.now():%Y-%m-%d_%H:%M:%S}.mp4"
    with open(file_name, "wb") as fp:
        fp.write(video_data)
    print(f"Done. Video saved to disk as {file_name}.")


if __name__ == "__main__":
    url = input("Enter Video/IGTV url: ").strip()
    get_video(link=url)
