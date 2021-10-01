import webbrowser
import sys
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def show_images_from_google_query(query: str = "dhaka"):
    """Searches google using the provided query term and opens the google image
    tab in a browser.

    Args:
        query : The image search term to be provided by the user. Defaults to
        "dhaka".
    """

    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    url = "https://www.google.com/search?q=" + query
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = list(soup.select(".eZt8xd"))
    print(links)
    for link in links:
        if link.text == "Images":
            print("here")
            print(link.get("href"))
            webbrowser.open(f"http://google.com{link.get('href')}")
            break

        else:
            print(f"Google search images not available for term {query}.")


if __name__ == "__main__":
    show_images_from_google_query(sys.argv[1:])
