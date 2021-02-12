"""
Author - AyushSehrawat
"""

import re
import sys
import urllib.parse
from collections import deque

import requests
import requests.exceptions

# Imports the needed modules
from bs4 import BeautifulSoup

"""
Info -
Function to get emails from the url,
It first find the email and links on first page , then go to the
links find and find some more links
and emails. This process goes on , depending on the loops
"""


def getmails(num: int) -> None:
    """
    This functions returns nothing.
    It just adds the emails to set. Which are later printed.
    """
    count = 0
    # Keep a check on range
    try:
        while urls:
            count += 1
            if count == num:
                break
            url = urls.popleft()
            scraped_urls.add(url)
            # Add to the set

            parts = urllib.parse.urlsplit(url)
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            # Forms a base url

            path = url[: url.rfind("/") + 1] if "/" in parts.path else url

            try:
                response = requests.get(url)
            except (
                requests.exceptions.MissingSchema,
                requests.exceptions.ConnectionError,
            ):
                continue

            new_emails = set(
                email_pattern = r"[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+"
                new_emails = set(re.findall(email_pattern, response.text, re.I))
                    r"[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+",
                    response.text,
                    re.I,
                )
            )
            # A regex search to find emails
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, features="lxml")

            # Find links

            for anchor in soup.find_all("a"):
                link = anchor.attrs.get("href", "")
                if link.startswith("/"):
                    link = base_url + link
                elif not link.startswith("http"):
                    link = path + link
                if link not in urls and link not in scraped_urls:
                    urls.append(link)

    except KeyboardInterrupt:
        print("[-] Processing interrupted.")
        sys.exit(1)


if __name__ == "__main__":
    user_url = "https://google.com"  # Example Url
    urls = deque([user_url])

    """
    These set store emails and prevent repeating emails,
    Set prevents duplicating of data
    """
    scraped_urls = set()
    emails = set()

    # Num = How much loops you want )

    num = 10
    getmails(num)

    """
    Finally prints the mails
    You can also return the emails ( optional)
    """
    for email in get_emails():
        print(mail)
