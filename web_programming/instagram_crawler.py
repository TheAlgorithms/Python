#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Usage
"""
>>> user = Instagram("github")
>>> user.is_verified
True
>>> user.get_biography
Built for developers.

"""


class InstagramUser:
    """
    Class Instagram crawl instagram user information
    """

    def __init__(self, username):
        self.username = username
        self.url = f"https://www.instagram.com/{username}/"

    def get_json(self):
        """
        return json of user information
        """

        html = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(html.text, "html.parser")
        try:
            return html_1(soup)
        except json.decoder.JSONDecodeError:
            return html_2(soup)

    @property
    def no_of_followers(self) -> int:
        """
        return number of followers
        """

        info = self.get_json()
        return info["edge_followed_by"]["count"]

    @property
    def no_of_followings(self) -> int:
        """
        return number of followings
        """

        info = self.get_json()
        return info["edge_follow"]["count"]

    @property
    def no_of_posts(self) -> int:
        """
        return number of posts
        """

        info = self.get_json()
        return info["edge_owner_to_timeline_media"]["count"]

    @property
    def get_biography(self) -> str:
        """
        return biography of user
        """

        info = self.get_json()
        return info["biography"]

    @property
    def get_fullname(self) -> str:
        """
        return fullname of the user
        """

        info = self.get_json()
        return info["full_name"]

    @property
    def get_username(self) -> str:
        """
        return the username of the user
        """

        info = self.get_json()
        return info["username"]

    @property
    def get_profile_pic(self) -> str:
        """
        return the link of profile picture
        """

        info = self.get_json()
        return info["profile_pic_url_hd"]

    @property
    def get_website(self) -> str:
        """
        return the users's website link
        """

        info = self.get_json()
        return info["external_url"]

    @property
    def get_email(self) -> str:
        """
        return the email id of user if
        available
        """

        info = self.get_json()
        return info["business_email"]

    @property
    def is_verified(self) -> bool:
        """
        check the user is verified
        """

        info = self.get_json()
        return info["is_verified"]

    @property
    def is_private(self) -> bool:
        """
        check user is private
        """

        info = self.get_json()
        return info["is_private"]


def html_1(soup):
    scripts = soup.find_all("script")
    main_scripts = scripts[4]
    data = main_scripts.contents[0]
    info_object = data[data.find('{"config"') : -1]
    info = json.loads(info_object)
    info = info["entry_data"]["ProfilePage"][0]["graphql"]["user"]
    return info


def html_2(soup):
    scripts = soup.find_all("script")
    main_scripts = scripts[3]
    data = main_scripts.contents[0]
    info_object = data[data.find('{"config"') : -1]
    info = json.loads(info_object)
    info = info["entry_data"]["ProfilePage"][0]["graphql"]["user"]
    return info


if __name__ == "__main__":
    user = InstagramUser("github")
    print(f"{user.is_verified = }")
    print(f"{user.get_biography = }")
