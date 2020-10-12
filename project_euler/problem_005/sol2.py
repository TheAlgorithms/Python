"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is _evenly divisible_ by all
of the numbers from 1 to 20?

References:
    - The Project Euler problem page:
    https://projecteuler.net/problem=5
    - Definition of 'evenly divisible':
    https://en.wiktionary.org/wiki/evenly_divisible
    - Wikipedia page for the Euklidean algorithm for the GCD:
    https://en.wikipedia.org/wiki/Euclidean_algorithm
    - Wikipedia page for the Least common Multiple (LCM):
    https://en.wikipedia.org/wiki/Least_common_multiple
"""


def gcd(x: int, y: int) -> int:
    """
    Euclidean GCD algorithm (Greatest Common Divisor)

    >>> gcd(0, 0)
    0
    >>> gcd(23, 42)
    1
    >>> gcd(15, 33)
    3
    >>> gcd(12345, 67890)
    15
    """

    return x if y == 0 else gcd(y, x % y)


def lcm(x: int, y: int) -> int:
    """
    Least Common Multiple.

    Using the property that lcm(a, b) * gcd(a, b) = a*b

    >>> lcm(3, 15)
    15
    >>> lcm(1, 27)
    27
    >>> lcm(13, 27)
    351
    >>> lcm(64, 48)
    192
    """

    return (x * y) // gcd(x, y)


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
    print(solution(int(input().strip())))
