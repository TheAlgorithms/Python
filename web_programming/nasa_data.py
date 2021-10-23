import requests


def get_apod_data(api_key: str) -> dict:
    """
    Get the APOD(Astronomical Picture of the day) data
    Get the API Key from : https://api.nasa.gov/
    """
    url = "https://api.nasa.gov/planetary/apod/"
    return requests.get(url, params={"api_key": api_key}).json()


def get_archive_data(query: str) -> dict:
    """
    Get the data of a particular query from NASA archives
    """
    endpoint = "https://images-api.nasa.gov/search"
    return requests.get(endpoint, params={"q": query}).json()


if __name__ == "__main__":
    print(get_apod_data("YOUR API KEY"))
    print(
        get_archive_data("apollo 2011")["collection"]["items"][0]["data"][0][
            "description"
        ]
    )
