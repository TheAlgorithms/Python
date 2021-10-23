import shutil

import requests


def get_apod_data(api_key: str, download: bool = False, path: str = ".") -> dict:
    """
    Get the APOD(Astronomical Picture of the day) data
    Get the API Key from : https://api.nasa.gov/
    """
    url = "https://api.nasa.gov/planetary/apod/"
    data = requests.get(url, params={"api_key": api_key}).json()
    if download:
        img_url = data["url"]
        img_name = img_url.split("/")[-1]
        response = requests.get(img_url, stream=True)

        with open(f"{path}/{img_name}", "wb+") as img_file:
            shutil.copyfileobj(response.raw, img_file)
        del response
    return data


def get_archive_data(query: str) -> dict:
    """
    Get the data of a particular query from NASA archives
    """
    endpoint = "https://images-api.nasa.gov/search"
    return requests.get(endpoint, params={"q": query}).json()


if __name__ == "__main__":
    print(get_apod_data("YOUR API KEY", download=True, path="/home/Pictures"))
    print(
        get_archive_data("apollo 2011")["collection"]["items"][0]["data"][0][
            "description"
        ]
    )
