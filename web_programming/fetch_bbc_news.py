# Created by sarathkaul on 12/11/19

import requests

_NEWS_API = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="


def fetch_bbc_news(bbc_news_api_key: str) -> list[dict]:
    """
    BBC News API anahtarı kullanarak en son haber makalelerini getirir.

    Args:
        bbc_news_api_key (str): BBC News API anahtarı

    Returns:
        list[dict]: Haber makalelerinin listesi
    """
    try:
        # Haber makalelerini json formatında getir
        response = requests.get(_NEWS_API + bbc_news_api_key, timeout=10)
        response.raise_for_status()
        bbc_news_page = response.json()
    except requests.RequestException as e:
        print(f"Veri alınırken hata oluştu: {e}")
        return []

    return bbc_news_page.get("articles", [])


if __name__ == "__main__":
    api_key = input("BBC News API anahtarınızı girin: ").strip()
    articles = fetch_bbc_news(bbc_news_api_key=api_key)
    if articles:
        for i, article in enumerate(articles, 1):
            print(f"{i}.) {article['title']}")
    else:
        print("Haber makalesi bulunamadı.")
