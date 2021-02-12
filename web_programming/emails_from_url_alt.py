"""
Author - AyushSehrawat
"""

import re
import sys
import urllib.parse
from collections import deque

import requests

# Imports the needed modules
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, MissingSchema

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

            # Get new url to scrape and remove the scraped url from urls
            url = urls.popleft()
            scraped_urls.add(url)
            # Add to the set

            parts = urllib.parse.urlsplit(url)
            print(parts)
            base_url = f"{parts.scheme}://{parts.netloc}"
            # Forms a base url

            path = url[: url.rfind("/") + 1] if "/" in parts.path else url

            try:
                response = requests.get(url)
            except (
                MissingSchema,
                ConnectionError,
            ):
                continue

            new_emails = set(
                re.findall(
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
        print("[-] Processing interrupted")
        """
        Print the emails which are in the set, in case user wants to
        stop the script and get partial emails
        """
        for mail in emails:
            print(mail)
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
    for mail in emails:
        print(mail)
