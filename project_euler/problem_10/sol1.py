"""
Problem Statement:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from __future__ import print_function
from math import sqrt

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3

try:
    xrange  # Python 2
except NameError:
    xrange = range  # Python 3


def is_prime(n):
    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def sum_of_primes(n):
    if n > 2:
        sumOfPrimes = 2
    else:
        return 0

    for i in xrange(3, n, 2):
        if is_prime(i):
            sumOfPrimes += i

    return sumOfPrimes


def solution(n):
    """Returns the sum of all the primes below n.
    
    >>> solution(2000000)
    142913828922
    >>> solution(1000)
    76127
    >>> solution(5000)
    1548136
    >>> solution(10000)
    5736396
    >>> solution(7)
    10
    """
    return sum_of_primes(n)


if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
