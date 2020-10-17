"""
Project 7: https://projecteuler.net/problem=7

By listing the first six prime numbers:

    2, 3, 5, 7, 11, and 13

We can see that the 6th prime is 13. What is the Nth prime number?
"""
import itertools
import math


def prime_check(number: int) -> bool:
    """Determines whether a given number is prime or not"""
    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))


def prime_generator():
    num = 2
    while True:
        if prime_check(num):
            yield num
        num += 1


def solution(nth: int = 10001) -> int:
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
    >>> solution()
    104743
    """
    return next(itertools.islice(prime_generator(), nth - 1, nth))


if __name__ == "__main__":
    print(solution(int(input().strip())))
