import re
import urllib.parse

import requests
from bs4 import BeautifulSoup


def is_valid_url(url):
    """
    Function Valid the url
    """

    regex = re.compile(
        r"^(?:http|ftp)s?://"
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)"
        r"+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        r"(?::\d+)?"
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return re.match(regex, url) is not None


def get_links(url):
    """
    Function get all links in website
    """

    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    data = [link.get("href") for link in soup.find_all("a")]
    links = []
    for link in data:
        if not is_valid_url(link):
            links.append(urllib.parse.urljoin(url + "/", link))
        else:
            links.append(link)
    return links


def test_get_links(url: str = "https://www.github.com") -> None:
    """
    A doctest for get_links function
    >>> test_get_links()
    """

    assert len(get_links(url)) == 144
    for url in get_links(url):
        assert is_valid_url(url) is True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    links = get_links("https://www.github.com")
    print(f"Total {len(links)} are found")
    for link in links:
        print(link)
