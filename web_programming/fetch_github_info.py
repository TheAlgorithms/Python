#!/usr/bin/env python3
"""
Created by sarathkaul on 14/11/19
Updated by lawric1 on 24/11/20

Authentication will be made via access token.
To generate your personal access token visit https://github.com/settings/tokens.

NOTE:
Never hardcode any credential information in the code. Always use an environment
file to store the private information and use the `os` module to get the information
during runtime.

Create a ".env" file in the root directory and write these two lines in that file
with your token::

#!/usr/bin/env bash
export USER_TOKEN=""
"""

from __future__ import annotations

import os
from typing import Any

import requests

BASE_URL = "https://api.github.com"

# https://docs.github.com/en/free-pro-team@latest/rest/reference/users#get-the-authenticated-user
AUTHENTICATED_USER_ENDPOINT = BASE_URL + "/user"

# https://github.com/settings/tokens
USER_TOKEN = os.environ.get("USER_TOKEN", "")


def fetch_github_info(auth_token: str) -> dict[Any, Any]:
    """
    Fetch GitHub info of a user using the requests module
    Input: auth_token - github user token
    Takes the headers provided and makes a GET request to github's user details API.
    The Authorization header is required for any request that
    accesses specific user information, in any API.
    Some are prefixed with bearer instead of token.
    The Accept header is a github only parameter,
    with application/vnd.github+json recommended.
    The request is then made with these headers at the API endpoint,
    and returns a response.
    Responses aren't human readable immediately,
    so the json() function outputs easy to read json.
    For more information on how the requests library is used,
    read up on https://requests.readthedocs.io/en/latest/.
    Output: json data about user from API request, in the form of a Python dictionary
    """
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    return requests.get(AUTHENTICATED_USER_ENDPOINT, headers=headers, timeout=10).json()


if __name__ == "__main__":  # pragma: no cover
    if USER_TOKEN:
        for key, value in fetch_github_info(USER_TOKEN).items():
            print(f"{key}: {value}")
    else:
        raise ValueError("'USER_TOKEN' field cannot be empty.")
