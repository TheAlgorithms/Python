import requests
from requests.exceptions import HTTPError


def get_apod_data(api_key: str) -> dict:
    """
    Get the APOD(Astronomical Picture of the day) data
    Get the API Key from : https://api.nasa.gov/
    """
    try:
        return requests.get(
            f"https://api.nasa.gov/planetary/apod/?api_key={api_key}"
        ).json()
    except requests.exceptions.HTTPError:
        raise HTTPError


def get_archive_data(query: str) -> dict:
    """
    Get the data of a particular query from NASA archives
    """
    formatted_query = query.strip().replace(" ", "%")
    endpoint = f"https://images-api.nasa.gov/search?q={formatted_query}"
    try:
        return requests.get(endpoint).json()
    except requests.exceptions.HTTPError:
        raise HTTPError


if __name__ == "__main__":
    print(get_apod_data("YOUR API KEY"))
    print(get_archive_data("apollo 2011"))
