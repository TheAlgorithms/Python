"""
This script demonstrates fetching simple COVID-19 statistics from the
Worldometers archive site using lxml. lxml is chosen over BeautifulSoup
for its speed and convenience in Python web projects (such as Django or
Flask).
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
#     "lxml",
# ]
# ///
from __future__ import annotations

import argparse
import logging
from typing import NamedTuple

import httpx
from lxml import html


class CovidData(NamedTuple):
    cases: str
    deaths: str
    recovered: str


def covid_stats(
    url: str = (
        "https://web.archive.org/web/20250825095350/"
        "https://www.worldometers.info/coronavirus/"
    ),
) -> CovidData:
    xpath_str = '//div[@class = "maincounter-number"]/span/text()'
    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
    except httpx.TimeoutException:
        logging.error(
            "Request timed out. Please check your network connection "
            "or try again later."
        )
        return CovidData("N/A", "N/A", "N/A")
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        return CovidData("N/A", "N/A", "N/A")
    data: list[str] = html.fromstring(response.content).xpath(xpath_str)
    if len(data) != 3:
        logging.warning("Unexpected data format. The page structure may have changed.")
        return CovidData("N/A", "N/A", "N/A")

    return CovidData(*data)


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch COVID-19 statistics from Worldometers (archived)."
    )
    parser.add_argument(
        "--url",
        type=str,
        default=(
            "https://web.archive.org/web/20250825095350/"
            "https://www.worldometers.info/coronavirus/"
        ),
        help="Custom archive URL (default: latest snapshot).",
    )
    # args = parser.parse_args()
    args, _ = parser.parse_known_args()

    stats = covid_stats(args.url)
    fmt = (
        "Total COVID-19 cases in the world: {}\n"
        "Total deaths due to COVID-19 in the world: {}\n"
        "Total COVID-19 patients recovered in the world: {}"
    )
    print(fmt.format(*stats))


if __name__ == "__main__":
    main()
