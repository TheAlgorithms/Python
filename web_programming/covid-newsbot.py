import requests
from bs4 import BeautifulSoup
import re

class Scraper:
    def __init__(self, keywords):
        self.markup = requests.get('https://economictimes.indiatimes.com/news/coronavirus').text
        self.keywords = keywords

    def parse(self):
        soup = BeautifulSoup(self.markup, 'html.parser')
        links = soup.findAll('a', limit=300)
        #regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        self.saved_links = []
        self.saved_linksTexts = []
        for link in links:
            for keyword in self.keywords:
                if keyword in link.text and '?' not in link.text:
                    self.saved_links.append(link)
        for link in self.saved_links:
            self.saved_linksTexts.append(link.text)


s = Scraper([
    'Coronavirus',
    'pandemic',
    'COVID-19',
    'infection',
    'Wuhan'
    ])

s.parse()
#for x in s.saved_links:
#    print(x.text)
