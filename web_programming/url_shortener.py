#!/usr/bin/env python

"""
URL Shortener - Shorten the long URLs using bit.ly API

Example:
>>> long = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
>>> short = shorten(long)
>>> print(short)
Short URL - https://bit.ly/3m65DwS

"""
# Importing the modules
import json
import random

import requests

# List of APIs
apis = [
    "aa23aee0d3fb2ca94502977922cc85c118f12232",
    "f8b29c335baa35f36df23068ff4299bf88da1a1b",
    "cd6177d489e82e7cc0593ae655bc3fe4654bcbf6",
]

# You can use your own bit.ly API in place of `token`
token = random.choice(apis)


def shorten(site: str) -> str:
    headers = {"Authorization": f"Bearer {token}"}
    data = json.dumps({"long_url": site})

    res = requests.post(
        "https://api-ssl.bitly.com/v4/shorten", headers=headers, data=data
    )

    out = json.loads(res.text)
    try:
        return out["link"]
    except KeyError:
        return -1  # Something went wrong


if __name__ == "__main__":
    long_site = input("Enter the long URL (included https://) ->")

    short_url = shorten(long_site)
    print("Shorten URL is", short_url)
