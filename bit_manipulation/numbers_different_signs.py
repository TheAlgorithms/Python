"""
Yazar  : Alexander Pantyukhin
Tarih  : 30 Kasım 2022

Görev:
İki tamsayı verildiğinde. Bu sayıların zıt işaretlere sahip olup olmadığını True,
aksi takdirde False döndürün.

Uygulama notları: Bit manipülasyonu kullanın.
İki sayı için XOR kullanın.
"""


def zıt_işaretli_mi(sayi1: int, sayi2: int) -> bool:
    """
    Sayıların zıt işaretlere sahip olup olmadığını True, aksi takdirde False döndürür.

    >>> zıt_işaretli_mi(1, -1)
    True
    >>> zıt_işaretli_mi(1, 1)
    False
    >>> zıt_işaretli_mi(1000000000000000000000000000, -1000000000000000000000000000)
    True
    >>> zıt_işaretli_mi(-1000000000000000000000000000, 1000000000000000000000000000)
    True
    >>> zıt_işaretli_mi(50, 278)
    False
    >>> zıt_işaretli_mi(0, 2)
    False
    >>> zıt_işaretli_mi(2, 0)
    False
    """
    return sayi1 ^ sayi2 < 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
