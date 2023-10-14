import json

import requests

from .fetch_github_info import AUTHENTICATED_USER_ENDPOINT, fetch_github_info


# Test function with mock response to test 'fetch_github_info'.
def test_fetch_github_info(monkeypatch):
    # Define a fake response class for testing purposes.
    class FakeResponse:
        def __init__(self, content) -> None:
            assert isinstance(content, (bytes, str))
            self.content = content

        def json(self):
            return json.loads(self.content)

    # Define a mock response function for 'requests.get'.
    def mock_response(*args, **kwargs):
        assert args[0] == AUTHENTICATED_USER_ENDPOINT
        assert "Authorization" in kwargs["headers"]
        assert kwargs["headers"]["Authorization"].startswith("token ")
        assert "Accept" in kwargs["headers"]
        return FakeResponse(b'{"login":"test","id":1}')

    # Use 'monkeypatch' to replace 'requests.get' with the mock response.
    monkeypatch.setattr(requests, "get", mock_response)

    # Call 'fetch_github_info' with a token and assert results.
    result = fetch_github_info("token")
    assert result["login"] == "test"
    assert result["id"] == 1
