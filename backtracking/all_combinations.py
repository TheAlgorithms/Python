"""
Bu problemde, 1'den n'ye kadar olan sayılardan k sayısının tüm olası kombinasyonlarını belirlemek istiyoruz.
Bu problemi çözmek için geri izleme (backtracking) kullanıyoruz.

"""
#Organiser: K. Umut Araz



from __future__ import annotations

from itertools import combinations


def kombinasyon_listeleri(n: int, k: int) -> list[list[int]]:
    """
    >>> kombinasyon_listeleri(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    return [list(x) for x in combinations(range(1, n + 1), k)]


def tüm_kombinasyonları_oluştur(n: int, k: int) -> list[list[int]]:
    """
    >>> tüm_kombinasyonları_oluştur(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    >>> tüm_kombinasyonları_oluştur(n=0, k=0)
    [[]]
    >>> tüm_kombinasyonları_oluştur(n=10, k=-1)
    Traceback (most recent call last):
        ...
    ValueError: k negatif olmamalı
    >>> tüm_kombinasyonları_oluştur(n=-1, k=10)
    Traceback (most recent call last):
        ...
    ValueError: n negatif olmamalı
    >>> tüm_kombinasyonları_oluştur(n=5, k=4)
    [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]
    >>> from itertools import combinations
    >>> all(tüm_kombinasyonları_oluştur(n, k) == kombinasyon_listeleri(n, k)
    ...     for n in range(1, 6) for k in range(1, 6))
    True
    """
    if k < 0:
        raise ValueError("k negatif olmamalı")
    if n < 0:
        raise ValueError("n negatif olmamalı")

    sonuç: list[list[int]] = []
    tüm_durumları_oluştur(1, n, k, [], sonuç)
    return sonuç


def tüm_durumları_oluştur(
    artış: int,
    toplam_sayı: int,
    seviye: int,
    mevcut_liste: list[int],
    toplam_liste: list[list[int]],
) -> None:
    if seviye == 0:
        toplam_liste.append(mevcut_liste[:])
        return

    for i in range(artış, toplam_sayı - seviye + 2):
        mevcut_liste.append(i)
        tüm_durumları_oluştur(i + 1, toplam_sayı, seviye - 1, mevcut_liste, toplam_liste)
        mevcut_liste.pop()


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(tüm_kombinasyonları_oluştur(n=4, k=2))
    testler = ((n, k) for n in range(1, 5) for k in range(1, 5))
    for n, k in testler:
        print(n, k, tüm_kombinasyonları_oluştur(n, k) == kombinasyon_listeleri(n, k))

    print("Benchmark:")
    from timeit import timeit

    for func in ("kombinasyon_listeleri", "tüm_kombinasyonları_oluştur"):
        print(f"{func:>25}(): {timeit(f'{func}(n=4, k = 2)', globals=globals())}")
