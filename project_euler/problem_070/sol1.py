"""
Project Euler Problem 70: https://projecteuler.net/problem=70

Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, so
φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and
the ratio n/φ(n) produces a minimum.

-----

This is essentially brute force. Calculate all totients up to 10^7 and
find the minimum ratio of n/φ(n) that way. To minimize the ratio, we want
to minimize n and maximize φ(n) as much as possible, so we can store the
minimum fraction's numerator and denominator and calculate new fractions
with each totient to compare against. To avoid dividing by zero, I opt to
use cross multiplication.

References:
Finding totients
https://en.wikipedia.org/wiki/Euler's_totient_function#Euler's_product_formula
"""
from __future__ import annotations

import numpy as np


def get_totients(max_one: int) -> list[int]:
    """
    Calculates a list of totients from 0 to max_one exclusive, using the
    definition of Euler's product formula.

    >>> get_totients(5)
    [0, 1, 1, 2, 2]

    >>> get_totients(10)
    [0, 1, 1, 2, 2, 4, 2, 6, 4, 6]
    """
    totients = np.arange(max_one)

    for i in range(2, max_one):
        if totients[i] == i:
            x = np.arange(i, max_one, i)  # array of indexes to select
            totients[x] -= totients[x] // i

    return totients.tolist()


def has_same_digits(num1: int, num2: int) -> bool:
    """
    Return True if num1 and num2 have the same frequency of every digit, False
    otherwise.

    >>> has_same_digits(123456789, 987654321)
    True

    >>> has_same_digits(123, 23)
    False

    >>> has_same_digits(1234566, 123456)
    False
    """
    return sorted(str(num1)) == sorted(str(num2))


def solution(max_n: int = 10000000) -> int:
    """
    Finds the value of n from 1 to max such that n/φ(n) produces a minimum.

    >>> solution(100)
    21

    >>> solution(10000)
    4435
    """

    min_numerator = 1  # i
    min_denominator = 0  # φ(i)
    totients = get_totients(max_n + 1)

    for i in range(2, max_n + 1):
        t = totients[i]

        if i * min_denominator < min_numerator * t and has_same_digits(i, t):
            min_numerator = i
            min_denominator = t

    return min_numerator


if __name__ == "__main__":
    print(f"{solution() = }")
