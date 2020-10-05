import re
import urllib.parse

import requests
from bs4 import BeautifulSoup

"""
Source of regex of URL
https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
"""


def is_valid_url(url: str) -> bool:
    """
    >>> is_valid_url("https://example.com/account.htm?birth=blow")
    True
    >>> is_valid_url("ftp://example.com/file.png")
    True
    >>> is_valid_url("https://www.google.com")
    True
    >>> is_valid_url("https://httpbin.org/ip")
    True
    >>> is_valid_url("https://localhost")
    True
    >>> is_valid_url("ftp://joebozobl123internet.address.edu")
    True
    >>> is_valid_url("https://github.com")
    True
    >>> is_valid_url("http://example.org")
    True
    >>> is_valid_url("www.google.com")
    False
    >>> is_valid_url("https://www.google")
    True
    >>> is_valid_url("google.com")
    False
    >>> is_valid_url("/images/index.png")
    False
    >>> is_valid_url("../bin/files.zip")
    False
    >>> is_valid_url("/#")
    False
    >>> is_valid_url("https://123.com")
    True
    >>> is_valid_url("https://bit.ly/3kYK3rQ")
    True
    >>> is_valid_url("https://bitly.is/34fp0KV")
    True
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


def get_links(url: str) -> list:
    """
    Function get all links in website
    >>> len(get_links("https://www.tic.com/index.html"))
    11
    """

    html = requests.get(url).text
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    data = [link.get("href") for link in soup.find_all("a")]
    links = []
    for link in data:
        if not is_valid_url(link):
            links.append(urllib.parse.urljoin(url + "/", link))
        else:
            links.append(link)
    return links


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    links = get_links("https://www.tic.com/index.html")
    print(f"Total {len(links)} are found")
    for link in links:
        print(link)
