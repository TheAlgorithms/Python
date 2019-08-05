# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers:

    2, 3, 5, 7, 11, and 13

We can see that the 6th prime is 13. What is the Nth prime number?
"""
from __future__ import print_function
import math
import itertools

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3


def primeCheck(number):
    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))


def prime_generator():
    num = 2
    while True:
        if primeCheck(num):
            yield num
        num += 1


def solution(n):
    """Returns the n-th prime number.
 
    >>> solution(6)
    13
    >>> solution(1)
    2
    >>> solution(3)
    5
    >>> solution(20)
    71
    >>> solution(50)
    229
    >>> solution(100)
    541
    """
    return next(itertools.islice(prime_generator(), n - 1, n))


if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
