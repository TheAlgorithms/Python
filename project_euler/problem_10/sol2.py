"""
Problem Statement:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math
from itertools import takewhile


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
    """Returns the sum of all the primes below n.

    # The code below has been commented due to slow execution affecting Travis.
    # >>> solution(2000000)
    # 142913828922
    >>> solution(1000)
    76127
    >>> solution(5000)
    1548136
    >>> solution(10000)
    5736396
    >>> solution(7)
    10
    """
    return sum(takewhile(lambda x: x < n, prime_generator()))


if __name__ == "__main__":
    print(solution(int(input().strip())))
