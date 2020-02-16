"""Get the site emails from URL."""
__author__ = "Muhammad Umer Farooq"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Production"

from html.parser import HTMLParser
import requests
import re
from urllib.parse import urlparse

from urllib import parse


class Parser(HTMLParser):

    def __init__(self, domain):
        HTMLParser.__init__(self)
        self.data = []
        self.domain = domain

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, and not empty nor # print it.
                if name == "href" and value != "#" and value != '':
                    # If not already in data.
                    if value not in self.data:
                        url = parse.urljoin(self.domain, value)
                        self.data.append(url)


# Get main domain name (example.com)
def get_domain_name(url):
    try:
        u = get_sub_domain_name(url).split('.')
        return u[-2] + '.' + u[-1]
    except:
        return ""


# Get sub domain name (sub.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

# Get the url
url = "https://github.com"
# Get the base domain from the url
domain = get_domain_name(url)

# Initialize the parser
parser = Parser(domain)

# Validate Email regx.
emailRegx = '[a-zA-Z0-9]+@' + domain
try:
    # Open URL
    r = requests.get(url)
except:
    print("Please provide the valid url")

# pass the raw HTML to the parser to get links
parser.feed(r.text)

# Store Email Data structure.
Emails = []
# Get links and loop through
for link in parser.data:
    # open URL.
    # read = requests.get(link)
    try:
        read = requests.get(link)
        # Get the valid email.
        email = re.findall(emailRegx, read.text)
        # If not in list then append it.
        if email not in Emails:
            Emails.append(email)
    except:
        pass

ValidEmails = []

# Remove duplicates email address.
for Email in Emails:
    for e in Email:
        if e not in ValidEmails:
            ValidEmails.append(e)

# Finally print list of email.
print(ValidEmails)
