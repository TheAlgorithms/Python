"""
Fetches jokes from JokesAPI

More information: https://v2.jokeapi.dev
"""

import requests

API_ENDPOINT_URL = "https://v2.jokeapi.dev/"


def random_joke() -> list:
    """
    Returns:
        list: If single joke, returns [joke].
        If two-part joke, returns [setup, delivery]
    """
    response = requests.get(API_ENDPOINT_URL + "joke/Any").json()
    if response["type"] == "single":
        return [response["joke"]]
    else:
        return [response["setup"], response["delivery"]]


def joke_from_id(joke_id: int) -> list:
    """
    Args:
        joke_id (int): id number of joke

    Returns:
        list: If single joke, returns [joke].
        If two-part joke, returns [setup, delivery]

    >>> joke_from_id(10)
    ['Hey, wanna hear a joke?', 'Parsing HTML with regex.']
    >>> joke_from_id(14)
    ["What do you call a developer who doesn't comment code?", 'A developer.']

    """
    response = requests.get(API_ENDPOINT_URL + f"joke/Any?idRange={joke_id}").json()
    if response["type"] == "single":
        return [response["joke"]]
    else:
        return [response["setup"], response["delivery"]]


if __name__ == "__main__":

    from doctest import testmod

    testmod()
