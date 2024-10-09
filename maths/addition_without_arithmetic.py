"""
Aritmetik işlemler kullanmadan tam sayıların nasıl toplandığını gösterir
Yazar: Suraj Kumar
Organised by K. Umut Araz
Zaman Karmaşıklığı: 1
https://en.wikipedia.org/wiki/Bitwise_operation
"""


def topla(birinci: int, ikinci: int) -> int:
    """
    Tam sayıların toplama işleminin uygulanması

    Örnekler:
    >>> topla(3, 5)
    8
    >>> topla(13, 5)
    18
    >>> topla(-7, 2)
    -5
    >>> topla(0, -7)
    -7
    >>> topla(-321, 0)
    -321
    """
    while ikinci != 0:
        c = birinci & ikinci
        birinci ^= ikinci
        ikinci = c << 1
    return birinci


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    birinci = int(input("Birinci sayıyı girin: ").strip())
    ikinci = int(input("İkinci sayıyı girin: ").strip())
    print(f"{topla(birinci, ikinci) = }")
