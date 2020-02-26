"""Get the site emails from URL."""
__author__ = "Muhammad Umer Farooq"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Alpha"

import re
import requests
from html.parser import HTMLParser
from urllib import parse


class Parser(HTMLParser):
    def __init__(self, domain):
        HTMLParser.__init__(self)
        self.data = []
        self.domain = domain

    def handle_starttag(self, tag, attrs):
        """
        This function parse html to take takes url from tags
        """
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, and not empty nor # print it.
                if name == "href" and value != "#" and value != "":
                    # If not already in data.
                    if value not in self.data:
                        url = parse.urljoin(self.domain, value)
                        self.data.append(url)


# Get main domain name (example.com)
def get_domain_name(url):
    """
    This function get the main domain name
    """
    return ".".join(get_sub_domain_name(url).split(".")[-2:])


# Get sub domain name (sub.example.com)
def get_sub_domain_name(url):
    """
    This function get sub domin name
    """
    return parse.urlparse(url).netloc


def emails_from_url(url: str = "https://github.com") -> list:
    """
    This function takes url and return all valid urls
    """
    # Get the base domain from the url
    domain = get_domain_name(url)

    # Initialize the parser
    parser = Parser(domain)

    # Validate Email regx.
    emailRegx = "[a-zA-Z0-9]+@" + domain

    # Open URL
    r = requests.get(url)

    # pass the raw HTML to the parser to get links
    parser.feed(r.text)

    # Store Email Data structure.
    Emails = []
    # Get links and loop through
    for link in parser.data:
        # open URL.
        # read = requests.get(link)
        read = requests.get(link)
        # Get the valid email.
        email = re.findall(emailRegx, read.text)
        # If not in list then append it.
        if email not in Emails:
            Emails.append(email)

    ValidEmails = []

    # Remove duplicates email address.
    for Email in Emails:
        for e in Email:
            if e not in ValidEmails:
                ValidEmails.append(e)

    # Finally print list of email.
    return ValidEmails


if __name__ == "__main__":
    emails = emails_from_url("https://github.com")
    print(f"{len(emails)} emails found:")
    print("\n".join(sorted(emails)))
