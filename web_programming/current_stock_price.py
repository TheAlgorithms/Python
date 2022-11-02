import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"


def stock_price(symbol: str) -> str:
    """
    fetches the stock price and return it in string
    """
    assert isinstance(symbol, str), "symbol value must be type of 'str'"

    url = f"https://finance.yahoo.com/quote/{symbol}"

    page_content = requests.get(url, headers={"user-agent": USER_AGENT}).content

    soup = BeautifulSoup(page_content, "html.parser")
    ele = soup.find(attrs={"data-symbol": symbol, "data-field": "regularMarketPrice"})
    return ele.text.strip() if ele is not None else ""


if __name__ == "__main__":
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL ZOMATO.NS".split():
        print(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")
