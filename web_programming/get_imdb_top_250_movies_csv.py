from __future__ import annotations

import csv

import requests
from bs4 import BeautifulSoup


def get_imdb_top_250_movies(url: str = "") -> dict[str, float]:
    url = url or "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    titles = soup.find_all("td", attrs="titleColumn")
    ratings = soup.find_all("td", class_="ratingColumn imdbRating")
    years = soup.find_all("td", class_ ="yearColumn releasingYear")
    return {
        title.a.text: float(rating.strong.text): int(year.strong.text)
        for title, rating, year in zip(titles, ratings, years)
    }


def write_movies(filename: str = "IMDb_Top_250_Movies.csv") -> None:
    movies = get_imdb_top_250_movies()
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Movie title", "IMDb rating", "Year of Release"])
        for title, rating, year in movies.items():
            writer.writerow([title, rating, year])


if __name__ == "__main__":
    write_movies()
