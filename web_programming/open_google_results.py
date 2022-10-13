import webbrowser
from sys import argv
from urllib.parse import quote, parse_qs
from fake_useragent import UserAgent

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    if len(argv) > 1:
        query = "%20".join(argv[1:])
    else:
        query = quote(str(input("Search: ")))

    print("Googling.....")

    url = f"https://www.google.com/search?q={query}&num=100"

    res = requests.get(
        url,
        headers={
            "User-Agent": str(UserAgent().random)
        },
    )

    try:
        link = (
            BeautifulSoup(res.text, "html.parser")
            .find("div", attrs={"class": "yuRUbf"})
            .find("a")
            .get("href")
        )

    except AttributeError:
        link = parse_qs(
            BeautifulSoup(res.text, "html.parser")
            .find("div", attrs={"class": "kCrYT"})
            .find("a")
            .get("href")
        )["url"][0]

    webbrowser.open(link)
