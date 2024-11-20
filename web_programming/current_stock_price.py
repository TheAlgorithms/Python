from doctest import testmod

from bs4 import BeautifulSoup
from requests import get


def stock_price(symbol: str = "AAPL") -> str:
    """
    >>> stock_price("EEEE")
    '-'
    >>> isinstance(float(stock_price("GOOG")),float)
    True
    """
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}"
    yahoo_finance_source = get(
        url, headers={"USER-AGENT": "Mozilla/5.0"}, timeout=10
    ).text
    soup = BeautifulSoup(yahoo_finance_source, "html.parser")
    specific_fin_streamer_tag = soup.find("fin-streamer", {"data-testid": "qsp-price"})

    if specific_fin_streamer_tag:
        text = specific_fin_streamer_tag.get_text()
        return text
    return "No <fin-streamer> tag with the specified data-test attribute found."


# Search for the symbol at https://finance.yahoo.com/lookup
if __name__ == "__main__":
    testmod()
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL".split():
        print(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")
