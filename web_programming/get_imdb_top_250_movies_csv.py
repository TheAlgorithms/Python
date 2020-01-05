import requests
import csv
import os
from bs4 import BeautifulSoup


def movies(filename,path):
   
    os.chdir(filename)
    connect=requests.get(""" https://www.imdb.com/chart/top/?ref_=nv_mv_250 """)
    soup=BeautifulSoup(connect.text,'html.parser')
    elements_title=soup.find_all('td',attrs='titleColumn')
    elements_rating=soup.find_all('td',class_='ratingColumn imdbRating')
    Movies={}


    for i in range(len(elements_title)):
        title=elements_title[i].find('a').text
        rating=elements_rating[i].find('strong').text
        Movies[title]=Movies.get(title,rating)


    with open ('Top_250_Movies_IMDB.csv','w') as newfile:
        Writer=csv.writer(newfile)
        for Movie,Ratings in Movies.items():
            Writer.writerow([Movie,Ratings])
    


if __name__ == "__main__":



    try:
        filename=input("Please enter a name for the file to be stored:\n")+".csv"
        path=input('Enter the path you want to store the file:\n')
        movies(filename,path)
        print("Done")


    except:
        filename='Top_250_Movies_IMDB.csv'
        path=os.path.join(os.environ["HOMEPATH"], "Desktop")
        movies(filename,path)
        print("Done!")
