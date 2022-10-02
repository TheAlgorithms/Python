import os
import urllib

import bs4 as bs
import requests


def get_links(url: str) -> list[str]:
    """
    Searches 4chan thread for all the available images

    Args:
        url: URL of 4chan thread
    
    Returns:
        list containing all image URLs
    """

    print("Retrieving UR:s...")

    page = requests.get(url)

    soup = bs.BeautifulSoup(page.content, "html.parser")

    results = soup.find_all(class_="fileText")

    links = []

    for i in results:
        k = i.find("a")
        links.append("https://" + k["href"][2:])

    return links


def save_links(links: list[str]) -> None:
    """
    Saves all image URLs to a file if user requests for it.

    Args:
        links: list containing all image URLs
    
    Returns:
        None
    """

    print("Saving links...")

    txt = ""
    for i in links:
        txt += i + "\n"

    with open("links.txt", "w+") as f:
        f.write(txt)

    print("File saved as `links.txt`")


def download(links:list[str]) -> None:
    """
    Downloads all the images from the list of URLs

    Args:
        links: List of URLs to download

    Returns:
        None
    """

    if not os.path.exists("4chan"):
        print("Creating `4chan` folder")
        os.makedirs("4chan")

    print("Starting download")
    for url in links:
        link = url.split("/")
        path = "4chan/" + link[len(link) - 1]
        urllib.request.urlretrieve(url, path)
        print("Saved file:", path, "from:", url)


def main() -> None:
    """
    Entry point for program

    Returns:
        None
    """
    url:str = input("URL of 4chan thread: ")
    _save:bool = (
        True
        if input("Save links? (overwrites [links.txt] if exists)[No]: ")
        in ["y", "yes", "true"]
        else False
    )

    links:list[str] = get_links(url)

    if _save:
        save_links(links)

    download(links)

    print("Done!")


if __name__ == "__main__":
    main()
