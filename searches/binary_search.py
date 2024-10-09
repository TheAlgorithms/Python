#!/usr/bin/env python3

"""
Saf Python uygulamaları için ikili arama algoritmalarının saf Python uygulamaları

Doküman testleri için aşağıdaki komutu çalıştırın:
python3 -m doctest -v binary_search.py

Manuel test için çalıştırın:
python3 binary_search.py

#Organiser: K. Umut Araz
"""

from __future__ import annotations

import bisect


def bisect_sol(
    sirali_koleksiyon: list[int], eleman: int, lo: int = 0, hi: int = -1
) -> int:
    """
    Verilen bir değerden büyük veya eşit olan ilk elemanı bulur.

    Aynı arayüze sahiptir
    https://docs.python.org/3/library/bisect.html#bisect.bisect_left .

    :param sirali_koleksiyon: karşılaştırılabilir öğelere sahip bazı artan sıralı koleksiyon
    :param eleman: bisect edilecek öğe
    :param lo: dikkate alınacak en düşük indeks (sirali_koleksiyon[lo:hi] gibi)
    :param hi: dikkate alınacak en yüksek indeksin ötesi (sirali_koleksiyon[lo:hi] gibi)
    :return: sirali_koleksiyon[lo:i] içindeki tüm değerlerin < eleman olduğu ve
        sirali_koleksiyon[i:hi] içindeki tüm değerlerin >= eleman olduğu i indeksi.

    Örnekler:
    >>> bisect_sol([0, 5, 7, 10, 15], 0)
    0
    >>> bisect_sol([0, 5, 7, 10, 15], 6)
    2
    >>> bisect_sol([0, 5, 7, 10, 15], 20)
    5
    >>> bisect_sol([0, 5, 7, 10, 15], 15, 1, 3)
    3
    >>> bisect_sol([0, 5, 7, 10, 15], 6, 2)
    2
    """
    if hi < 0:
        hi = len(sirali_koleksiyon)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if sirali_koleksiyon[mid] < eleman:
            lo = mid + 1
        else:
            hi = mid

    return lo


def bisect_sag(
    sirali_koleksiyon: list[int], eleman: int, lo: int = 0, hi: int = -1
) -> int:
    """
    Verilen bir değerden büyük olan ilk elemanı bulur.

    Aynı arayüze sahiptir
    https://docs.python.org/3/library/bisect.html#bisect.bisect_right .

    :param sirali_koleksiyon: karşılaştırılabilir öğelere sahip bazı artan sıralı koleksiyon
    :param eleman: bisect edilecek öğe
    :param lo: dikkate alınacak en düşük indeks (sirali_koleksiyon[lo:hi] gibi)
    :param hi: dikkate alınacak en yüksek indeksin ötesi (sirali_koleksiyon[lo:hi] gibi)
    :return: sirali_koleksiyon[lo:i] içindeki tüm değerlerin <= eleman olduğu ve
        sirali_koleksiyon[i:hi] içindeki tüm değerlerin > eleman olduğu i indeksi.

    Örnekler:
    >>> bisect_sag([0, 5, 7, 10, 15], 0)
    1
    >>> bisect_sag([0, 5, 7, 10, 15], 15)
    5
    >>> bisect_sag([0, 5, 7, 10, 15], 6)
    2
    >>> bisect_sag([0, 5, 7, 10, 15], 15, 1, 3)
    3
    >>> bisect_sag([0, 5, 7, 10, 15], 6, 2)
    2
    """
    if hi < 0:
        hi = len(sirali_koleksiyon)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if sirali_koleksiyon[mid] <= eleman:
            lo = mid + 1
        else:
            hi = mid

    return lo


def ekle_sol(
    sirali_koleksiyon: list[int], eleman: int, lo: int = 0, hi: int = -1
) -> None:
    """
    Verilen bir değeri, aynı değere sahip diğer değerlerden önce sıralı bir diziye ekler.

    Aynı arayüze sahiptir
    https://docs.python.org/3/library/bisect.html#bisect.insort_left .

    :param sirali_koleksiyon: karşılaştırılabilir öğelere sahip bazı artan sıralı koleksiyon
    :param eleman: eklenecek öğe
    :param lo: dikkate alınacak en düşük indeks (sirali_koleksiyon[lo:hi] gibi)
    :param hi: dikkate alınacak en yüksek indeksin ötesi (sirali_koleksiyon[lo:hi] gibi)

    Örnekler:
    >>> sirali_koleksiyon = [0, 5, 7, 10, 15]
    >>> ekle_sol(sirali_koleksiyon, 6)
    >>> sirali_koleksiyon
    [0, 5, 6, 7, 10, 15]
    >>> sirali_koleksiyon = [(0, 0), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> eleman = (5, 5)
    >>> ekle_sol(sirali_koleksiyon, eleman)
    >>> sirali_koleksiyon
    [(0, 0), (5, 5), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> eleman is sirali_koleksiyon[1]
    True
    >>> eleman is sirali_koleksiyon[2]
    False
    >>> sirali_koleksiyon = [0, 5, 7, 10, 15]
    >>> ekle_sol(sirali_koleksiyon, 20)
    >>> sirali_koleksiyon
    [0, 5, 7, 10, 15, 20]
    >>> sirali_koleksiyon = [0, 5, 7, 10, 15]
    >>> ekle_sol(sirali_koleksiyon, 15, 1, 3)
    >>> sirali_koleksiyon
    [0, 5, 7, 15, 10, 15]
    """
    sirali_koleksiyon.insert(bisect_sol(sirali_koleksiyon, eleman, lo, hi), eleman)


def ekle_sag(
    sirali_koleksiyon: list[int], eleman: int, lo: int = 0, hi: int = -1
) -> None:
    """
    Verilen bir değeri, aynı değere sahip diğer değerlerden sonra sıralı bir diziye ekler.

    Aynı arayüze sahiptir
    https://docs.python.org/3/library/bisect.html#bisect.insort_right .

    :param sirali_koleksiyon: karşılaştırılabilir öğelere sahip bazı artan sıralı koleksiyon
    :param eleman: eklenecek öğe
    :param lo: dikkate alınacak en düşük indeks (sirali_koleksiyon[lo:hi] gibi)
    :param hi: dikkate alınacak en yüksek indeksin ötesi (sirali_koleksiyon[lo:hi] gibi)

    Örnekler:
    >>> sirali_koleksiyon = [0, 5, 7, 10, 15]
    >>> ekle_sag(sirali_koleksiyon, 6)
    >>> sirali_koleksiyon
    [0, 5, 6, 7, 10, 15]
    >>> sirali_koleksiyon = [(0, 0), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> eleman = (5, 5)
    >>> ekle_sag(sirali_koleksiyon, eleman)
    >>> sirali_koleksiyon
    [(0, 0), (5, 5), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> eleman is sirali_koleksiyon[1]
    False
    >>> eleman is sirali_koleksiyon[2]
    True
    >>> sirali_koleksiyon = [0, 5, 7, 10, 15]
    >>> ekle_sag(sirali_koleksiyon, 20)
    >>> sirali_koleksiyon
    [0, 5, 7, 10, 15, 20]
    >>> sirali_koleksiyon = [0, 5, 7, 10, 15]
    >>> ekle_sag(sirali_koleksiyon, 15, 1, 3)
    >>> sirali_koleksiyon
    [0, 5, 7, 15, 10, 15]
    """
    sirali_koleksiyon.insert(bisect_sag(sirali_koleksiyon, eleman, lo, hi), eleman)


def ikili_arama(sirali_koleksiyon: list[int], eleman: int) -> int:
    """Python'da saf bir ikili arama algoritmasının saf uygulaması

    Dikkat edin, koleksiyon artan sıralı olmalıdır, aksi takdirde sonuç
    öngörülemez olacaktır.

    :param sirali_koleksiyon: karşılaştırılabilir öğelere sahip bazı artan sıralı koleksiyon
    :param eleman: aranacak öğe değeri
    :return: bulunan öğenin indeksi veya öğe bulunamazsa -1

    Örnekler:
    >>> ikili_arama([0, 5, 7, 10, 15], 0)
    0
    >>> ikili_arama([0, 5, 7, 10, 15], 15)
    4
    >>> ikili_arama([0, 5, 7, 10, 15], 5)
    1
    >>> ikili_arama([0, 5, 7, 10, 15], 6)
    -1
    """
    if list(sirali_koleksiyon) != sorted(sirali_koleksiyon):
        raise ValueError("sirali_koleksiyon artan sırada olmalıdır")
    sol = 0
    sag = len(sirali_koleksiyon) - 1

    while sol <= sag:
        orta = sol + (sag - sol) // 2
        mevcut_eleman = sirali_koleksiyon[orta]
        if mevcut_eleman == eleman:
            return orta
        elif eleman < mevcut_eleman:
            sag = orta - 1
        else:
            sol = orta + 1
    return -1


def ikili_arama_std_lib(sirali_koleksiyon: list[int], eleman: int) -> int:
    """Python'da stdlib kullanarak saf bir ikili arama algoritmasının saf uygulaması

    Dikkat edin, koleksiyon artan sıralı olmalıdır, aksi takdirde sonuç
    öngörülemez olacaktır.

    :param sirali_koleksiyon: karşılaştırılabilir öğelere sahip bazı artan sıralı koleksiyon
    :param eleman: aranacak öğe değeri
    :return: bulunan öğenin indeksi veya öğe bulunamazsa -1

    Örnekler:
    >>> ikili_arama_std_lib([0, 5, 7, 10, 15], 0)
    0
    >>> ikili_arama_std_lib([0, 5, 7, 10, 15], 15)
    4
    >>> ikili_arama_std_lib([0, 5, 7, 10, 15], 5)
    1
    >>> ikili_arama_std_lib([0, 5, 7, 10, 15], 6)
    -1
    """
    if list(sirali_koleksiyon) != sorted(sirali_koleksiyon):
        raise ValueError("sirali_koleksiyon artan sırada olmalıdır")
    indeks = bisect.bisect_sol(sirali_koleksiyon, eleman)
    if indeks != len(sirali_koleksiyon) and sirali_koleksiyon[indeks] == eleman:
        return indeks
    return -1


def ikili_arama_ile_rekursion(
    sirali_koleksiyon: list[int], eleman: int, sol: int = 0, sag: int = -1
) -> int:
    """Python'da saf bir ikili arama algoritmasının saf uygulaması, rekursif olarak

    Dikkat edin, koleksiyon artan sıralı olmalıdır, aksi takdirde sonuç
    öngörülemez olacaktır.
    İlk rekursiyon sol=0 ve sag=(len(sirali_koleksiyon)-1) ile başlatılmalıdır.

    :param sirali_koleksiyon: karşılaştırılabilir öğelere sahip bazı artan sıralı koleksiyon
    :param eleman: aranacak öğe değeri
    :return: bulunan öğenin indeksi veya öğe bulunamazsa -1

    Örnekler:
    >>> ikili_arama_ile_rekursion([0, 5, 7, 10, 15], 0, 0, 4)
    0
    >>> ikili_arama_ile_rekursion([0, 5, 7, 10, 15], 15, 0, 4)
    4
    >>> ikili_arama_ile_rekursion([0, 5, 7, 10, 15], 5, 0, 4)
    1
    >>> ikili_arama_ile_rekursion([0, 5, 7, 10, 15], 6, 0, 4)
    -1
    """
    if sag < 0:
        sag = len(sirali_koleksiyon) - 1
    if list(sirali_koleksiyon) != sorted(sirali_koleksiyon):
        raise ValueError("sirali_koleksiyon artan sırada olmalıdır")
    if sag < sol:
        return -1

    orta = sol + (sag - sol) // 2

    if sirali_koleksiyon[orta] == eleman:
        return orta
    elif sirali_koleksiyon[orta] > eleman:
        return ikili_arama_ile_rekursion(sirali_koleksiyon, eleman, sol, orta - 1)
    else:
        return ikili_arama_ile_rekursion(sirali_koleksiyon, eleman, orta + 1, sag)


def üssel_arama(sirali_koleksiyon: list[int], eleman: int) -> int:
    """Python'da saf bir üssel arama algoritmasının saf uygulaması
    Kullanılan kaynaklar:
    https://en.wikipedia.org/wiki/Exponential_search

    Dikkat edin, koleksiyon artan sıralı olmalıdır, aksi takdirde sonuç
    öngörülemez olacaktır.

    :param sirali_koleksiyon: karşılaştırılabilir öğelere sahip bazı artan sıralı koleksiyon
    :param eleman: aranacak öğe değeri
    :return: bulunan öğenin indeksi veya öğe bulunamazsa -1

    Bu algoritmanın karmaşıklığı O(lg I) dir, burada I, öğenin mevcut olduğu indeks konumudur.

    Örnekler:
    >>> üssel_arama([0, 5, 7, 10, 15], 0)
    0
    >>> üssel_arama([0, 5, 7, 10, 15], 15)
    4
    >>> üssel_arama([0, 5, 7, 10, 15], 5)
    1
    >>> üssel_arama([0, 5, 7, 10, 15], 6)
    -1
    """
    if list(sirali_koleksiyon) != sorted(sirali_koleksiyon):
        raise ValueError("sirali_koleksiyon artan sırada olmalıdır")
    sınır = 1
    while sınır < len(sirali_koleksiyon) and sirali_koleksiyon[sınır] < eleman:
        sınır *= 2
    sol = sınır // 2
    sag = min(sınır, len(sirali_koleksiyon) - 1)
    son_sonuc = ikili_arama_ile_rekursion(
        sirali_koleksiyon=sirali_koleksiyon, eleman=eleman, sol=sol, sag=sag
    )
    if son_sonuc is None:
        return -1
    return son_sonuc


arama_yöntemleri = (  # En hızlıdan en yavaşa...
    ikili_arama_std_lib,
    ikili_arama,
    üssel_arama,
    ikili_arama_ile_rekursion,
)


if __name__ == "__main__":
    import doctest
    import timeit

    doctest.testmod()
    for arama in arama_yöntemleri:
        isim = f"{arama.__name__:>26}"
        print(f"{isim}: {arama([0, 5, 7, 10, 15], 10) = }")  # type: ignore[operator]

    print("\nPerformans Testleri...")
    ayar = "koleksiyon = range(1000)"
    for arama in arama_yöntemleri:
        isim = arama.__name__
        print(
            f"{isim:>26}:",
            timeit.timeit(
                f"{isim}(koleksiyon, 500)", setup=ayar, number=5_000, globals=globals()
            ),
        )

    kullanici_girdisi = input("\nVirgülle ayrılmış sayıları girin: ").strip()
    koleksiyon = sorted(int(eleman) for eleman in kullanici_girdisi.split(","))
    hedef = int(input("Listede bulunacak tek bir sayıyı girin: "))
    sonuc = ikili_arama(sirali_koleksiyon=koleksiyon, eleman=hedef)
    if sonuc == -1:
        print(f"{hedef} {koleksiyon} içinde bulunamadı.")
    else:
        print(f"{hedef} {koleksiyon} içinde {sonuc} konumunda bulundu.")
