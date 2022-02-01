from urllib.error import HTTPError
from xml.dom import NotFoundErr

import requests
from bs4 import BeautifulSoup, NavigableString
from fake_useragent import UserAgent

BASE_URL = "https://ww1.gogoanime2.org"


def search_scraper(anime_name: str) -> list:

    """[summary]

    This function will take an url and
    return list of anime after scraping the site.

    >>> type(search_scraper("demon_slayer"))
    <class 'list'>

    Args:
        anime_name (str): [Name of anime]

    Raises:
        e: [Raises exception on failure]

    Returns:
        [list]: [List of animes]
    """

    try:

        # concat the name to form the search url.
        search_url = f"{BASE_URL}/search/{anime_name}"
        response = requests.get(
            search_url, headers={"UserAgent": UserAgent().chrome}
        )  # request the url.

        # Is the response ok?
        response.raise_for_status()

        # parse with soup.
        soup = BeautifulSoup(response.text, "html.parser")

        # get list of anime
        items_ul = soup.find("ul", {"class": "items"})
        items_li = items_ul.children

        # for each anime, insert to list. the name and url.
        anime_list = []
        for li in items_li:
            if not isinstance(li, NavigableString):
                anime_url, anime_title = li.find("a")["href"], li.find("a")["title"]
                anime_list.append(
                    {
                        "title": anime_title,
                        "url": anime_url,
                    }
                )

        return anime_list

    except (requests.exceptions.RequestException, HTTPError, TypeError) as e:
        raise e


def search_anime_episode_list(episode_endpoint: str) -> list:

    """[summary]

    This function will take an url and
    return list of episodes after scraping the site
    for an url.

    >>> type(search_anime_episode_list("/anime/kimetsu-no-yaiba"))
    <class 'list'>

    Args:
        episode_endpoint (str): [Endpoint of episode]

    Raises:
        e: [description]

    Returns:
        [list]: [List of episodes]
    """

    try:

        request_url = f"{BASE_URL}{episode_endpoint}"
        response = requests.get(
            url=request_url, headers={"UserAgent": UserAgent().chrome}
        )
        soup = BeautifulSoup(response.text, "html.parser")

        # With this id. get the episode list.
        episode_page_ul = soup.find("ul", {"id": "episode_related"})
        episode_page_li = episode_page_ul.children

        episode_list = []
        for children in episode_page_li:
            try:
                if not isinstance(children, NavigableString):
                    episode_list.append(
                        {
                            "title": children.find(
                                "div", {"class": "name"}
                            ).text.replace(" ", ""),
                            "url": children.find("a")["href"],
                        }
                    )
            except (KeyError, NotFoundErr, TypeError):
                pass

        return episode_list

    except (requests.exceptions.RequestException) as e:
        raise e


def get_anime_episode(episode_endpoint: str) -> list:

    """[summary]

    Get click url and download url from episode url

    >>> type(get_anime_episode("/watch/kimetsu-no-yaiba/1"))
    <class 'list'>

    Args:
        episode_endpoint (str): [Endpoint of episode]

    Raises:
        e: [description]

    Returns:
        [list]: [List of download and watch url]
    """

    try:

        episode_page_url = f"{BASE_URL}{episode_endpoint}"

        response = requests.get(
            url=episode_page_url, headers={"User-Agent": UserAgent().chrome}
        )
        soup = BeautifulSoup(response.text, "lxml")

        episode_url = soup.find("iframe", {"id": "playerframe"})["src"]
        download_url = episode_url.replace("/embed/", "/playlist/") + ".m3u8"
        return [f"{BASE_URL}{episode_url}", f"{BASE_URL}{download_url}"]

    except (
        KeyError,
        NotFoundErr,
        TypeError,
        requests.exceptions.RequestException,
    ) as e:
        raise e


if __name__ == "__main__":

    try:

        anime_name = input("Enter anime name: ").strip()
        anime_list = search_scraper(anime_name)
        print("\n")

        if len(anime_list) == 0:
            print("No anime found with this name")
        else:

            print(f"Found {len(anime_list)} results: ")
            for (i, anime) in enumerate(anime_list):
                anime_title = anime["title"]
                print(f"{i+1}. {anime_title}")

            anime_choice = int(
                input("\nPlease choose from the following list: ").strip()
            )
            chosen_anime = anime_list[anime_choice - 1]
            print(f"You chose {chosen_anime['title']}. Searching for episodes...")

            episode_list = search_anime_episode_list(chosen_anime["url"])
            if len(episode_list) == 0:
                print("No episode found for this anime")
            else:
                print(f"Found {len(episode_list)} results: ")
                for (i, episode) in enumerate(episode_list):
                    print(f"{i+1}. {episode['title']}")

                episode_choice = int(
                    input("\nChoose an episode by serial no: ").strip()
                )
                chosen_episode = episode_list[episode_choice - 1]
                print(f"You chose {chosen_episode['title']}. Searching...")

                episode_url, download_url = get_anime_episode(chosen_episode["url"])
                print(f"\nTo watch, ctrl+click on {episode_url}.")
                print(f"To download, ctrl+click on {download_url}.")

    except (ValueError, IndexError, TypeError) as e:
        raise e
