import sys


def minimum_alt_dizi_toplami(hedef: int, sayilar: list[int]) -> int:
    """
    Bir sayı listesindeki toplamı en az hedef olan en kısa ardışık alt dizinin uzunluğunu döndürür.
    Referans: https://stackoverflow.com/questions/8269916

    >>> minimum_alt_dizi_toplami(7, [2, 3, 1, 2, 4, 3])
    2
    >>> minimum_alt_dizi_toplami(7, [2, 3, -1, 2, 4, -3])
    4
    >>> minimum_alt_dizi_toplami(11, [1, 1, 1, 1, 1, 1, 1, 1])
    0
    >>> minimum_alt_dizi_toplami(10, [1, 2, 3, 4, 5, 6, 7])
    2
    >>> minimum_alt_dizi_toplami(5, [1, 1, 1, 1, 1, 5])
    1
    >>> minimum_alt_dizi_toplami(0, [])
    0
    >>> minimum_alt_dizi_toplami(0, [1, 2, 3])
    1
    >>> minimum_alt_dizi_toplami(10, [10, 20, 30])
    1
    >>> minimum_alt_dizi_toplami(7, [1, 1, 1, 1, 1, 1, 10])
    1
    >>> minimum_alt_dizi_toplami(6, [])
    0
    >>> minimum_alt_dizi_toplami(2, [1, 2, 3])
    1
    >>> minimum_alt_dizi_toplami(-6, [])
    0
    >>> minimum_alt_dizi_toplami(-6, [3, 4, 5])
    1
    >>> minimum_alt_dizi_toplami(8, None)
    0
    >>> minimum_alt_dizi_toplami(2, "ABC")
    Traceback (most recent call last):
        ...
    ValueError: sayilar bir tamsayılar dizisi olmalıdır
    """
    if not isinstance(sayilar, (list, tuple)) or not all(
        isinstance(sayi, int) for sayi in sayilar
    ):
        raise ValueError("sayilar bir tamsayılar dizisi olmalıdır")

    if not sayilar:
        return 0

    sol = sag = mevcut_toplam = 0
    min_uzunluk = sys.maxsize

    while sag < len(sayilar):
        mevcut_toplam += sayilar[sag]
        while mevcut_toplam >= hedef and sol <= sag:
            min_uzunluk = min(min_uzunluk, sag - sol + 1)
            mevcut_toplam -= sayilar[sol]
            sol += 1
        sag += 1

    return 0 if min_uzunluk == sys.maxsize else min_uzunluk
