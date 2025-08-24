# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

from datetime import UTC, datetime

import httpx
from bs4 import BeautifulSoup


def download_image(url: str) -> str:
    """
    Download an image from a given URL by scraping the 'og:image' meta tag.

    Parameters:
        url: The URL to scrape.

    Returns:
        A message indicating the result of the operation.
    """
    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
    except httpx.RequestError as e:
        return f"An error occurred during the HTTP request to {url}: {e!r}"

    soup = BeautifulSoup(response.text, "html.parser")
    image_meta_tag = soup.find("meta", {"property": "og:image"})
    if not image_meta_tag:
        return "No meta tag with property 'og:image' was found."

    image_url = image_meta_tag.get("content")
    if not image_url:
        return f"Image URL not found in meta tag {image_meta_tag}."

    try:
        image_data = httpx.get(image_url, timeout=10).content
    except httpx.RequestError as e:
        return f"An error occurred during the HTTP request to {image_url}: {e!r}"
    if not image_data:
        return f"Failed to download the image from {image_url}."

    file_name = f"{datetime.now(tz=UTC).astimezone():%Y-%m-%d_%H-%M-%S}.jpg"
    with open(file_name, "wb") as out_file:
        out_file.write(image_data)
    return f"Image downloaded and saved in the file {file_name}"


if __name__ == "__main__":
    url = input("Enter image URL: ").strip() or "https://www.instagram.com"
    print(f"download_image({url}): {download_image(url)}")
