"""
This file fetches quotes from the " ZenQuotes API ".
It does not require any API key as it uses free tier.

For more details and premium features visit:
    https://zenquotes.io/
"""

import pprint

import requests


def quote_of_the_day() -> list:
    api_endpoint_url = "https://zenquotes.io/api/today/"
    return requests.get(api_endpoint_url).json()


def random_quotes() -> list:
    api_endpoint_url = "https://zenquotes.io/api/random/"
    return requests.get(api_endpoint_url).json()


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
