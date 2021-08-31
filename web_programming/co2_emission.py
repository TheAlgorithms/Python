"""
Get CO2 emission data from the UK CarbonIntensity API
"""
from datetime import date

import requests

BASE_URL = "https://api.carbonintensity.org.uk/intensity"


# Emission in the last half hour
def fetch_last_half_hour() -> str:
    last_half_hour = requests.get(BASE_URL).json()["data"][0]
    return last_half_hour["intensity"]["actual"]


# Emissions in a specific date range
def fetch_from_to(start, end) -> list:
    return requests.get(f"{BASE_URL}/{start}/{end}").json()["data"]


if __name__ == "__main__":
    for entry in fetch_from_to(start=date(2020, 10, 1), end=date(2020, 10, 3)):
        print("from {from} to {to}: {intensity[actual]}".format(**entry))
    print(f"{fetch_last_half_hour() = }")
