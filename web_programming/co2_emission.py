"""
Get CO2 emission data from the UK CarbonIntensity API
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

from datetime import date

import httpx

BASE_URL = "https://api.carbonintensity.org.uk/intensity"


# Emission in the last half hour
def fetch_last_half_hour() -> str:
    last_half_hour = httpx.get(BASE_URL, timeout=10).json()["data"][0]
    return last_half_hour["intensity"]["actual"]


# Emissions in a specific date range
def fetch_from_to(start, end) -> list:
    return httpx.get(f"{BASE_URL}/{start}/{end}", timeout=10).json()["data"]


if __name__ == "__main__":
    for entry in fetch_from_to(start=date(2020, 10, 1), end=date(2020, 10, 3)):
        print("from {from} to {to}: {intensity[actual]}".format(**entry))
    print(f"{fetch_last_half_hour() = }")
