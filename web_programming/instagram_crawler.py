#!/usr/bin/env python3
from __future__ import annotations

import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {"UserAgent": UserAgent().random}


def extract_user_profile(script) -> dict:
    """
    May raise json.decoder.JSONDecodeError
    """
    data = script.contents[0]
    info = json.loads(data[data.find('{"config"') : -1])
    return info["entry_data"]["ProfilePage"][0]["graphql"]["user"]


class InstagramUser:
    """
    Class Instagram crawl instagram user information

    Usage: (doctest failing on Travis CI)
    # >>> instagram_user = InstagramUser("github")
    # >>> instagram_user.is_verified
    True
    # >>> instagram_user.biography
    'Built for developers.'
    """

    def __init__(self, username):
        self.url = f"https://www.instagram.com/{username}/"
        self.user_data = self.get_json()

    def get_json(self) -> dict:
        """
        Return a dict of user information
        """
        html = requests.get(self.url, headers=headers).text
        scripts = BeautifulSoup(html, "html.parser").find_all("script")
        try:
            return extract_user_profile(scripts[4])
        except (json.decoder.JSONDecodeError, KeyError):
            return extract_user_profile(scripts[3])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.username}')"

    def __str__(self) -> str:
        return f"{self.fullname} ({self.username}) is {self.biography}"

    @property
    def username(self) -> str:
        return self.user_data["username"]

    @property
    def fullname(self) -> str:
        return self.user_data["full_name"]

    @property
    def biography(self) -> str:
        return self.user_data["biography"]

    @property
    def email(self) -> str:
        return self.user_data["business_email"]

    @property
    def website(self) -> str:
        return self.user_data["external_url"]

    @property
    def number_of_followers(self) -> int:
        return self.user_data["edge_followed_by"]["count"]

    @property
    def number_of_followings(self) -> int:
        return self.user_data["edge_follow"]["count"]

    @property
    def number_of_posts(self) -> int:
        return self.user_data["edge_owner_to_timeline_media"]["count"]

    @property
    def profile_picture_url(self) -> str:
        return self.user_data["profile_pic_url_hd"]

    @property
    def is_verified(self) -> bool:
        return self.user_data["is_verified"]

    @property
    def is_private(self) -> bool:
        return self.user_data["is_private"]


def test_instagram_user(username: str = "github") -> None:
    """
    A self running doctest
    >>> test_instagram_user()
    """
    from os import getenv

    if getenv("CONTINUOUS_INTEGRATION"):
        return  # test failing on Travis CI
    instagram_user = InstagramUser(username)
    assert instagram_user.user_data
    assert isinstance(instagram_user.user_data, dict)
    assert instagram_user.username == username
    if username != "github":
        return
    assert instagram_user.fullname == "GitHub"
    assert instagram_user.biography == "Built for developers."
    assert instagram_user.number_of_posts > 150
    assert instagram_user.number_of_followers > 120000
    assert instagram_user.number_of_followings > 15
    assert instagram_user.email == "support@github.com"
    assert instagram_user.website == "https://github.com/readme"
    assert instagram_user.profile_picture_url.startswith("https://instagram.")
    assert instagram_user.is_verified is True
    assert instagram_user.is_private is False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    instagram_user = InstagramUser("github")
    print(instagram_user)
    print(f"{instagram_user.number_of_posts = }")
    print(f"{instagram_user.number_of_followers = }")
    print(f"{instagram_user.number_of_followings = }")
    print(f"{instagram_user.email = }")
    print(f"{instagram_user.website = }")
    print(f"{instagram_user.profile_picture_url = }")
    print(f"{instagram_user.is_verified = }")
    print(f"{instagram_user.is_private = }")
