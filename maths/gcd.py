"""Greatest Common Divisor using Euclidean algorithm."""


def gcd(a: int, b: int) -> int:
    """
    Find GCD of two numbers.

    >>> gcd(12, 8)
    4
    >>> gcd(54, 24)
    6
    """
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()
