# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "fake-useragent",
#     "httpx",
# ]
# ///

import webbrowser
from sys import argv
from urllib.parse import parse_qs, quote

import httpx
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

if __name__ == "__main__":
    query = "%20".join(argv[1:]) if len(argv) > 1 else quote(str(input("Search: ")))

    print("Googling.....")

    url = f"https://www.google.com/search?q={query}&num=100"

    res = httpx.get(
        url,
        headers={"User-Agent": str(UserAgent().random)},
        timeout=10,
    )

    try:
        link = BeautifulSoup(res.text, "html.parser").find("div").find("a").get("href")

    except AttributeError:
        link = parse_qs(
            BeautifulSoup(res.text, "html.parser").find("div").find("a").get("href")
        )["url"][0]

    webbrowser.open(link)
