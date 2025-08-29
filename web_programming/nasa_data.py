# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

import httpx


def get_apod_data(api_key: str) -> dict:
    """
    Get the APOD(Astronomical Picture of the day) data
    Get your API Key from: https://api.nasa.gov/
    """
    url = "https://api.nasa.gov/planetary/apod"
    return httpx.get(url, params={"api_key": api_key}, timeout=10).json()


def save_apod(api_key: str, path: str = ".") -> dict:
    apod_data = get_apod_data(api_key)
    img_url = apod_data["url"]
    img_name = img_url.split("/")[-1]
    response = httpx.get(img_url, timeout=10)

    with open(f"{path}/{img_name}", "wb+") as img_file:
        img_file.write(response.content)
    del response
    return apod_data


def get_archive_data(query: str) -> dict:
    """
    Get the data of a particular query from NASA archives
    """
    url = "https://images-api.nasa.gov/search"
    return httpx.get(url, params={"q": query}, timeout=10).json()


if __name__ == "__main__":
    print(save_apod("YOUR API KEY"))
    apollo_2011_items = get_archive_data("apollo 2011")["collection"]["items"]
    print(apollo_2011_items[0]["data"][0]["description"])
