import shutil
from datetime import UTC, datetime

import requests


def get_apod_data(api_key: str) -> dict:
    """
    APOD (Astronomical Picture of the Day) verilerini alır.
    API Anahtarınızı şu adresten alın: https://api.nasa.gov/
    """
    url = "https://api.nasa.gov/planetary/apod"
    try:
        response = requests.get(url, params={"api_key": api_key}, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"hata": f"APOD verilerini alırken bir hata oluştu: {e}"}


def save_apod(api_key: str, path: str = ".") -> dict:
    apod_data = get_apod_data(api_key)
    if "hata" in apod_data:
        return apod_data

    img_url = apod_data["url"]
    img_name = f"{datetime.now(tz=UTC).astimezone():%Y-%m-%d_%H:%M:%S}_{img_url.split('/')[-1]}"
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(f"{path}/{img_name}", "wb+") as img_file:
            shutil.copyfileobj(response.raw, img_file)
        del response
        return apod_data
    except requests.exceptions.RequestException as e:
        return {"hata": f"APOD resmini kaydederken bir hata oluştu: {e}"}


def get_archive_data(query: str) -> dict:
    """
    NASA arşivlerinden belirli bir sorgunun verilerini alır.
    """
    url = "https://images-api.nasa.gov/search"
    try:
        response = requests.get(url, params={"q": query}, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"hata": f"Arşiv verilerini alırken bir hata oluştu: {e}"}


if __name__ == "__main__":
    api_key = input("API Anahtarınızı girin: ").strip()
    print(save_apod(api_key))
    apollo_2011_items = get_archive_data("apollo 2011").get("collection", {}).get("items", [])
    if apollo_2011_items:
        print(apollo_2011_items[0]["data"][0]["description"])
    else:
        print("Apollo 2011 verileri bulunamadı.")
