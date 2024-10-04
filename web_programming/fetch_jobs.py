"""
Verilen iş unvanı ve konuma göre Indeed web sitesinden iş ilanlarını kazıma
"""

from __future__ import annotations

from collections.abc import Generator

import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.co.in/jobs?q=mobile+app+development&l="


def fetch_jobs(location: str = "mumbai") -> Generator[tuple[str, str], None, None]:
    soup = BeautifulSoup(
        requests.get(url + location, timeout=10).content, "html.parser"
    )
    # Bu özellik, bir işte listelenen tüm ayrıntıları bulur
    for job in soup.find_all("div", attrs={"data-tn-component": "organicJob"}):
        job_title = job.find("a", attrs={"data-tn-element": "jobTitle"}).text.strip()
        company_name = job.find("span", {"class": "company"}).text.strip()
        yield job_title, company_name


if __name__ == "__main__":
    for i, job in enumerate(fetch_jobs("Bangalore"), 1):
        print(f"İş {i:>2} : {job[0]} şirketinde {job[1]}")
