#!/usr/bin/env python3

"""
Created by sarathkaul on 14/11/19

Basic authentication using an API password is deprecated and will soon no longer work.
Visit https://developer.github.com/changes/2020-02-14-deprecating-password-auth
for more information around suggested workarounds and removal dates.
"""

"""
Created by lawric1 on 24/11/20

To generate your personal access token visit https://github.com/settings/tokens
"""

import requests

_GITHUB_API = "https://api.github.com/user"


def fetch_github_info(auth_user: str, auth_token: str) -> dict:
    """
    Fetch GitHub info of a user using the requests module
    """
    return requests.get(_GITHUB_API, auth=(auth_user, auth_token)).json()


if __name__ == "__main__":
    for key, value in fetch_github_info("<USER NAME>", "<TOKEN>").items():
        print(f"{key}: {value}")
