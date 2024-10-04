import json

import requests

from .fetch_github_info import AUTHENTICATED_USER_ENDPOINT, fetch_github_info


def test_fetch_github_info(monkeypatch):
    class SahteYanıt:
        def __init__(self, içerik) -> None:
            assert isinstance(içerik, (bytes, str))
            self.içerik = içerik

        def json(self):
            return json.loads(self.içerik)

    def sahte_yanıt(*args, **kwargs):
        assert args[0] == AUTHENTICATED_USER_ENDPOINT
        assert "Authorization" in kwargs["headers"]
        assert kwargs["headers"]["Authorization"].startswith("token ")
        assert "Accept" in kwargs["headers"]
        return SahteYanıt(b'{"login":"test","id":1}')

    monkeypatch.setattr(requests, "get", sahte_yanıt)
    sonuç = fetch_github_info("token")
    assert sonuç["login"] == "test"
    assert sonuç["id"] == 1
