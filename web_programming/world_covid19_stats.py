#!/usr/bin/env python3

"""
Provide the current worldwide COVID-19 statistics.
This data is being scrapped from 'https://www.worldometers.info/coronavirus/'.
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

import httpx
from bs4 import BeautifulSoup


def world_covid19_stats(
    url: str = "https://www.worldometers.info/coronavirus/",
) -> dict:
    """
    Return a dict of current worldwide COVID-19 statistics
    """
    soup = BeautifulSoup(
        httpx.get(url, timeout=10, follow_redirects=True).text, "html.parser"
    )
    keys = soup.find_all("h1")
    values = soup.find_all("div", {"class": "maincounter-number"})
    keys += soup.find_all("span", {"class": "panel-title"})
    values += soup.find_all("div", {"class": "number-table-main"})
    return {key.text.strip(): value.text.strip() for key, value in zip(keys, values)}


if __name__ == "__main__":
    print("\033[1m COVID-19 Status of the World \033[0m\n")
    print("\n".join(f"{key}\n{value}" for key, value in world_covid19_stats().items()))
