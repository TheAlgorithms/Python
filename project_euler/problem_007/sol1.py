"""
Project Euler Problem 7: https://projecteuler.net/problem=7

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""

from math import sqrt


def is_prime(num: int) -> bool:
    """
    Determines whether the given number is prime or not

    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(29)
    True
    >>> is_prime(0)
    False
    """

    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        sq = int(sqrt(num)) + 1
        for i in range(3, sq, 2):
            if num % i == 0:
                return False
    return True


def solution(nth: int = 10001) -> int:
    """
    Returns the n-th prime number.

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

    count = 0
    number = 1
    while count != nth and number < 3:
        number += 1
        if is_prime(number):
            count += 1
    while count != nth:
        number += 2
        if is_prime(number):
            count += 1
    return number


if __name__ == "__main__":
    print(f"{solution() = }")
