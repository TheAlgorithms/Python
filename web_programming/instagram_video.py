# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

from datetime import UTC, datetime

import httpx


def download_video(url: str) -> bytes:
    base_url = "https://downloadgram.net/wp-json/wppress/video-downloader/video?url="
    video_url = httpx.get(base_url + url, timeout=10)
    return httpx.get(video_url, timeout=10).content


if __name__ == "__main__":
    url = input("Enter Video/IGTV url: ").strip()
    file_name = f"{datetime.now(tz=UTC).astimezone():%Y-%m-%d_%H-%M-%S}.mp4"
    with open(file_name, "wb") as fp:
        fp.write(download_video(url))
    print(f"Done. Video saved to disk as {file_name}.")
