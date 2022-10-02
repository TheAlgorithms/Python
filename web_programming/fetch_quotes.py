"""
This file fetches quotes from the " ZenQuotes API ".
It does not require any API key as it uses free tier.

For more details and premium features visit:
    https://zenquotes.io/
"""

import pprint

import requests


def quote_of_the_day() -> list:
    API_ENDPOINT_URL = "https://zenquotes.io/api/today/"
    return requests.get(API_ENDPOINT_URL).json()


def random_quotes() -> list:
    API_ENDPOINT_URL = "https://zenquotes.io/api/random/"
    return requests.get(API_ENDPOINT_URL).json()


if __name__ == "__main__":
    """
    response object has all the info with the quote
    To retrieve the actual quote access the response.json() object as below
    response.json() is a list of json object
        response.json()[0]['q'] = actual quote.
        response.json()[0]['a'] = author name.
        response.json()[0]['h'] = in html format.
    """
    response = random_quotes()
    pprint.pprint(response)
