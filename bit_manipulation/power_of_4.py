"""
Organiser: K. Umut Araz

Görev:
Pozitif bir tamsayı verildiğinde, bu sayının 4'ün kuvveti olup olmadığını
True veya False olarak döndürün.

Uygulama notları: Bit manipülasyonu kullanın.
Örneğin, sayı 2'nin kuvveti ise bit gösterimi:
n     = 0..100..00
n - 1 = 0..011..11

n & (n - 1) - kesişim yok = 0
Eğer sayı 4'ün kuvveti ise, 2'nin kuvveti olmalı ve ayarlanmış bit tek bir pozisyonda olmalıdır.
"""


def dordun_ussu_mu(sayi: int) -> bool:
    """
    Bu sayının 4'ün kuvveti olup olmadığını True veya False olarak döndürür.

    >>> dordun_ussu_mu(0)
    Traceback (most recent call last):
        ...
    ValueError: sayı pozitif olmalıdır
    >>> dordun_ussu_mu(1)
    True
    >>> dordun_ussu_mu(2)
    False
    >>> dordun_ussu_mu(4)
    True
    >>> dordun_ussu_mu(6)
    False
    >>> dordun_ussu_mu(8)
    False
    >>> dordun_ussu_mu(17)
    False
    >>> dordun_ussu_mu(64)
    True
    >>> dordun_ussu_mu(-1)
    Traceback (most recent call last):
        ...
    ValueError: sayı pozitif olmalıdır
    >>> dordun_ussu_mu(1.2)
    Traceback (most recent call last):
        ...
    TypeError: sayı bir tamsayı olmalıdır

    """
    if not isinstance(sayi, int):
        raise TypeError("sayı bir tamsayı olmalıdır")
    if sayi <= 0:
        raise ValueError("sayı pozitif olmalıdır")
    if sayi & (sayi - 1) == 0:
        c = 0
        while sayi:
            c += 1
            sayi >>= 1
        return c % 2 == 1
    else:
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
