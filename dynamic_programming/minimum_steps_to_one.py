"""
YouTube Açıklaması: https://www.youtube.com/watch?v=f2xi3c1S95M

Verilen bir tamsayı n için, n'den 1'e minimum adım sayısını döndürün

MEVCUT ADIMLAR:
    * 1 azalt
    * n 2'ye bölünebiliyorsa, 2'ye böl
    * n 3'e bölünebiliyorsa, 3'e böl


Örnek 1: n = 10
10 -> 9 -> 3 -> 1
Sonuç: 3 adım

Örnek 2: n = 15
15 -> 5 -> 4 -> 2 -> 1
Sonuç: 4 adım

Örnek 3: n = 6
6 -> 2 -> 1
Sonuç: 2 adım
"""

from __future__ import annotations

__author__ = "Alexander Joslin"


def bire_min_adim_sayisi(sayi: int) -> int:
    """
    Tablo kullanarak 1'e minimum adım sayısı.
    >>> bire_min_adim_sayisi(10)
    3
    >>> bire_min_adim_sayisi(15)
    4
    >>> bire_min_adim_sayisi(6)
    2

    :param sayi:
    :return int:
    """

    if sayi <= 0:
        msg = f"n 0'dan büyük olmalıdır. Verilen n = {sayi}"
        raise ValueError(msg)

    tablo = [sayi + 1] * (sayi + 1)

    # başlangıç pozisyonu
    tablo[1] = 0
    for i in range(1, sayi):
        tablo[i + 1] = min(tablo[i + 1], tablo[i] + 1)
        # sınırları kontrol et
        if i * 2 <= sayi:
            tablo[i * 2] = min(tablo[i * 2], tablo[i] + 1)
        # sınırları kontrol et
        if i * 3 <= sayi:
            tablo[i * 3] = min(tablo[i * 3], tablo[i] + 1)
    return tablo[sayi]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
