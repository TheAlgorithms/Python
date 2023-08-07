import bs4
import requests


def get_movie_data_from_soup(soup: bs4.element.ResultSet) -> dict[str, str]:
    return {
        "name": soup.h3.a.text,
        "genre": soup.find("span", class_="genre").text.strip(),
        "rating": soup.strong.text,
        "page_link": f"https://www.imdb.com{soup.a.get('href')}",
    }


def get_imdb_top_movies(num_movies: int = 5) -> tuple:
    """Get the top num_movies most highly rated movies from IMDB and
    return a tuple of dicts describing each movie's name, genre, rating, and URL.

    Args:
        num_movies: The number of movies to get. Defaults to 5.

    Returns:
        A list of tuples containing information about the top n movies.

    >>> len(get_imdb_top_movies(5))
    5
    >>> len(get_imdb_top_movies(-3))
    0
    >>> len(get_imdb_top_movies(4.99999))
    4
    """
    num_movies = int(float(num_movies))
    if num_movies < 1:
        return ()
    base_url = (
        "https://www.imdb.com/search/title?title_type="
        f"feature&sort=num_votes,desc&count={num_movies}"
    )
    source = bs4.BeautifulSoup(requests.get(base_url).content, "html.parser")
    return tuple(
        get_movie_data_from_soup(movie)
        for movie in source.find_all("div", class_="lister-item mode-advanced")
    )


if __name__ == "__main__":
    import json

    num_movies = int(input("How many movies would you like to see? "))
    print(
        ", ".join(
            json.dumps(movie, indent=4) for movie in get_imdb_top_movies(num_movies)
        )
    )
