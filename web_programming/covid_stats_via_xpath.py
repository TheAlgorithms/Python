"""
This is to show simple COVID19 info fetching from worldometers site using lxml
* The main motivation to use lxml in place of bs4 is that it is faster and therefore
more convenient to use in Python web projects (e.g. Django or Flask-based)
"""

from collections import namedtuple

import requests
from lxml import html  # type: ignore

covid_data = namedtuple("covid_data", "cases deaths recovered")


def covid_stats(url: str = "https://www.worldometers.info/coronavirus/") -> covid_data:
    xpath_str = '//div[@class = "maincounter-number"]/span/text()'
    return covid_data(*html.fromstring(requests.get(url).content).xpath(xpath_str))


fmt = """Total COVID-19 cases in the world: {}
Total deaths due to COVID-19 in the world: {}
Total COVID-19 patients recovered in the world: {}"""
print(fmt.format(*covid_stats()))
