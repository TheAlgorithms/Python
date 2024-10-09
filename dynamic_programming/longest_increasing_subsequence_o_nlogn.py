#############################
# Yazar: Aravind Kashyap
# Dosya: lis.py
# yorumlar: Bu program, listedeki eleman sayısının N olduğu durumda
#           O(NLogN) zaman karmaşıklığında En Uzun Kesin Artan Alt Diziyi çıktılar
#############################
from __future__ import annotations


def tavan_indeksi(v, sol, sag, anahtar):
    while sag - sol > 1:
        orta = (sol + sag) // 2
        if v[orta] >= anahtar:
            sag = orta
        else:
            sol = orta
    return sag


def en_uzun_artan_alt_dizi_uzunlugu(v: list[int]) -> int:
    """
    >>> en_uzun_artan_alt_dizi_uzunlugu([2, 5, 3, 7, 11, 8, 10, 13, 6])
    6
    >>> en_uzun_artan_alt_dizi_uzunlugu([])
    0
    >>> en_uzun_artan_alt_dizi_uzunlugu([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13,
    ...                                     3, 11, 7, 15])
    6
    >>> en_uzun_artan_alt_dizi_uzunlugu([5, 4, 3, 2, 1])
    1
    """
    if len(v) == 0:
        return 0

    kuyruk = [0] * len(v)
    uzunluk = 1

    kuyruk[0] = v[0]

    for i in range(1, len(v)):
        if v[i] < kuyruk[0]:
            kuyruk[0] = v[i]
        elif v[i] > kuyruk[uzunluk - 1]:
            kuyruk[uzunluk] = v[i]
            uzunluk += 1
        else:
            kuyruk[tavan_indeksi(kuyruk, -1, uzunluk - 1, v[i])] = v[i]

    return uzunluk


if __name__ == "__main__":
    import doctest

    doctest.testmod()
