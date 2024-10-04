"""
Başlık ve yayın yılı ile derginin cilt ve sayfalarını kullanarak
Google Scholar'dan atıf sayısını alın.
"""

import requests
from bs4 import BeautifulSoup


def get_citation(base_url: str, params: dict) -> str:
    """
    Atıf sayısını döndürür.
    """
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Veri alınırken hata oluştu: {e}")
        return "Veri alınamadı"

    soup = BeautifulSoup(response.content, "html.parser")
    div = soup.find("div", attrs={"class": "gs_ri"})
    if not div:
        return "Atıf bulunamadı"
    
    anchors = div.find("div", attrs={"class": "gs_fl"}).find_all("a")
    if len(anchors) < 3:
        return "Atıf bilgisi eksik"
    
    return anchors[2].get_text()


if __name__ == "__main__":
    params = {
        "title": (
            "Precisely geometry controlled microsupercapacitors for ultrahigh areal "
            "capacitance, volumetric capacitance, and energy density"
        ),
        "journal": "Chem. Mater.",
        "volume": 30,
        "pages": "3979-3990",
        "year": 2018,
        "hl": "en",
    }
    print(get_citation("https://scholar.google.com/scholar_lookup", params=params))
