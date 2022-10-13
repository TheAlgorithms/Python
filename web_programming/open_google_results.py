import webbrowser
from sys import argv
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    if len(argv) > 1:
        query = "%20".join(argv[1:])
    else:
        query = quote(str(input("Search: ")))

    print("Googling.....")

    url = f"https://www.google.com/search?q={query}&num=2"

    res = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) " "Gecko/20100101 Firefox/98.0"
        },
    )

    link = (
        BeautifulSoup(res.text, "html.parser")
        .find("div", attrs={"class": "yuRUbf"})
        .find("a")
        .get("href")
    )

    webbrowser.open(link)
