#!/usr/bin/env python3

"""
Created by sarathkaul on 14/11/19

Depending on your settings, you may need a two-factor authentication OTP code.
Documentation_url: https://developer.github.com/v3/auth#working-with-two-factor-authentication
"""


import requests

_GITHUB_API = "https://api.github.com/user"


def fetch_github_info(auth_user: str, auth_pass: str) -> dict:
    """
    Fetch GitHub info using the requests module
    """
    return requests.get(_GITHUB_API, auth=(auth_user, auth_pass)).json()


if __name__ == "__main__":
    for key, value in fetch_github_info("<USER NAME>", "<PASSWORD>").items():
        print(f"{key}: {value}")
