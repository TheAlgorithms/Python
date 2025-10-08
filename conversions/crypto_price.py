"""
Convert ETH (Ethereum) to USD using live or static conversion rates.

Fetches current ETH price from CoinGecko API or uses fallback rate.
Source: https://api.coingecko.com/api/v3/simple/price
"""


def eth_to_usd(eth_amount: float, eth_price_usd: float = 2000.0) -> float:
    """
    Convert ETH amount to USD equivalent.

    Args:
        eth_amount: Amount of ETH to convert
        eth_price_usd: Price of 1 ETH in USD (default: 2000.0)

    Returns:
        USD equivalent of the ETH amount

    Raises:
        ValueError: If eth_amount or eth_price_usd is negative

    >>> eth_to_usd(1.0, 2000.0)
    2000.0
    >>> eth_to_usd(0.5, 3000.0)
    1500.0
    >>> eth_to_usd(0, 2000.0)
    0.0
    >>> eth_to_usd(-1, 2000.0)
    Traceback (most recent call last):
        ...
    ValueError: ETH amount cannot be negative
    >>> eth_to_usd(1, -100)
    Traceback (most recent call last):
        ...
    ValueError: ETH price cannot be negative
    """
    if eth_amount < 0:
        raise ValueError("ETH amount cannot be negative")
    if eth_price_usd < 0:
        raise ValueError("ETH price cannot be negative")

    return eth_amount * eth_price_usd


def get_live_eth_price() -> float:
    """
    Fetch current ETH price from CoinGecko API.

    Returns:
        Current ETH price in USD, or 2000.0 if request fails

    >>> price = get_live_eth_price()
    >>> isinstance(price, float)
    True
    """
    try:
        import requests

        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "ethereum", "vs_currencies": "usd"},
            timeout=10,
        )
        response.raise_for_status()
        return response.json()["ethereum"]["usd"]
    except (ImportError, requests.RequestException, KeyError):
        return 2000.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Interactive example
    live_price = get_live_eth_price()
    result = eth_to_usd(1.0, live_price)
    print(f"1 ETH = ${result:,.2f} USD (${live_price:,.2f}/ETH)")
