"""
Fetch the current price of a cryptocurrency in USD using CoinGecko API.
"""

import httpx


def crypto_price(coin: str = "bitcoin") -> float:
    """
    Return the current price of a cryptocurrency in USD using CoinGecko API.

    >>> isinstance(crypto_price("bitcoin"), float)
    True
    >>> isinstance(crypto_price("ethereum"), float)
    True
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
        return float(response.json().get(coin, {}).get("usd", 0.0))
    except (httpx.RequestError, ValueError, KeyError):
        return 0.0


if __name__ == "__main__":
    print(crypto_price("bitcoin"))
