"""
Yazar  : Mehdi ALAOUI

Bu, verilen bir dizinin en uzun artan alt dizisi için Dinamik Programlama çözümünün
saf Python uygulamasıdır.

Problem  :
Bir dizi verildiğinde, bu dizideki en uzun ve artan alt diziyi bulmak ve
geri döndürmek.
Örnek: Girdi olarak [10, 22, 9, 33, 21, 50, 41, 60, 80] verildiğinde
       çıktı olarak [10, 22, 33, 41, 60, 80] döner
"""

from __future__ import annotations


def en_uzun_alt_dizi(dizi: list[int]) -> list[int]:  # Bu fonksiyon özyinelemelidir
    """
    Bazı örnekler
    >>> en_uzun_alt_dizi([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [10, 22, 33, 41, 60, 80]
    >>> en_uzun_alt_dizi([4, 8, 7, 5, 1, 12, 2, 3, 9])
    [1, 2, 3, 9]
    >>> en_uzun_alt_dizi([9, 8, 7, 6, 5, 7])
    [8]
    >>> en_uzun_alt_dizi([1, 1, 1])
    [1, 1, 1]
    >>> en_uzun_alt_dizi([])
    []
    """
    dizi_uzunlugu = len(dizi)
    # Eğer dizi sadece bir eleman içeriyorsa, onu döndürürüz (bu özyinelemenin durma koşuludur)
    if dizi_uzunlugu <= 1:
        return dizi
    # Aksi takdirde
    pivot = dizi[0]
    bulundu = False
    i = 1
    en_uzun_alt_dizi: list[int] = []
    while not bulundu and i < dizi_uzunlugu:
        if dizi[i] < pivot:
            bulundu = True
            gecici_dizi = [eleman for eleman in dizi[i:] if eleman >= dizi[i]]
            gecici_dizi = en_uzun_alt_dizi(gecici_dizi)
            if len(gecici_dizi) > len(en_uzun_alt_dizi):
                en_uzun_alt_dizi = gecici_dizi
        else:
            i += 1

    gecici_dizi = [eleman for eleman in dizi[1:] if eleman >= pivot]
    gecici_dizi = [pivot, *en_uzun_alt_dizi(gecici_dizi)]
    if len(gecici_dizi) > len(en_uzun_alt_dizi):
        return gecici_dizi
    else:
        return en_uzun_alt_dizi


if __name__ == "__main__":
    import doctest

    doctest.testmod()
