
from bs4 import BeautifulSoup
import requests

def imdb_top(imdb_top_n):
   base_url = "https://www.imdb.com/search/title?title_type=feature&sort=num_votes,desc&count="+imdb_top_n
   r = requests.get(base_url)
   source = BeautifulSoup(r.content, "lxml")

   top250 = source.findAll("div", attrs={"class": "lister-item mode-advanced"})

   for i in top250:
               print("\n"+i.find("h3").find("a").text) #movie's name
               print(i.find("span", attrs={"class": "genre"}).text) #genre
               print(i.find("strong").text) # movie's rating
               print("https://www.imdb.com"+i.find("a").get("href")) #movie's page link
               print("\n**************************************")


if __name__ == "__main__":
    print(imdb_top(str(input())))
