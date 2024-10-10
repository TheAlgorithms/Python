# 2'nin tamamlayıcısı hakkında bilgi: https://en.wikipedia.org/wiki/Two%27s_complement


def ikinin_tamlayani(sayi: int) -> str:
    """

    Organiser: K. Umut Araz
        
    Negatif bir tamsayı 'sayi' alır.
    'sayi'nin ikinin tamamlayanı gösterimini döndürür.

    >>> ikinin_tamlayani(0)
    '0b0'
    >>> ikinin_tamlayani(-1)
    '0b11'
    >>> ikinin_tamlayani(-5)
    '0b1011'
    >>> ikinin_tamlayani(-17)
    '0b101111'
    >>> ikinin_tamlayani(-207)
    '0b100110001'
    >>> ikinin_tamlayani(1)
    Traceback (most recent call last):
        ...
    ValueError: giriş negatif bir tamsayı olmalıdır
    """
    if sayi > 0:
        raise ValueError("giriş negatif bir tamsayı olmalıdır")
    ikilik_sayi_uzunlugu = len(bin(sayi)[3:])
    ikinin_tamlayani_sayi = bin(abs(sayi) - (1 << ikilik_sayi_uzunlugu))[3:]
    ikinin_tamlayani_sayi = (
        (
            "1"
            + "0" * (ikilik_sayi_uzunlugu - len(ikinin_tamlayani_sayi))
            + ikinin_tamlayani_sayi
        )
        if sayi < 0
        else "0"
    )
    return "0b" + ikinin_tamlayani_sayi


if __name__ == "__main__":
    import doctest

    doctest.testmod()
