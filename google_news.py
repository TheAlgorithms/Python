"""
a simple terminal program to find new about certain topic by web scraping site.
site used :
1. Times of India,
   link : https://timesofindia.indiatimes.com/india/
2. India's Today,
   link : https://www.indiatoday.in/topic/
"""

import requests
from bs4 import BeautifulSoup
import webbrowser
import time


def Times_of_India(userInput, ua):
    bold_start = "\033[1m"
    bold_end = "\033[0m"

    url = "https://timesofindia.indiatimes.com/india/"
    url += userInput

    res = requests.post(url, headers=ua)
    soup = BeautifulSoup(res.content, "html.parser")
    data = soup.find_all(class_="w_tle")

    if len(data) > 0:
        print("News avaliable :", "\N{slightly smiling face}")
    if len(data) == 0:
        return 0

    for item in range(len(data)):
        print(bold_start, "\033[1;32;40m \nNEWS : ", item + 1, bold_end, end="  ")
        data1 = data[item].find("a")
        print(bold_start, data1.get_text(), bold_end)

        bol = input("For more details ->(y) (y/n) :: ")
        if bol == "y":
            url += data1.get("href")
            print("%s" % url)

            webbrowser.open(url)

    return len(data)


def india_today(userInput, ua):
    bold_start = "\033[1m"
    bold_end = "\033[0m"

    url = "https://www.indiatoday.in/topic/"
    url += userInput

    res = requests.get(url, headers=ua)
    soup = BeautifulSoup(res.content, "html.parser")
    data = soup.find_all(class_="field-content")

    if len(data) > 0:
        print("\nNews avaliable : ", "\N{slightly smiling face}")
    k = 0
    for i in range(len(data)):
        data1 = data[i].find_all("a")
        for j in range(len(data1)):
            print(bold_start, "\033[1;32;40m\nNEWS ", k + 1, bold_end, end=" : ")
            k += 1
            print(bold_start, data1[j].get_text(), bold_end)
            bol = input("\nFor more details ->(y) (y/n) :: ")
            if bol == "y" or bol == "Y":
                data2 = data[i].find("a")
                url = data2.get("href")
                webbrowser.open(url)

    return len(data)


if __name__ == "__main__":

    bold_start = "\033[1m"
    bold_end = "\033[0m"
    print("\033[5;31;40m")
    print(
        bold_start,
        "                 HERE YOU WILL GET ALL THE NEWS JUST IN ONE SEARCH                   ",
        bold_end,
    )
    print("\n")
    localtime = time.asctime(time.localtime(time.time()))
    print(bold_start, localtime, bold_end)

    ua = {
        "UserAgent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"
    }
    print(
        bold_start,
        "\n\033[1;35;40m Search any news (state , city ,Country , AnyThings etc) : ",
        bold_end,
        end=" ",
    )

    userInput = input()

    print(bold_start, "\033[1;33;40m \n")
    print("Which news channel data would you prefer")
    print("1. Times of india")
    print("2. India's Today", bold_end)

    say = int(input())

    if say == 1:
        length = Times_of_India(userInput, ua)
        if length == 0:
            print("Sorry Here No News Available", "\N{expressionless face}")
            print("\n")
            print(
                "Would you like to go for India's Today (y/n):: ",
                "\N{thinking face}",
                end="  ",
            )
            speak = input()
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
