import requests
from bs4 import BeautifulSoup


def parse_dictionary(movie_dict: dict = {}) -> None:
    """Prints the movie dictionary.

    Args:
        movie_dict: The dictionary to print.

    >>> parse_dictionary({"name": "The Shawshank Redemption", "genre": "Drama",
    "rating": "9.3", "page link": "https://www.imdb.com/title/tt0111161/"})

    Movie:
    The Shawshank Redemption
    Genre:
    Drama
    Rating: 9.3
    Page Link: https://www.imdb.com/title/tt0111161/
    """
    print(f"\nMovie: {movie_dict['name']}")
    print(f"Genre: {movie_dict['genre']}")
    print(f"Rating: {movie_dict['rating']}")
    print(f"Page Link: {movie_dict['page link']}")


def crawl_imdb_topn_movies(num_movies: int = 5) -> None:
    """Crawls IMDB and prints the top n movies with their respective titles, genre,
    ratings, and imdb page link released.

    Args:
        num_movies: The number of movies to crawl. Defaults to 5.
    """

    print(f"Crawling {num_movies} movies from the IMDB database...")
    base_url = (
        f"https://www.imdb.com/search/title?title_type="
        f"feature&sort=num_votes,desc&count={num_movies}"
    )
    source = BeautifulSoup(requests.get(base_url).content, "html.parser")
    movies = source.find_all("div", class_="lister-item mode-advanced")
    movie_dict = {}
    for m in movies:
        movie_dict["name"] = "\n" + m.h3.a.text  # movie's name
        movie_dict["genre"] = m.find("span", attrs={"class": "genre"}).text  # genre
        movie_dict["rating"] = m.strong.text  # movie's rating
        movie_dict[
            "page link"
        ] = f"https://www.imdb.com{m.a.get('href')}"  # movie's page link
        parse_dictionary(movie_dict)


if __name__ == "__main__":
    crawl_imdb_topn_movies(input("How many movies would you like to see? "))
