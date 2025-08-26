"""
Get the citation from google scholar
using title and year of publication, and volume and pages of journal.
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

import httpx
from bs4 import BeautifulSoup


def get_citation(base_url: str, params: dict) -> str:
    """
    Return the citation number.
    """
    soup = BeautifulSoup(
        httpx.get(base_url, params=params, timeout=10).content, "html.parser"
    )
    div = soup.find("div", attrs={"class": "gs_ri"})
    anchors = div.find("div", attrs={"class": "gs_fl"}).find_all("a")
    return anchors[2].get_text()


if __name__ == "__main__":
    params = {
        "title": (
            "Precisely geometry controlled microsupercapacitors for ultrahigh areal "
            "capacitance, volumetric capacitance, and energy density"
        ),
        "journal": "Chem. Mater.",
        "volume": 30,
        "pages": "3979-3990",
        "year": 2018,
        "hl": "en",
    }
    print(get_citation("https://scholar.google.com/scholar_lookup", params=params))
