"""
Author - AyushSehrawat
"""

# Imports the needed modules
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

""" Function to get emails from the url """
def getMails(num : int) -> None:
    count = 0
    """
    Keep a check on range
    """
    try:
        while len(urls):
            count += 1
            if count == num:
                break
            url = urls.popleft()
            scraped_urls.add(url)
            # Add to the set

            parts = urllib.parse.urlsplit(url)
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            # Forms a base url

            path = url[:url.rfind('/') + 1] if '/' in parts.path else url

            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema,
                    requests.exceptions.ConnectionError):
                continue

            new_emails = set(
                re.findall(r"[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+",
                        response.text, re.I))
            # A regex search to find emails
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, features='lxml')

            """
            Find links
            """
            for anchor in soup.find_all("a"):
                link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                if not link in urls and not link in scraped_urls:
                    urls.append(link)

    except KeyboardInterrupt:
        print('[-] Closing')


if __name__ == '__main__':
    user_url = "https://google.com" # Example Url
    urls = deque([user_url])

    """
    These set store emails and prevent repeating emails 
    """
    scraped_urls = set()
    emails = set()

    """
    Num = How much loops you want )

    """
    num = 10
    getMails(num)

    """
    Finally prints the mails
    You can also return the emails ( optional)
    """
    for mail in emails:
        print(mail)