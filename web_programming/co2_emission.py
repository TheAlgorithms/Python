"""
İngiltere Karbon Yoğunluğu API'sinden CO2 emisyon verilerini alın
"""

from datetime import date
import requests

BASE_URL = "https://api.carbonintensity.org.uk/intensity"

# Son yarım saatteki emisyon
def fetch_last_half_hour() -> str:
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
        last_half_hour = response.json()["data"][0]
        return last_half_hour["intensity"]["actual"]
    except requests.RequestException as e:
        print(f"Veri alınırken hata oluştu: {e}")
        return "Veri alınamadı"

# Belirli bir tarih aralığındaki emisyonlar
def fetch_from_to(start: date, end: date) -> list:
    try:
        response = requests.get(f"{BASE_URL}/{start}/{end}", timeout=10)
        response.raise_for_status()
        return response.json()["data"]
    except requests.RequestException as e:
        print(f"Veri alınırken hata oluştu: {e}")
        return []

if __name__ == "__main__":
    start_date = date(2020, 10, 1)
    end_date = date(2020, 10, 3)
    for entry in fetch_from_to(start=start_date, end=end_date):
        print(f"from {entry['from']} to {entry['to']}: {entry['intensity']['actual']}")
    print(f"fetch_last_half_hour() = {fetch_last_half_hour()}")
