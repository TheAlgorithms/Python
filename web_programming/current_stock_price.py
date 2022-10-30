import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"

def stock_price(symbol:str) -> str:
    url = f"https://finance.yahoo.com/quote/{symbol}"
    
    page_content = requests.get(url,headers={
        "user-agent" : USER_AGENT
    }).content

    soup = BeautifulSoup(page_content, "html.parser")
    return soup.find(attrs={
        "data-symbol" : symbol,
        "data-field":"regularMarketPrice"
    }).text

if __name__ == "__main__":
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL ZOMATO.NS".split():
        print(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")
