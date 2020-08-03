#!/usr/bin/env python3

'''
This programs gives the latest statistics related to the situaion of Covid 19 all around the world.
The data is being scrapped from 'https://www.worldometers.info/coronavirus/'.
'''

import requests
from bs4 import BeautifulSoup


def world_covid19_stats(url: str="https://www.worldometers.info/coronavirus/") -> dict:
    """
    Return a dict of world covid19 stats
    """
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    keys = soup.findAll('h1')
    values = soup.findAll("div", {"class": "maincounter-number"})
    keys += soup.findAll("span", {"class": "panel-title"})
    values += soup.findAll("div", {"class": "number-table-main"})
    return {key.text.strip(): value.text.strip() for key, value in zip(keys, values)}


if __name__ == "__main__":
    print("\033[1m" + "COVID-19 Status of the World" + "\033[0m\n")
    for key, value in world_covid19_stats().items():
        print(f"{key}\n{value}\n")
