"""
Project Euler Problem 5: https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is _evenly divisible_ by all
of the numbers from 1 to 20?

References:
    - https://en.wiktionary.org/wiki/evenly_divisible
"""


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
    >>> solution(3.4)
    6
    >>> solution(0)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater than or equal to one.
    >>> solution(-17)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater than or equal to one.
    >>> solution([])
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or castable to int.
    >>> solution("asd")
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or castable to int.
    """

    try:
        n = int(n)
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or castable to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater than or equal to one.")
    i = 0
    while 1:
        i += n * (n - 1)
        nfound = 0
        for j in range(2, n):
            if i % j != 0:
                nfound = 1
                break
        if nfound == 0:
            if i == 0:
                i = 1
            return i
    return None


if __name__ == "__main__":
    print(f"{solution() = }")
