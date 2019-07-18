# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers:

    2, 3, 5, 7, 11, and 13

We can see that the 6th prime is 13. What is the Nth prime number?
"""
from __future__ import print_function

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3


def isprime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


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
    primes = []
    num = 2
    while len(primes) < n:
        if isprime(num):
            primes.append(num)
            num += 1
        else:
            num += 1
    return primes[len(primes) - 1]


if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
