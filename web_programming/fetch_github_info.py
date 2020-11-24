#!/usr/bin/env python3
"""
Updated by lawric1 on 24/11/20

Authentication will be made via access token.
To generate your personal access token visit https://github.com/settings/tokens.
"""

import requests

_GITHUB_API = "https://api.github.com/user"
USER_TOKEN = "" # provide your access token

def fetch_github_info(auth_token: str) -> dict:
    """
    Fetch GitHub info of a user using the requests module
    """
    token = {"Authorization": "token {}".format(auth_token)}
    return requests.get(_GITHUB_API, headers=token).json()


if __name__ == "__main__":
    if USER_TOKEN:
        for key, value in fetch_github_info(USER_TOKEN).items():
            print(f"{key}: {value}")
    else:
        print("token should not be empty")