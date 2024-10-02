"""
Get the citation from google scholar
using title and year of publication, and volume and pages of journal.
"""

import requests
from bs4 import BeautifulSoup


def get_citation(base_url: str, params: dict) -> str:
    """
    Returns the citation number for a publication based on its title, journal, volume,
    pages, and year of publication.

    Parameters:
    - base_url: The base URL for making requests to Google Scholar.
    - params: A dictionary containing the publication information.

    Returns:
    - A string containing the number of citations.
    """
    # Send a GET request to the URL with the specified parameters
    soup = BeautifulSoup(
        requests.get(base_url, params=params, timeout=10).content, "html.parser"
    )

    # Find the div element with class 'gs_ri' that contains citation information
    div = soup.find("div", attrs={"class": "gs_ri"})

    # Find all links in the div and retrieve the third link (the citation count)
    anchors = div.find("div", attrs={"class": "gs_fl"}).find_all("a")

    return anchors[2].get_text()  # Return the text from the third link


if __name__ == "__main__":
    # Define parameters for the publication whose citation is to be searched
    params = {
        "title": (
            "Precisely geometry controlled microsupercapacitors for ultrahigh areal "
            "capacitance, volumetric capacitance, and energy density"
        ),
        "journal": "Chem. Mater.",
        "volume": 30,
        "pages": "3979-3990",
        "year": 2018,
        "hl": "en",  # Language to be used (English)
    }

    # Call the get_citation function with the specified URL and parameters
    print(get_citation("https://scholar.google.com/scholar_lookup", params=params))
