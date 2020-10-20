import doctest

import requests
from bs4 import BeautifulSoup


def imdb_top(imdb_top_n: int) -> None:
    r"""
    >>> imdb_top(2)             # doctest: +NORMALIZE_WHITESPACE
    1. The Shawshank Redemption
    <BLANKLINE>
    Drama
    9.3
    https://www.imdb.com/title/tt0111161/
    ----------------------------------------
    2. The Dark Knight
    <BLANKLINE>
    Action, Crime, Drama
    9.0
    https://www.imdb.com/title/tt0468569/
    ----------------------------------------
    >>> imdb_top('jskjksas')    # doctest: +NORMALIZE_WHITESPACE
    Sorry! couldn't understand your choice. Let's show you the highest rated movie details.
    1. The Shawshank Redemption
    <BLANKLINE>
    Drama
    9.3
    https://www.imdb.com/title/tt0111161/
    ----------------------------------------
    >>> imdb_top('')    # doctest: +NORMALIZE_WHITESPACE
    Sorry! couldn't understand your choice. Let's show you the highest rated movie details.
    1. The Shawshank Redemption
    <BLANKLINE>
    Drama
    9.3
    https://www.imdb.com/title/tt0111161/
    ----------------------------------------
    """
    try:
        if not imdb_top_n:
            raise UnboundLocalError()
        imdb_top_n = int(imdb_top_n)
    except (ValueError, UnboundLocalError):
        print(
            "\nSorry! couldn't understand your choice. Let's show you the highest rated movie details.\n"
        )
        imdb_top_n = 1

    base_url = (
        f"https://www.imdb.com/search/title?title_type="
        f"feature&sort=num_votes,desc&count={imdb_top_n}"
    )
    source = BeautifulSoup(requests.get(base_url).content, "html.parser")
    for i, m in enumerate(source.findAll("div", class_="lister-item mode-advanced")):
        print(f"{i+1}. {m.h3.a.text}")  # serial number followed by movie name
        print(m.find("span", attrs={"class": "genre"}).text)  # genre
        print(m.strong.text)  # movie's rating
        print(f"https://www.imdb.com{m.a.get('href')}")  # movie's page link
        print("-" * 40)


if __name__ == "__main__":
    doctest.testmod()
    movie_count = input(
        "How many movies would you like to see [default set to 1]? "
    ).strip()
    imdb_top(movie_count)
