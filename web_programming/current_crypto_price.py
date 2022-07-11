import yfinance as yf

def crypto_prices(tickers: list ) -> str:
    """Get the latest price of cryptocurrencies using 
    Yahoo's publicly available API.

    Args:
        tickers (list): cryptocurrency Symbols

    Returns:
        String: latest closing prices

    >>> crypto_prices(["BTC-UaSD"])
    - BTC-UASD: No data found, symbol may be delisted
    """

    results = []

    for ticker in tickers:

        try:
            crypto_yahoo = yf.Ticker(ticker)
            data = crypto_yahoo.history()
            price = data['Close'].iloc[-1]   

        except IndexError:
            continue


        results.append((ticker, price))

        return results


if __name__ == "__main__":

    import doctest

    doctest.testmod()

    