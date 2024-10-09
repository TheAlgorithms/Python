import math
import sys


def bir_sayiyi_temsil_eden_minimum_kareler(sayi: int) -> int:
    """
    Bir sayıyı temsil eden minimum kare sayısını say
    >>> bir_sayiyi_temsil_eden_minimum_kareler(25)
    1
    >>> bir_sayiyi_temsil_eden_minimum_kareler(37)
    2
    >>> bir_sayiyi_temsil_eden_minimum_kareler(21)
    3
    >>> bir_sayiyi_temsil_eden_minimum_kareler(58)
    2
    >>> bir_sayiyi_temsil_eden_minimum_kareler(-1)
    Traceback (most recent call last):
        ...
    ValueError: giriş değeri negatif bir sayı olmamalıdır
    >>> bir_sayiyi_temsil_eden_minimum_kareler(0)
    1
    >>> bir_sayiyi_temsil_eden_minimum_kareler(12.34)
    Traceback (most recent call last):
        ...
    ValueError: giriş değeri doğal bir sayı olmalıdır
    """
    if sayi != int(sayi):
        raise ValueError("giriş değeri doğal bir sayı olmalıdır")
    if sayi < 0:
        raise ValueError("giriş değeri negatif bir sayı olmamalıdır")
    if sayi == 0:
        return 1
    cevaplar = [-1] * (sayi + 1)
    cevaplar[0] = 0
    for i in range(1, sayi + 1):
        cevap = sys.maxsize
        kok = int(math.sqrt(i))
        for j in range(1, kok + 1):
            mevcut_cevap = 1 + cevaplar[i - (j**2)]
            cevap = min(cevap, mevcut_cevap)
        cevaplar[i] = cevap
    return cevaplar[sayi]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
