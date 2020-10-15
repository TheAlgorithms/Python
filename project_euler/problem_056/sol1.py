"""
Project Euler Problem 56: https://projecteuler.net/problem=56

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100,
what is the maximum digital sum?
"""


def solution(a: int = 100, b: int = 100) -> int:
    """
    Considering natural numbers of the form, a**b, where a, b < 100,
    what is the maximum digital sum?
    :param a:
    :param b:
    :return:
    >>> solution(10,10)
    45

    >>> solution(100,100)
    972

    >>> solution(100,200)
    1872
    """

    # RETURN the MAXIMUM from the list of SUMs of the list of INT converted from STR of
    # BASE raised to the POWER
    return max(
        [
            sum([int(x) for x in str(base ** power)])
            for base in range(a)
            for power in range(b)
        ]
    )


# Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
