"""
Convert ETH to USD using real-time price data from CoinGecko.
"""

# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
# ]
# ///

import httpx

COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
)


def get_eth_price_usd() -> float:
    """Fetch the current ETH price in USD."""
    response = httpx.get(COINGECKO_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["ethereum"]["usd"]


def eth_to_usd(eth_amount: float) -> float:
    """Convert ETH amount to USD."""
    return eth_amount * get_eth_price_usd()


if __name__ == "__main__":
    eth_amount = float(input("Enter ETH amount: "))
    usd_value = eth_to_usd(eth_amount)
    print(f"{eth_amount} ETH = ${usd_value:.2f} USD")
