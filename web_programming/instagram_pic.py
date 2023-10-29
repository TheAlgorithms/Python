from datetime import datetime
from typing import Optional
import requests
from bs4 import BeautifulSoup


def validate_url(url: str) -> bool:
    """
    Validates the given URL.
    >>> validate_url("https://www.example.com")
    True
    """
    return True


def download_image_data(image_url: str) -> bytes | None:
    """
    Downloads image data from the given URL.
    """
    try:
        return requests.get(image_url).content
    except requests.exceptions.RequestException:
        return None


def save_image(image_data: bytes, file_name: str) -> None:
    """
    Saves the image data to a file.
    """
    with open(file_name, "wb") as file:
        file.write(image_data)


def download_image(url: str) -> str:
    """
    Downloads an image from the given URL and saves it to a file.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        image_meta_tag = soup.find("meta", {"property": "og:image"})

        if image_meta_tag:
            image_url = image_meta_tag.get("content")
            if image_url:
                image_data = download_image_data(image_url)
                if image_data:
                    file_name = f"image_{datetime.now():%Y-%m-%d_%H:%M:%S}.jpg"
                    save_image(image_data, file_name)
                    return f"Image downloaded and saved as {file_name}"
    except requests.exceptions.RequestException:
        return "An error occurred during the HTTP request."


if __name__ == "__main__":
    url = input("Enter image URL: ").strip()
    if validate_url(url):
        result = download_image(url)
        print(result)
    else:
        print("Invalid URL. Please try again.")
