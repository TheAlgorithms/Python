"""
Problem:
The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor
of a given number N?

e.g. for 10, largest prime factor = 5. For 17, largest prime factor = 17.
"""
from __future__ import print_function, division
import math

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3


def solution(n):
    """Returns the largest prime factor of a given number n.
    
    >>> solution(13195)
    29
    >>> solution(10)
    5
    >>> solution(17)
    17
    """
    prime = 1
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime = i
            n //= i
        i += 1
    if n > 1:
        prime = n
    return int(prime)


if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
