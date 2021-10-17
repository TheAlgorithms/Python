"""
Get Covid-19 daily statistic from disease.sh
"""

import requests

API_URL = "https://disease.sh/v3/covid-19/all"

def fetch_data() -> list:
    return requests.get(API_URL).json()

if __name__ == "__main__":
    data = fetch_data()
    print(f"Today cases: {data['todayCases']:,}")
    print(f"Today recovered: {data['todayRecovered']:,}")
    print(f"Today deaths: {data['todayDeaths']:,}")
    print(f"Total cases: {data['cases']:,}")
    print(f"Total recovered: {data['recovered']:,}")
    print(f"Total deaths: {data['deaths']:,}")