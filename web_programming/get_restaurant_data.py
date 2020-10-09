#!/usr/bin/env python
# coding: utf-8

# In[22]:


import requests

API_KEY = ""  # <-- Enter your free API key here.
ROOT_URL = "https://developers.zomato.com/api/v2.1/"


def search_for_restaurants(API_KEY, latitude, longitude):
    """
    Return a list of restaurants based on the parameters provided.
    >>> search_for_restaurants("35a8539481b022dfcce8a69e1746f049", 40.7128, 74.0060)
    <Response [200]>
    """
    headers = {"user-key": API_KEY}
    MODIFIED_URL = ROOT_URL + "/search?lat=" + str(latitude) + "&lon=" + str(longitude)
    response = requests.get(MODIFIED_URL, headers=headers)
    return response


def get_restaurant_details(API_KEY, restaurant_id):
    """
    Return details of a restaurant based on Restaurant ID provided.
    >>> get_restaurant_details("35a8539481b022dfcce8a69e1746f049", 16507624)
    <Response [200]>
    """
    headers = {"user-key": API_KEY}
    MODIFIED_URL = ROOT_URL + "/restaurant?res_id=" + str(restaurant_id)
    response = requests.get(MODIFIED_URL, headers=headers)
    return response


def get_restaurant_menu(API_KEY, restaurant_id):
    """
    Return the menu of a restaurant.
    >>> get_restaurant_menu("35a8539481b022dfcce8a69e1746f049", 16507624)
    <Response [200]>
    """
    headers = {"user-key": API_KEY}
    MODIFIED_URL = ROOT_URL + "/dailymenu?res_id=" + str(restaurant_id)
    response = requests.get(MODIFIED_URL, headers=headers)
    return response


def get_city_details(API_KEY, city_name):
    """
    Return details of a city based on the name.
    >>> get_city_details("35a8539481b022dfcce8a69e1746f049", "New York")
    <Response [200]>
    """
    headers = {"user-key": API_KEY}
    MODIFIED_URL = ROOT_URL + "/cities?q=" + str(city_name)
    response = requests.get(MODIFIED_URL, headers=headers)
    return response


def get_restaurant_reviews(API_KEY, restaurant_id):
    """
    Return reviews of a particular restaurant given the ID.
    >>> get_restaurant_reviews("35a8539481b022dfcce8a69e1746f049", 16507624)
    <Response [200]>
    """
    headers = {"user-key": API_KEY}
    MODIFIED_URL = ROOT_URL + "/reviews?res_id=" + str(restaurant_id)
    response = requests.get(MODIFIED_URL, headers=headers)
    return response


if __name__ == "__main__":
    import doctest

    doctest.testmod()
