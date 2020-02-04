# Created by sarathkaul on 12/11/19

import requests

_NEWS_API = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="


def fetch_bbc_news(bbc_news_api_key: str) -> None:
    # fetching a list of articles in json format
    bbc_news_page = requests.get(_NEWS_API + bbc_news_api_key).json()
    print (bbc_news_page)
    # each article in the list is a dict
    # for i, article in enumerate(bbc_news_page["articles"], 1):
    #     print(f"{i}.) {article['title']}")


if __name__ == "__main__":
    fetch_bbc_news(bbc_news_api_key="4dbc17e007ab436fb66416009dfb59a8")
