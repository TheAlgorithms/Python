"""Get the site emails from URL."""

from __future__ import annotations

__author__ = "Muhammad Umer Farooq"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Alpha"

import re
from html.parser import HTMLParser
from urllib import parse

import requests


class Parser(HTMLParser):
    def __init__(self, domain: str) -> None:
        super().__init__()
        self.urls: list[str] = []
        self.domain = domain

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """
        This function parse html to take takes url from tags
        """
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, not empty nor # print it and not already in urls.
                if (
                    name == "href"
                    and value != "#"
                    and value != ""
                    and value not in self.urls
                ):
                    url = parse.urljoin(self.domain, value)
                    self.urls.append(url)


# Get main domain name (example.com)
def get_domain_name(url: str) -> str:
    """
    This function get the main domain name

    >>> get_domain_name("https://a.b.c.d/e/f?g=h,i=j#k")
    'c.d'
    >>> get_domain_name("Not a URL!")
    ''
    """
    return ".".join(get_sub_domain_name(url).split(".")[-2:])


# Get sub domain name (sub.example.com)
def get_sub_domain_name(url: str) -> str:
    """
    >>> get_sub_domain_name("https://a.b.c.d/e/f?g=h,i=j#k")
    'a.b.c.d'
    >>> get_sub_domain_name("Not a URL!")
    ''
    """
    return parse.urlparse(url).netloc


def emails_from_url(url: str = "https://github.com") -> list[str]:
    """
    This function takes url and return all valid urls
    """
    # Get the base domain from the url
    domain = get_domain_name(url)

    # Initialize the parser
    parser = Parser(domain)

    try:
        # Open URL
        r = requests.get(url)

        # pass the raw HTML to the parser to get links
        parser.feed(r.text)

        # Get links and loop through
        valid_emails = set()
        for link in parser.urls:
            # open URL.
            # read = requests.get(link)
            try:
                read = requests.get(link)
                # Get the valid email.
                emails = re.findall("[a-zA-Z0-9]+@" + domain, read.text)
                # If not in list then append it.
                for email in emails:
                    valid_emails.add(email)
            except ValueError:
                pass
    except ValueError:
        raise SystemExit(1)

    # Finally return a sorted list of email addresses with no duplicates.
    return sorted(valid_emails)


if __name__ == "__main__":
    emails = emails_from_url("https://github.com")
    print(f"{len(emails)} emails found:")
    print("\n".join(sorted(emails)))
