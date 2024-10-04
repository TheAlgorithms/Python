"""
Bu, worldometers sitesinden basit COVID19 bilgilerini lxml kullanarak almayı gösterir.
* bs4 yerine lxml kullanmanın ana motivasyonu, daha hızlı olması ve bu nedenle
Python web projelerinde (örneğin, Django veya Flask tabanlı) kullanmanın daha uygun olmasıdır.
"""

from typing import NamedTuple
import requests
from lxml import html


class CovidData(NamedTuple):
    vakalar: int
    ölümler: int
    iyileşenler: int


def covid_istatistikleri(url: str = "https://www.worldometers.info/coronavirus/") -> CovidData:
    xpath_str = '//div[@class = "maincounter-number"]/span/text()'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        veri = html.fromstring(response.content).xpath(xpath_str)
        return CovidData(*map(int, veri))
    except requests.RequestException as e:
        print(f"Veri alınırken hata oluştu: {e}")
        return CovidData(0, 0, 0)


fmt = """Dünyadaki toplam COVID-19 vakaları: {}
COVID-19 nedeniyle dünyadaki toplam ölümler: {}
Dünyadaki toplam iyileşen COVID-19 hastaları: {}"""
print(fmt.format(*covid_istatistikleri()))

