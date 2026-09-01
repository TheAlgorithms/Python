"""Least Common Multiple using GCD."""


def lcm(a: int, b: int) -> int:
    """
    Find LCM of two numbers.

    >>> lcm(4, 6)
    12
    >>> lcm(3, 7)
    21
    """
    from math import gcd
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
