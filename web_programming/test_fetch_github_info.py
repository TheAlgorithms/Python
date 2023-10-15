import json

import requests

from .fetch_github_info import AUTHENTICATED_USER_ENDPOINT, fetch_github_info


# Define a test case to fetch and validate GitHub user information.
def test_fetch_github_info(monkeypatch):
    class FakeResponse:
        def __init__(self, content) -> None:
            assert isinstance(content, (bytes, str))
            self.content = content

        def json(self):
            return json.loads(self.content)

    # Mock the response from a GitHub API request with a fake response.
    def mock_response(*args, **kwargs):
        assert args[0] == AUTHENTICATED_USER_ENDPOINT
        assert "Authorization" in kwargs["headers"]
        assert kwargs["headers"]["Authorization"].startswith("token ")
        assert "Accept" in kwargs["headers"]
        return FakeResponse(b'{"login":"test","id":1}')

    monkeypatch.setattr(requests, "get", mock_response)

    # Call the function to fetch GitHub information with a mock response.
    result = fetch_github_info("token")

    # Assert that the fetched data matches the expected values.
    assert result["login"] == "test"
    assert result["id"] == 1
