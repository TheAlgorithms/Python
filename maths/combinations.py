from math import factorial


def combinations(n, k):
    """
    >>> combinations(10,5)
    252
    >>> combinations(6,3)
    20
    >>> combinations(20,5)
    15504
    """
    return int(factorial(n) / ((factorial(k)) * (factorial(n - k))))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
