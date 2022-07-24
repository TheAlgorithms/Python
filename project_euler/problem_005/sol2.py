"""
Project Euler Problem 5: https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is _evenly divisible_ by all
of the numbers from 1 to 20?

References:
    - https://en.wiktionary.org/wiki/evenly_divisible
    - https://en.wikipedia.org/wiki/Euclidean_algorithm
    - https://en.wikipedia.org/wiki/Least_common_multiple
"""


def greatest_common_divisor(x: int, y: int) -> int:
    """
    Euclidean Greatest Common Divisor algorithm

    >>> greatest_common_divisor(0, 0)
    0
    >>> greatest_common_divisor(23, 42)
    1
    >>> greatest_common_divisor(15, 33)
    3
    >>> greatest_common_divisor(12345, 67890)
    15
    """

    return x if y == 0 else greatest_common_divisor(y, x % y)


def lcm(x: int, y: int) -> int:
    """
    Least Common Multiple.

    Using the property that lcm(a, b) * greatest_common_divisor(a, b) = a*b

    >>> lcm(3, 15)
    15
    >>> lcm(1, 27)
    27
    >>> lcm(13, 27)
    351
    >>> lcm(64, 48)
    192
    """

    return (x * y) // greatest_common_divisor(x, y)


def solution(n: int = 20) -> int:
    """
    Returns the smallest positive number that is evenly divisible (divisible
    with no remainder) by all of the numbers from 1 to n.

    >>> solution(10)
    2520
    >>> solution(15)
    360360
    >>> solution(22)
    232792560
    """

    g = 1
    for i in range(1, n + 1):
        g = lcm(g, i)
    return g


if __name__ == "__main__":
    print(f"{solution() = }")
