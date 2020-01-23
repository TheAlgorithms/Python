"""
A simple terminal program to find news about a certain topic by web scraping site.
site used:
1. Times of India,
   link : https://timesofindia.indiatimes.com/india/
2. India's Today,
   link : https://www.indiatoday.in/topic/
"""

import time
import webbrowser
import requests
from bs4 import BeautifulSoup

BOLD_START = "\033[1m"
BOLD_END = "\033[0m"


def times_of_india(userInput, ua):
    url = "https://timesofindia.indiatimes.com/india/" + userInput

    res = requests.post(url, headers=ua)
    soup = BeautifulSoup(res.content, "html.parser")
    data = soup.find_all(class_="w_tle")

    if not data:
        return 0

   print("News available :", "\N{slightly smiling face}")
    for i, article in enumerate(data):
        print(BOLD_START, "\033[1;32;40m \nNEWS : ", i + 1, BOLD_END, end="  ")
        data1 = article.find("a")
        print(BOLD_START, data1.get_text(), BOLD_END)

        bol = input("For more details ->(y) (y/n) :: ".strip().lower())
        if bol == "y":
            url += data1.get("href")
            print("%s" % url)
            webbrowser.open(url)
    return len(data)


def india_today(userInput, ua):
    url = "https://www.indiatoday.in/topic/" + userInput

    res = requests.get(url, headers=ua)
    soup = BeautifulSoup(res.content, "html.parser")
    data = soup.find_all(class_="field-content")

    if len(data) > 0:
        print("\nNews available : ", "\N{slightly smiling face}")
    k = 0
    for i in range(len(data)):
        data1 = data[i].find_all("a")
        for j in range(len(data1)):
            print(BOLD_START, "\033[1;32;40m\nNEWS ", k + 1, BOLD_END, end=" : ")
            k += 1
            print(BOLD_START, data1[j].get_text(), BOLD_END)
            bol = input("\nFor more details ->(y) (y/n) :: ")
            if bol == "y" or bol == "Y":
                data2 = data[i].find("a")
                url = data2.get("href")
                webbrowser.open(url)

    return len(data)


if __name__ == "__main__":
    print("\033[5;31;40m")
    print(
        BOLD_START,
        "                 HERE YOU WILL GET ALL THE NEWS JUST IN ONE SEARCH                   ",
        BOLD_END,
    )
    print("\n")
    localtime = time.asctime(time.localtime(time.time()))
    print(BOLD_START, localtime, BOLD_END)

    ua = {
        "UserAgent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"
    }
    print(
        BOLD_START,
        "\n\033[1;35;40m Search any news (state , city ,Country , AnyThings etc) : ",
        BOLD_END,
        end=" ",
    )

    userInput = input()

    print(BOLD_START, "\033[1;33;40m \n")
    print("Which news channel data would you prefer")
    print("1. Times of India")
    print("2. India's Today", BOLD_END)

    say = int(input())

    if say == 1:
        length = times_of_india(userInput, ua)
        if length == 0:
            print("Sorry Here No News Available", "\N{expressionless face}")
            print("\n")
            print(
                "Would you like to go for India's Today (y/n):: ",
                "\N{thinking face}",
                end="  ",
            )
            speak = input().strip().lower()
            if speak == "y":
                length = india_today(userInput, ua)
                if length == 0:
                    print("Sorry No news", "\N{expressionless face}")
                else:
                    print("\nThank you", "\U0001f600")
            else:
                print("\nThank you", "\U0001f600")
    elif say == 2:
        length = india_today(userInput, ua)

        if length == 0:
            print("Sorry No news")
        else:
            print("\nThank you", "\U0001f600")
    else:
        print("Sorry", "\N{expressionless face}")
