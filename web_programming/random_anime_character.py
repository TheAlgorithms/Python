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
    image = requests.get(image_url, headers=headers, timeout=10)
    with open(image_title, "wb") as file:
        file.write(image.content)


def random_anime_character() -> tuple[str, str, str]:
    """
    Returns the Title, Description, and Image Title of a random anime character .
    """
    soup = BeautifulSoup(
        requests.get(URL, headers=headers, timeout=10).text, "html.parser"
    )
    title = soup.find("meta", attrs={"property": "og:title"}).attrs["content"]
    image_url = soup.find("meta", attrs={"property": "og:image"}).attrs["content"]
    description = soup.find("p", id="description").get_text()
    _, image_extension = os.path.splitext(os.path.basename(image_url))
    image_title = title.strip().replace(" ", "_")
    image_title = f"{image_title}{image_extension}"
    save_image(image_url, image_title)
    return (title, description, image_title)


if __name__ == "__main__":
    title, desc, image_title = random_anime_character()
    print(f"{title}\n\n{desc}\n\nImage saved : {image_title}")
