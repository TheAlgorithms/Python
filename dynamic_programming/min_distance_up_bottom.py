"""
Yazar   : Alexander Pantyukhin
Tarih   : 14 Ekim 2022
Bu, düzenleme mesafesini bulmak için yukarıdan aşağıya yaklaşımın bir uygulamasıdır.
Uygulama Leetcode'da test edildi: https://leetcode.com/problems/edit-distance/

Levinstein mesafesi
Dinamik Programlama: yukarı -> aşağı.
"""

import functools


def min_distance_up_bottom(kelime1: str, kelime2: str) -> int:
    """
    >>> min_distance_up_bottom("intention", "execution")
    5
    >>> min_distance_up_bottom("intention", "")
    9
    >>> min_distance_up_bottom("", "")
    0
    >>> min_distance_up_bottom("zooicoarchaeologist", "zoologist")
    10
    """
    len_kelime1 = len(kelime1)
    len_kelime2 = len(kelime2)

    @functools.cache
    def min_distance(indeks1: int, indeks2: int) -> int:
        # ilk kelime indeksi taşarsa - ikinci kelimeden hepsini sil
        if indeks1 >= len_kelime1:
            return len_kelime2 - indeks2
        # ikinci kelime indeksi taşarsa - ilk kelimeden hepsini sil
        if indeks2 >= len_kelime2:
            return len_kelime1 - indeks1
        fark = int(kelime1[indeks1] != kelime2[indeks2])  # mevcut harfler aynı değil
        return min(
            1 + min_distance(indeks1 + 1, indeks2),
            1 + min_distance(indeks1, indeks2 + 1),
            fark + min_distance(indeks1 + 1, indeks2 + 1),
        )

    return min_distance(0, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
