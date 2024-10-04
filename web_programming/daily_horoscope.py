import requests
from bs4 import BeautifulSoup

# Burç yorumu almak için fonksiyon
def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Veri alınırken hata oluştu: {e}"
    
    soup = BeautifulSoup(response.content, "html.parser")
    horoscope_div = soup.find("div", class_="main-horoscope")
    if horoscope_div and horoscope_div.p:
        return horoscope_div.p.text
    return "Burç yorumu bulunamadı."

if __name__ == "__main__":
    print("Günlük Burç Yorumu. \n")
    print(
        "Burç numaranızı girin:\n",
        "1. Koç\n",
        "2. Boğa\n",
        "3. İkizler\n",
        "4. Yengeç\n",
        "5. Aslan\n",
        "6. Başak\n",
        "7. Terazi\n",
        "8. Akrep\n",
        "9. Yay\n",
        "10. Oğlak\n",
        "11. Kova\n",
        "12. Balık\n",
    )
    try:
        zodiac_sign = int(input("Numara> ").strip())
        if zodiac_sign < 1 or zodiac_sign > 12:
            raise ValueError("Geçersiz burç numarası.")
    except ValueError as e:
        print(f"Hata: {e}")
        exit(1)
    
    print("Bir gün seçin:\n", "dün\n", "bugün\n", "yarın\n")
    day = input("Günü girin> ").strip().lower()
    if day not in ["dün", "bugün", "yarın"]:
        print("Geçersiz gün seçimi.")
        exit(1)
    
    horoscope_text = horoscope(zodiac_sign, day)
    print(horoscope_text)
