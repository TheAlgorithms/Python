import bs4
import requests
from bs4 import BeautifulSoup


def parsePrice():
    page = requests.get('https://in.finance.yahoo.com/quote/%5EIXIC?p=^IXIC')
    soup = bs4.BeautifulSoup(page.content , 'lxml')
    price = soup.find_all('div' , {'class' : 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all('span')[0].text

    return price


while True:
    print('Current price is ' + str(parsePrice()))  

    