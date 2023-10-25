import os
import requests
from bs4 import BeautifulSoup

def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

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
                    print(f"Image downloaded and saved as {file_name}")
                else:
                    print("Failed to download the image.")
            else:
                print("Image URL not found in the meta tag.")
        else:
            print("No meta tag with 'og:image' property found.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the HTTP request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter image URL: ").strip()
    print(f"Downloading image from {url} ...")
    download_image(url)
