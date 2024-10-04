import sys
import webbrowser

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def google_ara(query: str) -> None:
    """
    Google'da arama yapar ve ilk 5 sonucu tarayıcıda açar.
    @parametreler: query, arama yapılacak sorgu
    """
    print("Googling.....")
    url = f"https://www.google.com/search?q={query}"
    try:
        res = requests.get(url, headers={"User-Agent": UserAgent().random}, timeout=10)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"Veri alınırken hata oluştu: {e}")
        return

    with open("project1a.html", "wb") as out_file:  # sadece sınıfı bilmek için
        for data in res.iter_content(10000):
            out_file.write(data)

    soup = BeautifulSoup(res.text, "html.parser")
    links = list(soup.select(".eZt8xd"))[:5]

    print(f"Bulunan link sayısı: {len(links)}")
    for link in links:
        href = link.get("href")
        if link.text == "Maps":
            webbrowser.open(href)
        else:
            webbrowser.open(f"https://google.com{href}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        google_ara(query)
    else:
        print("Lütfen arama yapmak için bir sorgu girin.")
