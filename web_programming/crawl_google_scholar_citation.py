"""
Get the citation from google scholar
using title and year of publication, and volume and pages of journal.
"""

import requests
from bs4 import BeautifulSoup


def get_citation(base_url: str, params: dict) -> str:
    """
    Return the citation number.
    """
    soup = BeautifulSoup(requests.get(base_url, params=params).content, "html.parser")
    get_div = soup.find("div", attrs={"class": "gs_ri"})
    get_a_tag = get_div.find("div", attrs={"class": "gs_fl"}).findAll("a")
    citation = get_a_tag[2].get_text()
    if "Cited" not in citation:
        citation = "Cited by 0"

    return citation.replace("Cited by ", "")


if __name__ == "__main__":
    params = {
        "title": (
            "Precisely geometry controlled microsupercapacitors"
            " for ultrahigh areal capacitance,"
            " volumetric capacitance, and energy density"
        ),
        "journal_name": "Chem. Mater.",
        "volume": "30",
        "page": "3979-3990",
        "year": "2018",
    }

    print(get_citation("http://scholar.google.com/scholar_lookup?hl=en&", params=params))
