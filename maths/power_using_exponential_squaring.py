def power_using_exponential_squaring(base: int, exponent: int) -> int:
    """Returns the result of base^exponent
    https://en.wikipedia.org/wiki/Exponentiation_by_squaring

    >>> power_using_exponential_squaring(3, 3)
    27
    >>> power_using_exponential_squaring(2, 0)
    1
    >>> power_using_exponential_squaring(2, 10)
    1024
    >>> power_using_exponential_squaring(10, 6)
    1000000
    """

    assert base >= 1

    result = 1
    while exponent > 0:
        if exponent & 1:
            result *= base

        base *= base
        exponent >>= 1

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
