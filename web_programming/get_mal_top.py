import csv

import requests
from bs4 import BeautifulSoup

def mal_top(top_n, airing=False, csv_file=False):

    base_url = "https://myanimelist.net/topanime.php?"
    if airing:
        base_url += "type=airing&"

    if csv_file:
        csv_file_ = open(csv_file, "w")
        csv_writer = csv.writer(csv_file_)
        csv_writer.writerow(["Rank", "Anime title", "Episodes", "Aired", "Score"])

    url = base_url
    rank = 1
    while (rank < top_n):
        source = BeautifulSoup(requests.get(url).content, "html.parser")
        for anime in source.findAll("tr", class_="ranking-list"):
            info = anime.findAll("td")
            rank = int(info[0].getText(strip=True))
            info_ = info[1].getText("{SEP}", strip=True).split("{SEP}")
            title = info_[0]
            eps, aired = info_[-3:-1]
            try:
                score = float(info[2].getText(strip=True))
            except ValueError:
                score = float("NaN")

            if csv_file:
                csv_writer.writerow([rank, title, eps, aired, score])
            else:
                print()
                print(rank, title, score)
                print('\t', eps)
                print('\t', aired)

            if rank == top_n:
                break

        if rank % 50 == 0:
            url = base_url + "limit=" + str(rank)

    if csv_file:
        csv_file_.close()

YES = ['y', 'yes']

if __name__ == "__main__":
    top_n = int(input("How many animes would you like to list? "))
    airing = input("Would you like to list airing animes? [Y/n] ")
    airing = True if airing.lower() in YES else False
    csv_file = input("Would you like to write in CSV file? [Y/n] ")
    if csv_file.lower() in YES:
        csv_file = "MAL_Top_{}_Animes.csv".format(top_n)
    else:
        csv_file = False
    mal_top(top_n, airing, csv_file)
