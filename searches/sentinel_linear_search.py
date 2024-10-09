"""
Bu, bekçi doğrusal arama algoritmasının saf Python ile uygulanışıdır.

Doküman testleri için aşağıdaki komutu çalıştırın:
python -m doctest -v sentinel_linear_search.py
veya
python3 -m doctest -v sentinel_linear_search.py

Organiser: K. Umut Araz

Manuel test için çalıştırın:
python sentinel_linear_search.py
"""


def bekçi_doğrusal_arama(dizi, hedef):
    """Bekçi doğrusal arama algoritmasının saf Python ile uygulanışı

    :param dizi: Karşılaştırılabilir öğeler içeren bir dizi
    :param hedef: Aranacak öğe değeri
    :return: Bulunan öğenin indeksi veya öğe bulunamazsa None

    Örnekler:
    >>> bekçi_doğrusal_arama([0, 5, 7, 10, 15], 0)
    0

    >>> bekçi_doğrusal_arama([0, 5, 7, 10, 15], 15)
    4

    >>> bekçi_doğrusal_arama([0, 5, 7, 10, 15], 5)
    1

    >>> bekçi_doğrusal_arama([0, 5, 7, 10, 15], 6)

    """
    dizi.append(hedef)

    indeks = 0
    while dizi[indeks] != hedef:
        indeks += 1

    dizi.pop()

    if indeks == len(dizi):
        return None

    return indeks


if __name__ == "__main__":
    kullanici_girdisi = input("Virgülle ayrılmış sayıları girin:\n").strip()
    dizi = [int(eleman) for eleman in kullanici_girdisi.split(",")]

    hedef_girdi = input("Listede bulunması gereken tek bir sayıyı girin:\n")
    hedef = int(hedef_girdi)
    sonuc = bekçi_doğrusal_arama(dizi, hedef)
    if sonuc is not None:
        print(f"{hedef} şu konumda bulundu: {sonuc}")
    else:
        print("Bulunamadı")
