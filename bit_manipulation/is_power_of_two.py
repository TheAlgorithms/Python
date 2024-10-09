"""
Yazar  : Alexander Pantyukhin
Tarih  : 1 Kasım 2022

Görev:
Pozitif bir tamsayı verildiğinde, bu sayının 2'nin kuvveti olup olmadığını
True veya False olarak döndürün.

Uygulama notları: Bit manipülasyonu kullanın.
Örneğin, sayı 2'nin kuvveti ise bit gösterimi:
n     = 0..100..00
n - 1 = 0..011..11

n & (n - 1) - kesişim yok = 0
"""


def iki_ussu_mu(sayi: int) -> bool:
    """
    Bu sayının 2'nin kuvveti olup olmadığını True veya False olarak döndürür.

    >>> iki_ussu_mu(0)
    False
    >>> iki_ussu_mu(1)
    True
    >>> iki_ussu_mu(2)
    True
    >>> iki_ussu_mu(4)
    True
    >>> iki_ussu_mu(6)
    False
    >>> iki_ussu_mu(8)
    True
    >>> iki_ussu_mu(17)
    False
    >>> iki_ussu_mu(-1)
    Traceback (most recent call last):
        ...
    ValueError: sayı negatif olmamalıdır
    >>> iki_ussu_mu(1.2)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for &: 'float' and 'float'

    # 0'dan 10,000'e kadar olan tüm 2'nin kuvvetlerini test edin
    >>> all(iki_ussu_mu(int(2 ** i)) for i in range(10000))
    True
    """
    if sayi < 0:
        raise ValueError("sayı negatif olmamalıdır")
    return sayi & (sayi - 1) == 0 and sayi != 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
