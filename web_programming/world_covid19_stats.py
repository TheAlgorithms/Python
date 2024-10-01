#!/usr/bin/env python3

"""
Provide the current worldwide COVID-19 statistics.
This data is being scrapped from 'https://www.worldometers.info/coronavirus/'.
"""

import requests
from bs4 import BeautifulSoup


def world_covid19_stats(url: str = "https://www.worldometers.info/coronavirus") -> dict:
    """
    Return a dict of current worldwide COVID-19 statistics.

    The function scrapes data from the Worldometer website and returns the
    global COVID-19 statistics.

    Args:
        url (str): The URL to fetch the COVID-19 data from.
    
    Returns:
        dict: A dictionary of worldwide COVID-19 statistics where the keys are
        the names of the statistics (e.g., 'Total Cases') and the values are the
        corresponding numbers (e.g., '233,456,789').

    Example:
        >>> stats = world_covid19_stats()
        >>> isinstance(stats, dict)
        True
        >>> 'Total Cases' in stats.keys()
        True
        >>> 'Total Deaths' in stats.keys()
        True
        >>> len(stats) > 0
        True
    
    Raises:
        requests.RequestException: If there is an issue with the network request.
    """
    soup = BeautifulSoup(requests.get(url, timeout=10).text, "html.parser")
    keys = soup.findAll("h1")
    values = soup.findAll("div", {"class": "maincounter-number"})
    keys += soup.findAll("span", {"class": "panel-title"})
    values += soup.findAll("div", {"class": "number-table-main"})
    return {key.text.strip(): value.text.strip() for key, value in zip(keys, values)}


if __name__ == "__main__":
    print("\033[1m COVID-19 Status of the World \033[0m\n")
    print("\n".join(f"{key}\n{value}" for key, value in world_covid19_stats().items()))
