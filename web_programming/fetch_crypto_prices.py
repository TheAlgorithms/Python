"""
Fetch current cryptocurrency prices using the CoinGecko API.
This script uses the 'httpx' library as per the repository's preference.
"""

from __future__ import annotations
import httpx

def fetch_crypto_price(coin_id: str = "bitcoin") -> dict[str, dict[str, float]]:
    """
    Fetch the current price of a cryptocurrency in USD.
    :param coin_id: The ID of the coin (e.g., 'bitcoin', 'ethereum', 'dogecoin')
    :return: A dictionary containing the price data.

    >>> # Note: Actual API call results may vary over time.
    >>> isinstance(fetch_crypto_price("bitcoin"), dict)
    True
    >>> "bitcoin" in fetch_crypto_price("bitcoin")
    True
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    
    with httpx.Client() as client:
        response = client.get(url)
        if response.status_code != 200:
            raise ValueError(f"Could not fetch price for {coin_id}. Status code: {response.status_code}")
        
        data = response.json()
        if not data:
            raise ValueError(f"Invalid coin ID: {coin_id}")
            
        return data

if __name__ == "__main__":
    try:
        coin = "bitcoin"
        price_data = fetch_crypto_price(coin)
        price = price_data[coin]["usd"]
        print(f"The current price of {coin.capitalize()} is ${price:,.2f} USD")
    except Exception as e:
        print(f"Error: {e}")