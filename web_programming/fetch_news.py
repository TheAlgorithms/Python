# Created by sarathkaul on 12/11/19

import requests

_NEWS_API = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"


def fetch_bbc_news():
    # fetching data in json format
    bbc_page_fetch = requests.get(_NEWS_API).json()

    # getting all articles in a string article
    article = bbc_page_fetch["articles"]

    # result containing all trending news
    results = []

    for a_article in article:
        results.append(a_article)

    for a_result in range(len(results)):
        # printing all trending news
        print(str(a_result + 1) + ".) ", results[a_result]['title'])


if __name__ == '__main__':
    fetch_bbc_news()
