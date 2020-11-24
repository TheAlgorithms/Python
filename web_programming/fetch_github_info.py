#!/usr/bin/env python3
"""
Created by sarathkaul on 14/11/19

Basic authentication using an API password is deprecated and will soon no longer work.
Visit https://developer.github.com/changes/2020-02-14-deprecating-password-auth
for more information around suggested workarounds and removal dates.


Updated by lawric1 on 24/11/20

Authentication will be made via access token.
To generate your personal access token visit https://github.com/settings/tokens.
"""

import requests

_GITHUB_API = "https://api.github.com/user"


def fetch_github_info(auth_token: str) -> dict:
    """
    Fetch GitHub info of a user using the requests module
    """
    token = {'Authorization': 'token {}'.format(auth_token)}
    return requests.get(_GITHUB_API, headers=token).json()


if __name__ == "__main__":
    for key, value in fetch_github_info("<TOKEN>").items():
        print(f"{key}: {value}")
