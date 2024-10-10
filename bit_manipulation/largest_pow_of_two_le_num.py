"""
Yazar   : Naman Sharma
Tarih   : 2 Ekim 2023

Organiser: K. Umut Araz 

Görev:
Verilen bir sayıdan küçük veya ona eşit olan en büyük 2'nin kuvvetini bulun.

Uygulama notları: Bit manipülasyonu kullanın.
1'den başlarız ve ayarlanmış biti sola kaydırarak (res<<1)<=sayi olup olmadığını kontrol ederiz.
Her sol bit kaydırma bir 2'nin kuvvetini temsil eder. 

Örneğin:
sayi: 15
sonuc: 1   0b1
        2   0b10
        4   0b100
        8   0b1000
        16  0b10000 (Çıkış)
"""


def en_buyuk_iki_ussu(sayi: int) -> int:
    """
    Verilen bir sayıdan küçük veya ona eşit olan en büyük 2'nin kuvvetini döndürür.

    >>> en_buyuk_iki_ussu(0)
    0
    >>> en_buyuk_iki_ussu(1)
    1
    >>> en_buyuk_iki_ussu(-1)
    0
    >>> en_buyuk_iki_ussu(3)
    2
    >>> en_buyuk_iki_ussu(15)
    8
    >>> en_buyuk_iki_ussu(99)
    64
    >>> en_buyuk_iki_ussu(178)
    128
    >>> en_buyuk_iki_ussu(999999)
    524288
    >>> en_buyuk_iki_ussu(99.9)
    Traceback (most recent call last):
        ...
    TypeError: Girdi değeri 'int' türünde olmalıdır
    """
    if isinstance(sayi, float):
        raise TypeError("Girdi değeri 'int' türünde olmalıdır")
    if sayi <= 0:
        return 0
    sonuc = 1
    while (sonuc << 1) <= sayi:
        sonuc <<= 1
    return sonuc


if __name__ == "__main__":
    import doctest

    doctest.testmod()
