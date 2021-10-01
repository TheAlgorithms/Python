import requests
from bs4 import BeautifulSoup


def print_imdb_topn_movies(num_movies: int = 5) -> None:
    """Crawls IMDB and prints the top n movies with their respective titles, genre,
    ratings, and imdb page link released.

    Args:
        num_movies: The number of movies to crawl. Defaults to 5.

    >>> print_imdb_topn_movies()
    The Shawshank Redemption

    Drama
    9.3
    https://www.imdb.com/title/tt0111161/
    ****************************************

    The Dark Knight

    Action, Crime, Drama
    9.0
    https://www.imdb.com/title/tt0468569/
    ****************************************

    Inception

    Action, Adventure, Sci-Fi
    8.8
    https://www.imdb.com/title/tt1375666/
    ****************************************

    Fight Club

    Drama
    8.8
    https://www.imdb.com/title/tt0137523/
    ****************************************

    Pulp Fiction

    Crime, Drama
    8.9
    https://www.imdb.com/title/tt0110912/
    ****************************************

    >>> print_imdb_topn_movies(2)
    The Shawshank Redemption

    Drama
    9.3
    https://www.imdb.com/title/tt0111161/
    ****************************************

    The Dark Knight

    Action, Crime, Drama
    9.0
    https://www.imdb.com/title/tt0468569/
    ****************************************
    """
    base_url = (
        f"https://www.imdb.com/search/title?title_type="
        f"feature&sort=num_votes,desc&count={num_movies}"
    )
    source = BeautifulSoup(requests.get(base_url).content, "html.parser")
    for m in source.findAll("div", class_="lister-item mode-advanced"):
        print("\n" + m.h3.a.text)  # movie's name
        print(m.find("span", attrs={"class": "genre"}).text)  # genre
        print(m.strong.text)  # movie's rating
        print(f"https://www.imdb.com{m.a.get('href')}")  # movie's page link
        print("*" * 40)


if __name__ == "__main__":
    print_imdb_topn_movies(input("How many movies would you like to see? "))
