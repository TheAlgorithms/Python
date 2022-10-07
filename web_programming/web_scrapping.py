import csv
import re

import requests
from bs4 import BeautifulSoup


def get_soup(url: str) -> BeautifulSoup:
    return bs4.BeautifulSoup(requests.get(url).text, "html.parser")


def get_webpage_metadata(url: str) -> dict:
    soup = get_soup(url)
    webpage_metadata = {
        "language": soup.html.get("lang") or "Not mentioned",
        "charset": soup.meta.get("charset") or "Not mentioned",
    }

    try:
        if title := soup.find("meta", property="og:title")["content"]:
            webpage_metadata["title"] = title
    except KeyError:
        try:
            if title := soup.find("meta", attrs={"name": "title"})["content"]:
                webpage_metadata["title"] = title
        except KeyError:
            webpage_metadata["title"] = "Not mentioned"

    try:
        if type_ := soup.find("meta", property="og:type")["content"]:
            webpage_metadata["type"] = type_
    except KeyError:
        try:
            if type_ := soup.find("meta", attrs={"name": "type"})["content"]:
                webpage_metadata["type"] = type_
        except KeyError:
            webpage_metadata["type"] = "Not mentioned"

    try:
        if description := soup.find("meta", property="og:description")["content"]:
            webpage_metadata["description"] = description
    except KeyError:
        try:
            if description := soup.find("meta", attrs={"name": "description"})[
                "content"
            ]:
                webpage_metadata["description"] = description
        except KeyError:
            webpage_metadata["description"] = "Not mentioned"

    try:
        if site_name := soup.find("meta", property="og:site_name")["content"]:
            webpage_metadata["site_name"] = site_name
    except KeyError:
        try:
            if site_name := soup.find("meta", attrs={"name": "site_name"})["content"]:
                webpage_metadata["site_name"] = site_name
        except KeyError:
            webpage_metadata["site_name"] = "Not mentioned"

    try:
        if image := soup.find("meta", property="og:image")["content"]:
            webpage_metadata["image"] = image
    except KeyError:
        try:
            if image := soup.find("meta", attrs={"name": "image"})["content"]:
                webpage_metadata["image"] = image
        except KeyError:
            webpage_metadata["image"] = "Not mentioned"

    try:
        if keywords := soup.find("meta", property="og:keywords")["content"]:
            webpage_metadata["keywords"] = keywords
    except KeyError:
        try:
            if keywords := soup.find("meta", attrs={"name": "keywords"})["content"]:
                webpage_metadata["keywords"] = keywords
        except KeyError:
            webpage_metadata["keywords"] = "Not mentioned"
    if webpage_metadata["title"] == "Not mentioned":
        webpage_metadata["title"] = soup.find("title").text
    return webpage_metadata


def process_tags(soup: bs4.BeautifulSoup) -> list:
    all_tags = []
    allhrefs = set()
    for a in soup.find_all("a", href=True):
        if a["href"].find("https://") == -1:
            allhrefs.add(request_url + a["href"])
        else:
            allhrefs.add(a["href"])
    hrefs = list(allhrefs)

    hrefs.insert(0, "links")
    all_tags.append(hrefs)
    all_images = {image["src"] for image in soup.find_all("img", src=True)}
    images = list(all_images)
    images.insert(0, "images")
    all_tags.append(images)

    all_h2 = set()
    for h2 in soup.find_all("h2"):
        all_h2.add(h2.text.strip())
    h2 = list(all_h2)
    h2.insert(0, "h2")
    all_tags.append(h2)

    return all_tags


def write_in_csv(webpage_metadata: dict, all_tags: list) -> None:
    with open("webpage_info.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(webpage_metadata)
        writer.writerows(all_tags)


def write_webpage_metadata_to_csv(webpage_metadata: dict) -> None:
    meta_list = []
    for key, value in webpage_metadata.items():
        l = []
        l.insert(0, key)
        l.append(value)
        meta_list.append(l)

    all_tags = process_tags

    write_in_csv(meta_list, all_tags)


if __name__ == "__main__":
    write_webpage_metadata_to_csv(get_webpage_metadata("https://techcrunch.com/"))
