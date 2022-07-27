import youtube_dl
from typing import List

class SoundCloud:
    def __init__(self, url: str) -> None:
        self.url = url
        self.info = self.extract_info()

    def ydl_option(self) -> None:
        return {"dumpjson": True, "extract_flat": True}

    def extract_info(self) -> dict:
        with youtube_dl.YoutubeDL(self.ydl_option()) as ydl:
            return ydl.extract_info(url=self.url, download=False)
    
    @property
    def genre(self) -> str:
        return self.info["genre"]

    @property
    def formats(self) -> List:
        return self.info["formats"]

    @property
    def caption(self) -> str:
        return self.info["description"]

    @property
    def thumbnails(self) -> List:
        return self.info["thumbnails"]

    @property
    def view_count(self) -> int:
        return self.info["view_count"]

    @property
    def comment_count(self) -> int:
        return self.info["comment_count"]

    @property
    def repost_count(self) -> int:
        return self.info["repost_count"]

    @property
    def like_count(self) -> int:
        return self.info["like_count"]

    @property
    def idd(self) -> str:
        return self.info["id"]

    @property
    def uploader(self) -> str:
        return self.info["uploader"]

    @property
    def uploader_id(self) -> str:
        return self.info["uploader_id"]

    @property
    def uploader_url(self) -> str:
        return self.info["uploader_url"]

    @property
    def upload_date(self) -> int:
        return self.info["timestamp"]

    @property
    def title(self) -> str:
        return self.info["title"]
