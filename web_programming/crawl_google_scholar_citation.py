"""
Get the citation from google scholar
using title and year of publication, and volume and pages of journal.
"""

import re

import requests
from bs4 import BeautifulSoup


def create_url(title: str, journal: str, volume: str, page: str, year: str) -> str:
    """
    Return the url.
    """
    url = (
        f"http://scholar.google.com/scholar_lookup?hl=en&"
        f"title={title}"
        f"&journal={journal}"
        f"&volume={volume}"
        f"&pages={page}"
        f"&publication_year={year}"
    )
    url = remove_tag(url)
    return url.replace(" ", "%")


def remove_tag(url: str) -> str:
    """
    Remove the html tags in 'url'.
    Return the url removed the html tags.
    """
    tag = re.compile("<.*?>")
    clean_url = re.sub(tag, "", url)
    return clean_url


def get_citation(url: str) -> str:
    """
    Return the citation number.
    """
    url = requests.get(url).text
    soup = BeautifulSoup(url, "html.parser")
    get_div = soup.find("div", attrs={"class": "gs_ri"})
    get_a_tag = get_div.find("div", attrs={"class": "gs_fl"}).findAll("a")
    citation = get_a_tag[2].get_text()
    if "Cited" not in citation:
        citation = "Cited by 0"

    return citation.replace("Cited by ", "")


if __name__ == "__main__":
    """
    You have to fill following values: title, journal_name, volume, page, year.
    For example,
    title = "abc de"
    journal_name = "fgh"
    volume = "30"
    page = "3979-3990"
    year = "2020"
    """
    title = ""
    journal_name = ""
    volume = ""
    page = ""
    year = ""

    citation = get_citation(create_url(title, journal_name, volume, page, year))
    print(citation)
