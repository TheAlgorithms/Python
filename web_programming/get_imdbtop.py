import requests
from bs4 import BeautifulSoup


def crawl_imdb_topn_movies(num_movies: int = 5) -> list:
    """Crawls IMDB and return a list of tuples containing
    the top n movies with their respective titles, genre,
    ratings, and imdb page link released.

    Args:
        num_movies: The number of movies to crawl. Defaults to 5.

    Returns:
        A list of tuples containing information about the top n movies.

    >>> len(crawl_imdb_topn_movies(5)) == int(5)
    True
    >>> len(crawl_imdb_topn_movies(-3)) == int(0)
    True
    >>> len(crawl_imdb_topn_movies(4.6)) == int(4)
    True
    """
    num_movies = int(float(num_movies))
    if int(num_movies) < 1:
        return []
    base_url = (
        f"https://www.imdb.com/search/title?title_type="
        f"feature&sort=num_votes,desc&count={num_movies}"
    )
    source = BeautifulSoup(requests.get(base_url).content, "html.parser")
    movies = source.find_all("div", class_="lister-item mode-advanced")
    total_movies_list = []
    movie_dict = {}
    for m in movies:
        movie_dict["name"] = "\n" + m.h3.a.text  # movie's name
        movie_dict["genre"] = m.find("span", attrs={"class": "genre"}).text
        movie_dict["rating"] = m.strong.text  # movie's rating
        movie_dict["page link"] = f"https://www.imdb.com{m.a.get('href')}"
        total_movies_list.append(movie_dict)
    return total_movies_list


if __name__ == "__main__":
    num_movies = int(float(input("How many movies would you like to see? ")))
    crawl_imdb_topn_movies(num_movies)
