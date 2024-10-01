#!/usr/bin/env python3

"""
Provide the current worldwide COVID-19 statistics.
This data is being scraped from 'https://www.worldometers.info/coronavirus/'.
"""

import requests
from bs4 import BeautifulSoup


def world_covid19_stats(url: str = "https://www.worldometers.info/coronavirus") -> dict:
    """
    Return a dictionary of current worldwide COVID-19 statistics.
    
    The function scrapes COVID-19 statistics from the Worldometer website. 
    It returns key metrics such as total cases, deaths, and recoveries.
    
    :param url: URL of the website to scrape data from (default is Worldometer COVID-19 page).
    :return: A dictionary containing the key COVID-19 statistics.
    :raises: Exception if there is an issue with the request or scraping.
    """
    try:
        # Make a GET request to the URL and create a BeautifulSoup object
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for request errors
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the keys (labels) and values (statistics)
        keys = soup.findAll("h1")
        values = soup.findAll("div", {"class": "maincounter-number"})
        keys += soup.findAll("span", {"class": "panel-title"})
        values += soup.findAll("div", {"class": "number-table-main"})

        # Create and return a dictionary of COVID-19 statistics
        return {key.text.strip(): value.text.strip() for key, value in zip(keys, values)}
    
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return {}
    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return {}


if __name__ == "__main__":
    print("\033[1m COVID-19 Status of the World \033[0m\n")
    
    stats = world_covid19_stats()

    # If stats is empty, inform the user that something went wrong
    if stats:
        print("\n".join(f"{key}\n{value}" for key, value in stats.items()))
    else:
        print("Could not retrieve the COVID-19 statistics.")
