from bs4 import BeautifulSoup
import requests


def imdb_top(imdb_top_n):
    base_url = (f"https://www.imdb.com/search/title?title_type="
                f"feature&sort=num_votes,desc&count={imdb_top_n}")
    source = BeautifulSoup(requests.get(base_url).content, "html.parser")
    for m in source.findAll("div", class_="lister-item mode-advanced"):
        print("\n" + m.h3.a.text)  # movie's name
        print(m.find("span", attrs={"class": "genre"}).text)  # genre
        print(m.strong.text)  # movie's rating
        print(f"https://www.imdb.com{m.a.get('href')}")  # movie's page link
        print("*" * 40)


if __name__ == "__main__":
    imdb_top(input("How many movies would you like to see? "))
