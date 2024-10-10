"""Ondalık (Decimal) Değerleri Hexadecimal Temsillere Dönüştür"""
# Organiser: K. Umut Araz
# Her hexadecimal basamağı için ondalık değerleri ayarla
değerler = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}


def ondalik_to_hexadecimal(ondalik: float) -> str:
    """
    Tam sayı ondalık değeri alır, 0x ile başlayan hexadecimal temsili döner
    >>> ondalik_to_hexadecimal(5)
    '0x5'
    >>> ondalik_to_hexadecimal(15)
    '0xf'
    >>> ondalik_to_hexadecimal(37)
    '0x25'
    >>> ondalik_to_hexadecimal(255)
    '0xff'
    >>> ondalik_to_hexadecimal(4096)
    '0x1000'
    >>> ondalik_to_hexadecimal(999098)
    '0xf3eba'
    >>> # negatif sayılar da çalışır
    >>> ondalik_to_hexadecimal(-256)
    '-0x100'
    >>> # float değerler, tam sayıya eşit olduğunda kabul edilir
    >>> ondalik_to_hexadecimal(17.0)
    '0x11'
    >>> # diğer float değerler hata verir
    >>> ondalik_to_hexadecimal(16.16) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    AssertionError
    >>> # string değerler de hata verir
    >>> ondalik_to_hexadecimal('0xfffff') # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    AssertionError
    >>> # sonuçlar, Python'un varsayılan hex fonksiyonu ile karşılaştırıldığında aynıdır
    >>> ondalik_to_hexadecimal(-256) == hex(-256)
    True
    """
    assert isinstance(ondalik, (int, float))
    assert ondalik == int(ondalik)
    ondalik = int(ondalik)
    hexadecimal = ""
    negatif = False
    if ondalik < 0:
        negatif = True
        ondalik *= -1
    while ondalik > 0:
        ondalik, kalan = divmod(ondalik, 16)
        hexadecimal = değerler[kalan] + hexadecimal
    hexadecimal = "0x" + hexadecimal
    if negatif:
        hexadecimal = "-" + hexadecimal
    return hexadecimal


if __name__ == "__main__":
    import doctest

    doctest.testmod()
