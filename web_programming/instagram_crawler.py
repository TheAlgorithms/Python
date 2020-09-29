#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Usage
"""
>>> user = Instagram("github")
>>> user.is_verified()
True
>>> user.get_biography()
Built for developers.

"""


class Instagram(object):
    """
    Class Instagram crawl instagram user information
    """

    def __init__(self, username):
        self.username = username
        self.url = "https://www.instagram.com/{}/".format(username)

    def get_json(self):
        """
        return json of user information
        """

        html = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(html.text, "html.parser")
        try:
            info = html_1(soup)
            return info
        except:
            info = html_2(soup)
            return info

    def get_followers(self):
        """
        return number of followers
        """

        info = self.get_json()
        followers = info["edge_followed_by"]["count"]
        return followers

    def get_followings(self):
        """
        return number of followings
        """

        info = self.get_json()
        following = info["edge_follow"]["count"]
        return following

    def get_posts(self):
        """
        return number of posts
        """

        info = self.get_json()
        posts = info["edge_owner_to_timeline_media"]["count"]
        return posts

    def get_biography(self):
        """
        return biography of user
        """

        info = self.get_json()
        bio = info["biography"]
        return bio

    def get_fullname(self):
        """
        return fullname of the user
        """

        info = self.get_json()
        fullname = info["full_name"]
        return fullname

    def get_username(self):
        """
        return the username of the user
        """

        info = self.get_json()
        username = info["username"]
        return username

    def get_profile_pic(self):
        """
        return the link of profile picture
        """

        info = self.get_json()
        pic = info["profile_pic_url_hd"]
        return pic

    def get_website(self):
        """
        return the users's website link
        """

        info = self.get_json()
        external_url = info["external_url"]
        return external_url

    def get_email(self):
        """
        return the email id of user if
        available
        """

        info = self.get_json()
        return info["business_email"]

    def is_verified(self):
        """
        check the user is verified
        """

        info = self.get_json()
        return info["is_verified"]

    def is_private(self):
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


user = Instagram("github")
print(user.is_verified())
print(user.get_biography())

