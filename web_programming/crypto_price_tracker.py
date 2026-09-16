"""
Fetch the current price of a cryptocurrency in USD using CoinGecko API.
"""

# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx2",
# ]
# ///

import httpx2


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
        json_response = httpx2.get(url, timeout=10).raise_for_status().json()
        return float(response.json().get(coin, {}).get("usd", 0.0))
    except (httpx2.RequestError, ValueError, KeyError):
        return 0.0
    return float(json_response.get(coin, {}).get("usd", 0.0))


if __name__ == "__main__":
    print(f"{crypto_price('bitcoin') = }")
