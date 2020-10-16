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
from math import sqrt


def is_prime(n: int) -> bool:
    """
    Returns True if n is prime,
    False otherwise.
    >>> is_prime(67483)
    False
    >>> is_prime(563)
    True
    >>> is_prime(87)
    False
    """
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True


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
    pandigitals = [num for num in perm_list if is_prime(num)]
    return max(pandigitals) if pandigitals else 0


if __name__ == "__main__":
    print(f"{solution() = }")
