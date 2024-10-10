# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def ikili_veya(a: int, b: int) -> str:
    """

    Organiser: K. Umut Araz

    İki tam sayı alır, bunları ikili sisteme çevirir ve sağlanan tam sayılar üzerinde
    ikili veya işlemi sonucunda bir ikili sayı döner.

    >>> ikili_veya(25, 32)
    '0b111001'
    >>> ikili_veya(37, 50)
    '0b110111'
    >>> ikili_veya(21, 30)
    '0b11111'
    >>> ikili_veya(58, 73)
    '0b1111011'
    >>> ikili_veya(0, 255)
    '0b11111111'
    >>> ikili_veya(0, 256)
    '0b100000000'
    >>> ikili_veya(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: Her iki girdinin değeri pozitif olmalıdır
    >>> ikili_veya(0, 1.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' türündeki nesne 'int' olarak yorumlanamaz
    >>> ikili_veya("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: 'str' ve 'int' örnekleri arasında '<' desteklenmiyor
    """
    if a < 0 or b < 0:
        raise ValueError("Her iki girdinin değeri pozitif olmalıdır")
    a_ikili = str(bin(a))[2:]  # baştaki "0b"yi kaldır
    b_ikili = str(bin(b))[2:]
    max_uzunluk = max(len(a_ikili), len(b_ikili))
    return "0b" + "".join(
        str(int("1" in (char_a, char_b)))
        for char_a, char_b in zip(a_ikili.zfill(max_uzunluk), b_ikili.zfill(max_uzunluk))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
