def snake_to_camel_case(girdi_str: str, pascal_kullan: bool = False) -> str:
    """

    Organiser: K. Umut Araz

    
    Verilen bir snake_case dizesini camelCase (veya belirtilirse PascalCase) formatına dönüştürür.
    (Varsayılan olarak Pascal kullanılmaz)

    >>> snake_to_camel_case("baz_random_dize")
    'bazRandomDize'

    >>> snake_to_camel_case("baz_random_dize", pascal_kullan=True)
    'BazRandomDize'

    >>> snake_to_camel_case("baz_random_dize_ile_sayilar_123")
    'bazRandomDizeIleSayilar123'

    >>> snake_to_camel_case("baz_random_dize_ile_sayilar_123", pascal_kullan=True)
    'BazRandomDizeIleSayilar123'

    >>> snake_to_camel_case(123)
    Traceback (most recent call last):
        ...
    ValueError: Girdi olarak string bekleniyor, bulunan <class 'int'>

    >>> snake_to_camel_case("baz_dize", pascal_kullan="True")
    Traceback (most recent call last):
        ...
    ValueError: pascal_kullan parametresi için boolean bekleniyor, bulunan <class 'str'>
    """

    if not isinstance(girdi_str, str):
        msg = f"Girdi olarak string bekleniyor, bulunan {type(girdi_str)}"
        raise ValueError(msg)
    if not isinstance(pascal_kullan, bool):
        msg = f"pascal_kullan parametresi için boolean bekleniyor, bulunan {type(pascal_kullan)}"
        raise ValueError(msg)

    kelimeler = girdi_str.split("_")

    baslangic_indeksi = 0 if pascal_kullan else 1

    buyuk_harfle_baslayacak_kelimeler = kelimeler[baslangic_indeksi:]

    buyuk_harfli_kelimeler = [kelime[0].upper() + kelime[1:] for kelime in buyuk_harfle_baslayacak_kelimeler]

    ilk_kelime = "" if pascal_kullan else kelimeler[0]

    return "".join([ilk_kelime, *buyuk_harfli_kelimeler])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
