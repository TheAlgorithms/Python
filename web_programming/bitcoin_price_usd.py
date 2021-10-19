"""
a python script that gets the closing price of bitcoin
from the past seven days
"""
from typing import List

import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

ROOT_URL = "https://finance.yahoo.com/quote/BTC-USD/history/"
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


def btc_close_price() -> List[float]:
    """
    a function that gets a list closing prices of bitcoin in USD
    from the past seven days
    """
    options = Options()
    firefox_browser = Firefox(options=options)
    firefox_browser.implicitly_wait(30)
    firefox_browser.get(ROOT_URL)
    # soup = firefox_browser.find_element_by_tag_name('table')
    soup = firefox_browser.page_source

    df = pd.read_html(soup)[0]
    # get a list of the first seven closing prices in a list format
    df_close_prices = df["Close*"][:7].tolist()
    # convert each element in the list to a float
    close_prices = [float(i) for i in df_close_prices]
    return close_prices


print(btc_close_price())
