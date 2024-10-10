# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm

#Organiser: K. Umut Araz


def binary_and(a: int, b: int) -> str:
    """
    İki tam sayı alır, bunları ikili sisteme çevirir,
    sağlanan tam sayılar üzerinde ikili ve işlemi sonucunda
    bir ikili sayı döner.

    >>> binary_and(25, 32)
    '0b000000'
    >>> binary_and(37, 50)
    '0b100000'
    >>> binary_and(21, 30)
    '0b10100'
    >>> binary_and(58, 73)
    '0b0001000'
    >>> binary_and(0, 255)
    '0b00000000'
    >>> binary_and(256, 256)
    '0b100000000'
    >>> binary_and(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: her iki girdinin değeri pozitif olmalıdır
    >>> binary_and(0, 1.1)
    Traceback (most recent call last):
        ...
    ValueError: float türündeki nesne için 'b' format kodu bilinmiyor
    >>> binary_and("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: 'str' ve 'int' örnekleri arasında '<' desteklenmiyor
    """
    if a < 0 or b < 0:
        raise ValueError("her iki girdinin değeri pozitif olmalıdır")

    a_binary = format(a, "b")
    b_binary = format(b, "b")

    max_len = max(len(a_binary), len(b_binary))

    return "0b" + "".join(
        str(int(char_a == "1" and char_b == "1"))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
