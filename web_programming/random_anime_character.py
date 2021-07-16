import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {"UserAgent": UserAgent().random}
URL = "https://www.mywaifulist.moe/random"

def save_image(image_url: str, image_title: str) -> None:
    """
    Saves the image of anime character
    """
    image = requests.get(image_url, headers=headers)
    with open(image_title, 'wb') as file:
        file.write(image.content)

def random_anime_character() -> None:
    """
    Returns the Name and Description of the anime character .
    """

    html = requests.get(URL, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find('meta', attrs={"property": "og:title"}).attrs["content"]
    image_url = soup.find('meta', attrs={"property": "og:image"}).attrs["content"]
    description = soup.find('p', id="description").get_text()

    print(f"{title}\n{description}")

    _ , image_extension = os.path.splitext(os.path.basename(image_url))
    image_title = title.strip().replace(" ", "_")
    image_title = f'{image_title}{image_extension}'

    save_image(image_url, image_title)
    print(f"Image Saved : {image_title}")


if __name__ == "__main__":
    random_anime_character()
