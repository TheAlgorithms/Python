# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx2",
# ]
# ///

from datetime import UTC, datetime

import httpx2


def download_video(url: str) -> bytes:
    base_url = "https://downloadgram.net/wp-json/wppress/video-downloader/video?url="
    video_url = httpx2.get(base_url + url, timeout=10)
    return httpx2.get(video_url, timeout=10).content


if __name__ == "__main__":
    url = input("Enter Video/IGTV url: ").strip()
    file_name = f"{datetime.now(tz=UTC).astimezone():%Y-%m-%d_%H-%M-%S}.mp4"
    with open(file_name, "wb") as fp:
        fp.write(download_video(url))
    print(f"Done. Video saved to disk as {file_name}.")
