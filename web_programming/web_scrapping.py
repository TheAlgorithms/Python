import csv
import re

import bs4
import requests


def scrap_info(request_url: str) -> dict:
    res = requests.get(request_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")

    webpage_metadata = {}
    language = str(soup.html.get("lang"))
    print("Language is ",language)
    if language == "None":
        webpage_metadata["language"] = "Not mentioned"
    else:
        webpage_metadata["language"] = language
    charset = str(soup.meta.get("charset"))
    if charset == "None":
        webpage_metadata["charset"] = "Not mentioned"
    else:
        webpage_metadata["charset"] = charset

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
            if description := soup.find("meta", attrs={"name": "description"})["content"]:
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
    meta_list = []
    for key, value in webpage_metadata.items():
        l = []
        l.insert(0, key)
        l.append(value)
        meta_list.append(l)

    all_tags = process_tags
    
    write_in_csv(meta_list, all_tags)
    return webpage_metadata

def process_tags() -> list:
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

if __name__ == '__main__':
    scrap_info("https://techcrunch.com/")
