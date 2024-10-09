def binary_count_setbits(a: int) -> int:
    """
    Bir tam sayı alır, bu sayının ikili gösterimindeki
    1'lerin sayısını döner.

    >>> binary_count_setbits(25)
    3
    >>> binary_count_setbits(36)
    2
    >>> binary_count_setbits(16)
    1
    >>> binary_count_setbits(58)
    4
    >>> binary_count_setbits(4294967295)
    32
    >>> binary_count_setbits(0)
    0
    >>> binary_count_setbits(-10)
    Traceback (most recent call last):
        ...
    ValueError: Girdi değeri pozitif bir tam sayı olmalıdır
    >>> binary_count_setbits(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Girdi değeri 'int' türünde olmalıdır
    >>> binary_count_setbits("0")
    Traceback (most recent call last):
        ...
    TypeError: '<' 'str' ve 'int' örnekleri arasında desteklenmiyor
    """
    if a < 0:
        raise ValueError("Girdi değeri pozitif bir tam sayı olmalıdır")
    elif isinstance(a, float):
        raise TypeError("Girdi değeri 'int' türünde olmalıdır")
    return bin(a).count("1")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
