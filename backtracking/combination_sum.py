"""
Kombinasyon Toplamı probleminde, birbirinden farklı tamsayılardan oluşan bir liste verilir.
Hedef değere eşit olan tüm kombinasyonları bulmamız gerekiyor.
Bir elemanı birden fazla kullanabiliriz.

Zaman karmaşıklığı (Ortalama Durum): O(n!)

Organiser: K. Umut Araz

Kısıtlar:
1 <= adaylar.length <= 30
2 <= adaylar[i] <= 40
Adayların tüm elemanları birbirinden farklıdır.
1 <= hedef <= 40
"""


def geri_izleme(
    adaylar: list, yol: list, cevap: list, hedef: int, önceki_indeks: int
) -> None:
    """
    Olası kombinasyonları arayan özyinelemeli bir fonksiyon. Hedef değerden büyük bir
    mevcut kombinasyon değeri durumunda geri izler.

    Parametreler
    ----------
    önceki_indeks: Önceki aramadan son indeks
    hedef: Yol listesindeki tamsayıları toplayarak elde etmemiz gereken değer.
    cevap: Olası kombinasyonların listesi
    yol: Mevcut kombinasyon
    adaylar: Kullanabileceğimiz tamsayıların listesi.
    """
    if hedef == 0:
        cevap.append(yol.copy())
    else:
        for indeks in range(önceki_indeks, len(adaylar)):
            if hedef >= adaylar[indeks]:
                yol.append(adaylar[indeks])
                geri_izleme(adaylar, yol, cevap, hedef - adaylar[indeks], indeks)
                yol.pop(len(yol) - 1)


def kombinasyon_toplamı(adaylar: list, hedef: int) -> list:
    """
    >>> kombinasyon_toplamı([2, 3, 5], 8)
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    >>> kombinasyon_toplamı([2, 3, 6, 7], 7)
    [[2, 2, 3], [7]]
    >>> kombinasyon_toplamı([-8, 2.3, 0], 1)
    Traceback (most recent call last):
        ...
    RecursionError: maximum recursion depth exceeded
    """
    yol = []  # type: list[int]
    cevap = []  # type: list[int]
    geri_izleme(adaylar, yol, cevap, hedef, 0)
    return cevap


def ana() -> None:
    print(kombinasyon_toplamı([-8, 2.3, 0], 1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ana()
