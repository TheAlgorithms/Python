"""
Bu problemde, verilen dizinin tüm olası alt dizilerini belirlemek istiyoruz.
Bu problemi çözmek için geri izleme (backtracking) kullanıyoruz.

Organiser: K. Umut Araz

Zaman karmaşıklığı: O(2^n),
burada n, verilen dizinin uzunluğunu belirtir.
"""

from __future__ import annotations

from typing import Any


def tüm_alt_dizileri_oluştur(dizi: list[Any]) -> None:
    durum_uzayı_ağacı_oluştur(dizi, [], 0)


def durum_uzayı_ağacı_oluştur(
    dizi: list[Any], mevcut_alt_dizi: list[Any], indeks: int
) -> None:
    """
    Her dalı DFS kullanarak yinelemek için bir durum uzayı ağacı oluşturur.
    Her durumun tam olarak iki çocuğu olduğunu biliyoruz.
    Verilen dizinin sonuna ulaştığında sona erer.

    :param dizi: Alt dizilerin oluşturulduğu giriş dizisi.
    :param mevcut_alt_dizi: Oluşturulan mevcut alt dizi.
    :param indeks: Dizideki mevcut indeks.

    Örnek:
    >>> dizi = [3, 2, 1]
    >>> mevcut_alt_dizi = []
    >>> durum_uzayı_ağacı_oluştur(dizi, mevcut_alt_dizi, 0)
    []
    [1]
    [2]
    [2, 1]
    [3]
    [3, 1]
    [3, 2]
    [3, 2, 1]

    >>> dizi = ["A", "B"]
    >>> mevcut_alt_dizi = []
    >>> durum_uzayı_ağacı_oluştur(dizi, mevcut_alt_dizi, 0)
    []
    ['B']
    ['A']
    ['A', 'B']

    >>> dizi = []
    >>> mevcut_alt_dizi = []
    >>> durum_uzayı_ağacı_oluştur(dizi, mevcut_alt_dizi, 0)
    []

    >>> dizi = [1, 2, 3, 4]
    >>> mevcut_alt_dizi = []
    >>> durum_uzayı_ağacı_oluştur(dizi, mevcut_alt_dizi, 0)
    []
    [4]
    [3]
    [3, 4]
    [2]
    [2, 4]
    [2, 3]
    [2, 3, 4]
    [1]
    [1, 4]
    [1, 3]
    [1, 3, 4]
    [1, 2]
    [1, 2, 4]
    [1, 2, 3]
    [1, 2, 3, 4]
    """

    if indeks == len(dizi):
        print(mevcut_alt_dizi)
        return

    durum_uzayı_ağacı_oluştur(dizi, mevcut_alt_dizi, indeks + 1)
    mevcut_alt_dizi.append(dizi[indeks])
    durum_uzayı_ağacı_oluştur(dizi, mevcut_alt_dizi, indeks + 1)
    mevcut_alt_dizi.pop()


if __name__ == "__main__":
    dizi: list[Any] = [1, 2, 3]
    tüm_alt_dizileri_oluştur(dizi)

    dizi.clear()
    dizi.extend(["A", "B", "C"])
    tüm_alt_dizileri_oluştur(dizi)
