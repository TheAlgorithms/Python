# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

from __future__ import annotations

import csv

import httpx
from bs4 import BeautifulSoup


def get_imdb_top_250_movies(url: str = "") -> dict[str, float]:
    url = url or "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    soup = BeautifulSoup(httpx.get(url, timeout=10).text, "html.parser")
    titles = soup.find_all("h3", class_="ipc-title__text")
    ratings = soup.find_all("span", class_="ipc-rating-star--rating")
    return {
        title.a.text: float(rating.strong.text)
        for title, rating in zip(titles, ratings)
    }


def write_movies(filename: str = "IMDb_Top_250_Movies.csv") -> None:
    movies = get_imdb_top_250_movies()
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Movie title", "IMDb rating"])
        for title, rating in movies.items():
            writer.writerow([title, rating])


if __name__ == "__main__":
    write_movies()
