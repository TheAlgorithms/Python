from datetime import UTC, datetime

import requests
from bs4 import BeautifulSoup


def download_video(url: str) -> bytes:
    """
    Verilen bir Instagram video URL'sinden video indirir.

    Parametreler:
        url: İndirilecek video URL'si.

    Dönüş:
        Video içeriği byte olarak.
    """
    base_url = "https://downloadgram.net/wp-json/wppress/video-downloader/video?url="
    try:
        response = requests.get(base_url + url, timeout=10)
        response.raise_for_status()
        video_url = response.json()[0]["urls"][0]["src"]
        video_response = requests.get(video_url, timeout=10)
        video_response.raise_for_status()
        return video_response.content
    except requests.exceptions.RequestException as e:
        return f"Video indirme hatası: {e}".encode()


if __name__ == "__main__":
    url = input("Video/IGTV URL'sini girin: ").strip()
    file_name = f"{datetime.now(tz=UTC).astimezone():%Y-%m-%d_%H:%M:%S}.mp4"
    with open(file_name, "wb") as fp:
        video_content = download_video(url)
        if isinstance(video_content, bytes):
            fp.write(video_content)
            print(f"Tamamlandı. Video {file_name} olarak diske kaydedildi.")
        else:
            print(video_content.decode())
