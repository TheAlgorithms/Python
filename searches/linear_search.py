"""
Bu, doğrusal arama algoritmasının saf Python ile uygulanışıdır.

Doküman testleri için aşağıdaki komutu çalıştırın:
python3 -m doctest -v linear_search.py

Organiser: K. Umut Araz

Manuel test için çalıştırın:
python3 linear_search.py
"""


def linear_search(dizi: list, hedef: int) -> int:
    """Doğrusal arama algoritmasının saf Python ile uygulanışı

    :param dizi: Karşılaştırılabilir öğeler içeren bir koleksiyon (Doğrusal Arama için sıralı öğeler gerekli değildir)
    :param hedef: Aranacak öğe değeri
    :return: Bulunan öğenin indeksi veya öğe bulunamazsa -1

    Örnekler:
    >>> linear_search([0, 5, 7, 10, 15], 0)
    0
    >>> linear_search([0, 5, 7, 10, 15], 15)
    4
    >>> linear_search([0, 5, 7, 10, 15], 5)
    1
    >>> linear_search([0, 5, 7, 10, 15], 6)
    -1
    """
    for indeks, ogret in enumerate(dizi):
        if ogret == hedef:
            return indeks
    return -1


def rec_linear_search(dizi: list, alt: int, ust: int, hedef: int) -> int:
    """
    Doğrusal arama algoritmasının saf Python ile rekürsif uygulanışı

    :param dizi: Karşılaştırılabilir öğeler içeren bir koleksiyon (Doğrusal Arama için sıralı öğeler gerekli değildir)
    :param alt: Dizinin alt sınırı
    :param ust: Dizinin üst sınırı
    :param hedef: Bulunması gereken öğe
    :return: Anahtarın indeksi veya anahtar bulunamazsa -1

    Örnekler:
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 0)
    0
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 700)
    4
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 30)
    1
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, -6)
    -1
    """
    if not (0 <= ust < len(dizi) and 0 <= alt < len(dizi)):
        raise Exception("Geçersiz üst veya alt sınır!")
    if ust < alt:
        return -1
    if dizi[alt] == hedef:
        return alt
    if dizi[ust] == hedef:
        return ust
    return rec_linear_search(dizi, alt + 1, ust - 1, hedef)


if __name__ == "__main__":
    kullanici_girdisi = input("Virgülle ayrılmış sayıları girin:\n").strip()
    dizi = [int(ogret.strip()) for ogret in kullanici_girdisi.split(",")]

    hedef = int(input("Listede bulunması gereken tek bir sayıyı girin:\n").strip())
    sonuc = linear_search(dizi, hedef)
    if sonuc != -1:
        print(f"linear_search({dizi}, {hedef}) = {sonuc}")
    else:
        print(f"{hedef} {dizi} içinde bulunamadı.")
