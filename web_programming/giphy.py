#!/usr/bin/env python3
import requests


def get_gifs(query: str, api_key: str) -> list[str]:
    """
    Verilen bir sorguya dayalı olarak GIF URL'lerinin bir listesini alın.
    """
    formatted_query = "+".join(query.split())
    url = f"https://api.giphy.com/v1/gifs/search?q={formatted_query}&api_key={api_key}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        gifs = response.json()["data"]
        return [gif["url"] for gif in gifs]
    except requests.exceptions.RequestException as e:
        return [f"İstek hatası: {e}"]
    except ValueError as e:
        return [f"JSON ayrıştırma hatası: {e}"]


if __name__ == "__main__":
    giphy_api_key = input("Giphy API anahtarınızı girin: ")
    query = input("Aramak istediğiniz GIF sorgusunu girin: ")
    print("\n".join(get_gifs(query, giphy_api_key)))
