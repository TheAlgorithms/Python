#!/usr/bin/env python3

"""
Dünya genelindeki güncel COVID-19 istatistiklerini sağlayın.
Bu veriler 'https://www.worldometers.info/coronavirus/' adresinden alınmaktadır.
"""

import requests
from bs4 import BeautifulSoup


def world_covid19_stats(url: str = "https://www.worldometers.info/coronavirus") -> dict:
    """
    Güncel dünya genelindeki COVID-19 istatistiklerini içeren bir sözlük döndürür
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # HTTP hatalarını kontrol et
    soup = BeautifulSoup(response.text, "html.parser")
    keys = soup.findAll("h1")
    values = soup.findAll("div", {"class": "maincounter-number"})
    keys += soup.findAll("span", {"class": "panel-title"})
    values += soup.findAll("div", {"class": "number-table-main"})
    return {key.text.strip(): value.text.strip() for key, value in zip(keys, values)}


if __name__ == "__main__":
    print("\033[1m Dünya COVID-19 Durumu \033[0m\n")
    print("\n".join(f"{key}\n{value}" for key, value in world_covid19_stats().items()))
