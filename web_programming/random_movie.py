import requests
import bs4
from fake_useragent import UserAgent

MOVIES_URL = "https://www.coolgenerator.com/random-movie-generator"


def get_imdb_link(movie_title: str) -> str:
    """
        Return the IMDB url of the movie title
    Args:
        movie_title (str): Movie title

    Returns:
        str: Imdb Url of the movie
    """
    url = f"https://www.imdb.com/find?q={movie_title.replace(' ', '+')}"
    try:
        for _ in range(2):
            response = requests.get(url, headers={"User-Agent": UserAgent().firefox})
            if response.ok:
                break
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        imdb_link = soup.find("a", {"class": "ipc-metadata-list-summary-item__t"})
        url_imdb = "https://www.imdb.com" + imdb_link.attrs["href"]

    except Exception:
        return ""

    return url_imdb


def get_movie_images(movies: bs4.element.Tag) -> list:
    """
        Return a list of movies image

    Args:
        movies (bs4.element.Tag): BS4 element tag

    Returns:
        list: List of the movies images
    """
    images = []
    for imgs in movies.select("img"):
        src = "https:" + imgs.get("src")
        images.append(src)
    return images


def get_movies(num_movies: int) -> None:
    """
        Print the list of movies

    Args:
        num_movies (int): Number of movies
    """
    count = 0
    while True:
        response = requests.get(MOVIES_URL, headers={"UserAgent": UserAgent().chrome})
        soup = bs4.BeautifulSoup(response.content, "html.parser")

        movies_ul = soup.find("ul", {"class": "list-unstyled content-list"})
        images = get_movie_images(movies_ul)

        for idx, movie in enumerate(movies_ul.contents):
            if movie.name != "li":
                break
            if count >= num_movies:
                return
            title = (movie.contents[2].text).replace("(", " (")
            genre = (movie.contents[3].contents[1].text).replace(",", ", ")
            rate = movie.contents[3].contents[3].text
            imdb = get_imdb_link(title)

            print(f"TITLE: {title}")
            print(f"GENRE: {genre}")
            print(f"RATING: {float(rate):.1f}")
            print(f"IMDb: {imdb}")
            print(f"IMAGE URL: {images[idx]}\n")
            count += 1


if __name__ == "__main__":

    num_movies = int(input("Enter a number of movies: ").strip())
    print("\n🎥 Picking movies ...\n")
    get_movies(num_movies)
