"""Fast exponentiation using binary exponentiation."""


def power(base: int, exp: int) -> int:
    """
    Calculate base^exp using binary exponentiation.

    >>> power(2, 10)
    1024
    >>> power(3, 5)
    243
    """
    if exp < 0:
        return 1 / power(base, -exp)
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
