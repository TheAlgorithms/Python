"""
Pandigital prime
Problem 41: https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?

All pandigital numbers except for 1, 4 ,7 pandigital numbers are divisible by 3.
So we will check only 7 digit pandigital numbers to obtain the largest possible
pandigital prime.
"""
from __future__ import annotations

from itertools import permutations

from maths.prime_check import prime_check


def solution(n: int = 7) -> int:
    """
    Returns the maximum pandigital prime number of length n.
    If there are none, then it will return 0.
    >>> solution(2)
    0
    >>> solution(4)
    4231
    >>> solution(7)
    7652413
    """
    pandigital_str = "".join(str(i) for i in range(1, n + 1))
    perm_list = [int("".join(i)) for i in permutations(pandigital_str, n)]
    pandigitals = [num for num in perm_list if prime_check(num)]
    return max(pandigitals) if pandigitals else 0


if __name__ == "__main__":
    print(f"{solution() = }")
