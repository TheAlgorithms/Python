"""
This is to show simple COVID19 info fetching from worldometers site using lxml
* The main motivation to use lxml in place of bs4 is that it is faster & therefore more
convenient to use in Python web projects (e.g. Django based)
"""

import requests
from lxml import html


wld = requests.get("https://www.worldometers.info/coronavirus/")
wldh = html.fromstring(wld.content)
wldc = wldh.xpath('//div[@class = "maincounter-number"]/span/text()')
wcase = wldc[0]
wdeath = wldc[1]
wcure = wldc[2]

print('Total COVID19 Cases in the world :' + wcase)
print('Total Deaths Due to COVID19 in the world :' + wdeath)
print('Total COVID19 Patients Cured in the world :' + wcure)