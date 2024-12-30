"""
Scraping jobs given job title and location from indeed website
"""

from __future__ import annotations

from collections.abc import Generator

import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.co.in/jobs?q=mobile+app+development&l="


def fetch_jobs(location: str = "mumbai") -> Generator[tuple[str, str]]:
    soup = BeautifulSoup(
        requests.get(url + location, timeout=10).content, "html.parser"
    )
    # This attribute finds out all the specifics listed in a job
    for job in soup.find_all("div", attrs={"data-tn-component": "organicJob"}):
        job_title = job.find("a", attrs={"data-tn-element": "jobTitle"}).text.strip()
        company_name = job.find("span", {"class": "company"}).text.strip()
        yield job_title, company_name


if __name__ == "__main__":
    for i, job in enumerate(fetch_jobs("Bangalore"), 1):
        print(f"Job {i:>2} is {job[0]} at {job[1]}")
