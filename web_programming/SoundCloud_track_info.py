import youtube_dl


class SoundCloud:
    def __init__(self, url: str):
        self.url = url
        self.info = self.extract_info()

    def ydl_option(self):
        return {
            "dumpjson": True,
            "extract_flat": True
        }

    def extract_info(self):
        try:
            with youtube_dl.YoutubeDL(self.ydl_option()) as ydl:
                return ydl.extract_info(url=self.url, download=False)
        except Exception as e:
            return e

    @property
    def genre(self):
        return self.info['genre']
    
    @property
    def formats(self):
        return self.info['formats']

    @property
    def caption(self):
        return self.info['description']
    
    @property
    def thumbnails(self):
        return self.info['thumbnails']

    @property
    def view_count(self):
        return self.info['view_count']
    
    @property
    def comment_count(self):
        return self.info['comment_count']
    
    @property
    def repost_count(self):
        return self.info['repost_count']
    @property
    def like_count(self):
        return self.info['like_count']

    @property
    def idd(self)
        return self.info['id']

    @property
    def uploader(self):
        return self.info['uploader']

    @property
    def uploader_id(self):
        return self.info['uploader_id']
    
    @property
    def uploader_url(self):
        return self.info['uploader_url']

    @property
    def upload_date(self):
        return self.info['timestamp']
    
    @property
    def title(self):
        return self.info['title']

