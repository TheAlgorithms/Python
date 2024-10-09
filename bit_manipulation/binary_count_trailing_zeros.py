from math import log2


def binary_count_trailing_zeros(a: int) -> int:
    """
    Bir tam sayı alır, bu sayının ikili gösterimindeki
    sondaki sıfırların sayısını döner.

    >>> binary_count_trailing_zeros(25)
    0
    >>> binary_count_trailing_zeros(36)
    2
    >>> binary_count_trailing_zeros(16)
    4
    >>> binary_count_trailing_zeros(58)
    1
    >>> binary_count_trailing_zeros(4294967296)
    32
    >>> binary_count_trailing_zeros(0)
    0
    >>> binary_count_trailing_zeros(-10)
    Traceback (most recent call last):
        ...
    ValueError: Girdi değeri pozitif bir tam sayı olmalıdır
    >>> binary_count_trailing_zeros(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Girdi değeri 'int' türünde olmalıdır
    >>> binary_count_trailing_zeros("0")
    Traceback (most recent call last):
        ...
    TypeError: '<' 'str' ve 'int' örnekleri arasında desteklenmiyor
    """
    if a < 0:
        raise ValueError("Girdi değeri pozitif bir tam sayı olmalıdır")
    elif isinstance(a, float):
        raise TypeError("Girdi değeri 'int' türünde olmalıdır")
    return 0 if (a == 0) else int(log2(a & -a))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
