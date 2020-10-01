import re

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


def is_valid_url(url):
    """
    Function Valid the url
    """

    regex = re.compile(
        r"^(?:http|ftp)s?://"
        r"""(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)
        +(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"""
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

    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    data = [link.get("href") for link in soup.find_all("a")]
    links = []
    for link in data:
        if not is_valid_url(link):
            links.append(urllib.parse.urljoin(url, link))
        else:
            links.append(link)
    return links


if __name__ == "__main__":
    links = get_links("https://www.github.com")
    print(f"Total {len(links)} are found")
    for link in links:
        print(link)
