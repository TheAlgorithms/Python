"""
Scraping jobs given job title and location from Indeed website
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

from __future__ import annotations
from collections.abc import Generator
import httpx
from bs4 import BeautifulSoup

BASE_URL = "https://www.indeed.co.in/jobs"


def fetch_jobs(
    job_title: str = "mobile app development", location: str = "mumbai"
) -> Generator[tuple[str, str], None, None]:
    """
    Scrape job postings from Indeed for a given job title and location.

    Args:
        job_title: Keywords to search for (default: "mobile app development").
        location: City or region to search jobs in (default: "mumbai").

    Yields:
        Tuples of (job title, company name).

    Example:
        >>> jobs = list(fetch_jobs("python developer", "Bangalore"))
        >>> isinstance(jobs[0], tuple)
        True
    """
    headers = {"User-Agent": "Mozilla/5.0 (compatible; JobScraper/1.0)"}
    params = {"q": job_title, "l": location}

    response = httpx.get(BASE_URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    for job in soup.find_all("div", attrs={"data-tn-component": "organicJob"}):
        title_tag = job.find("a", attrs={"data-tn-element": "jobTitle"})
        company_tag = job.find("span", {"class": "company"})
        if title_tag and company_tag:
            yield title_tag.text.strip(), company_tag.text.strip()


if __name__ == "__main__":
    for i, (title, company) in enumerate(
        fetch_jobs("python developer", "Bangalore"), 1
    ):
        print(f"Job {i:>2} is {title} at {company}")
