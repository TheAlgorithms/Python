"""
Fetch all the top headlines from Hindustan Times News website with
title, link to the news article and cover image link.

The following format is used while displaying the data

news = {
        0: {
            "title": <title-of-the-article>,
            "link": <link-to-the-news-article>,
            "img": <link-to-the-cover-image>
        }
}
"""

import requests
from bs4 import BeautifulSoup


def fetch_ht_news() -> dict:
    header = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/127.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
    }

    url = "https://www.hindustantimes.com/"
    page_request = requests.get(url, headers=header, timeout=10)
    data = page_request.content
    soup = BeautifulSoup(data, "html.parser")

    news = {}

    counter = 0

    for divtag in soup.find_all("div", {"class": "timeAgo"}):
        if "liveStory" not in divtag["class"]:
            head = divtag.find(class_="hdg3")
            title = head.get_text()
            link = divtag["data-weburl"]
            imgtag = divtag.find("img")
            try:
                img = imgtag["data-src"]
            except KeyError:
                img = imgtag["src"]
            news[counter] = {"title": title, "link": link, "img": img}
            counter += 1

    return news


if __name__ == "__main__":
    fetch_ht_news()
