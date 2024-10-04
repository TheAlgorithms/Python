import webbrowser
from sys import argv
from urllib.parse import parse_qs, quote

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def google_search(query: str) -> str:
    """
    Verilen sorguyu Google'da arar ve ilk sonucun bağlantısını döndürür.
    """
    url = f"https://www.google.com/search?q={quote(query)}&num=100"
    res = requests.get(
        url,
        headers={"User-Agent": str(UserAgent().random)},
        timeout=10,
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
    return link

if __name__ == "__main__":
    query = " ".join(argv[1:]) if len(argv) > 1 else input("Arama: ").strip()
    print("Googling.....")
    link = google_search(query)
    webbrowser.open(link)
