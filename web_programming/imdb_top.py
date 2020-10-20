import requests
from bs4 import BeautifulSoup
import helper

def validate_input(movie_count):
    try:
        if not movie_count:
            raise UnboundLocalError("Count must not be empty")
        int_count = int(movie_count)
        return int_count
    except (UnboundLocalError,ValueError,TypeError) as e:
        with helper.disable_exception_traceback():
            raise(e)
            
def imdb_top(imdb_top_n):
    '''
    Args:
        imdb_top_n: Movie count provided by user. Integer value.
    Returns:
        None
    '''
    base_url = (
        f"https://www.imdb.com/search/title?title_type="
        f"feature&sort=num_votes,desc&count={imdb_top_n}"
    )
    source = BeautifulSoup(requests.get(base_url).content, "html.parser")
    for i, m in enumerate(source.findAll("div", class_="lister-item mode-advanced")):
        print(f"\n{i+1}. {m.h3.a.text}")  # serial no and movie's name
        print(m.find("span", attrs={"class": "genre"}).text)  # genre
        print(m.strong.text)  # movie's rating
        print(f"https://www.imdb.com{m.a.get('href')}")  # movie's page link
        print("*" * 40)


if __name__ == "__main__":
    movie_count = input("How many movies would you like to see? ")
    imdb_top(validate_input(movie_count))
