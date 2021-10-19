"""
a python script that gets the closing price of bitcoin
from the past seven days
"""
from typing import List

import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


def btc_close_price(url: str) -> List[float]:
    """
    a function that gets a list closing prices of bitcoin in USD
    from the past seven days.
    the urls are being shortened by bitly in order for it to be flake8 compliant.
    >>> btc_close_price("https://yhoo.it/3pcVYYt")
    [60892.18, 61593.95, 57321.52, 57401.1, 56041.06, 57484.79, 54771.58]
    >>> btc_close_price("https://yhoo.it/3vnaE8o")
    [8037.54, 8166.55, 7879.07, 8079.86, 8163.69, 7769.22, 7411.32]
    >>> btc_close_price("https://yhoo.it/3aQlxGb")
    [3742.7, 3865.95, 3820.41, 3923.92, 3654.83, 3857.3, 3815.49]
    """
    options = Options()
    firefox_browser = Firefox(options=options)
    firefox_browser.implicitly_wait(30)
    firefox_browser.get(url)
    # soup = firefox_browser.find_element_by_tag_name('table')
    soup = firefox_browser.page_source

    df = pd.read_html(soup)[0]
    # get a list of the first seven closing prices in a list format
    df_close_prices = df["Close*"][:7].tolist()
    # convert each element in the list to a float
    close_prices = [float(i) for i in df_close_prices]
    return close_prices


if __name__ == "__main__":
    url = "https://finance.yahoo.com/quote/BTC-USD/history/"
    print(btc_close_price(url))
