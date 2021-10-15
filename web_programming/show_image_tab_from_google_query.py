import sys
import webbrowser

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def show_images_from_google_query(query: str = "dhaka") -> bool:
    """Searches google using the provided query term and opens the google image
    tab in a browser.

    Args:
        query : The image search term to be provided by the user. Defaults to
        "dhaka".

    Returns:
        True if the image tab is opened successfully.

    >>> show_images_from_google_query ()
    True

    >>> show_images_from_google_query ("potato")
    True
    """

    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    url = "https://www.google.com/search?q=" + query
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select(".eZt8xd"):
        if link.text == "Images":
            webbrowser.open(f"http://google.com{link.get('href')}")
            return True
    return False


if __name__ == "__main__":
    show_images_from_google_query(sys.argv[1])
