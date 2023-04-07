"""
Project Euler Problem 10: https://projecteuler.net/problem=10

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""

import math
import time
start_time = time.time()

def solution(n: int = 2000000) -> int:
    """
    Returns the sum of all the primes below n.

    >>> solution(1000)
    76127
    >>> solution(5000)
    1548136
    >>> solution(10000)
    5736396
    >>> solution(7)
    10
    """

    if n < 2:
        return 0

    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return sum(i for i in range(2, n) if primes[i])



if __name__ == "__main__":
    print(f"{solution() = }")
print("Process finished --- %s seconds ---" % (time.time() - start_time))
