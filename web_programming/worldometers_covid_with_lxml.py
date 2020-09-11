import requests
from lxml import html

try:
    wld = requests.get("https://www.worldometers.info/coronavirus/")
    wldh = html.fromstring(wld.content)
    wldc = wldh.xpath('//div[@class = "maincounter-number"]/span/text()')
    wcase = wldc[0]
    wdeath = wldc[1]
    wcure = wldc[2]
except:
    wcase = 'fetching.....'
    wdeath ='fetching.....'
    wcure = 'fetching.....'

print('Total COVID19 Cases in the world :' + wcase)
print('Total Deaths Due to COVID19 in the world :' + wdeath)
print('Total COVID19 Patients Cured in the world :' + wcure)