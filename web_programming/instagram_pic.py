from datetime import datetime

from bs4 import BeautifulSoup

import requests

def download_image(url: str) -> str:
    """
    Download an image from a given URL by scraping the 'og:image' meta tag.

    Parameters:
        url (str): The URL to scrape.

    Returns:
        str: A message indicating the result of the operation.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        image_meta_tag = soup.find("meta", {"property": "og:image"})

        if image_meta_tag:
            image_url = image_meta_tag.get("content")
            if image_url:
                image_data = requests.get(image_url).content
                if image_data:
                    file_name = f"{datetime.now():%Y-%m-%d_%H:%M:%S}.jpg"
                    with open(file_name, "wb") as file:
                        file.write(image_data)
                    return f"Image downloaded and saved as {file_name}"
                else:
                    return "Failed to download the image."
            else:
                return "Image URL not found in the meta tag."
        else:
            return "No meta tag with 'og:image' property found."
    except requests.exceptions.RequestException as e:
        return f"An error occurred during the HTTP request: {e}"


if __name__ == "__main__":
    url = input("Enter image URL: ").strip()
    result = download_image(url)
    print(result)
