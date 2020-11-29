"""
Project Euler Problem 3: https://projecteuler.net/problem=3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

References:
    - https://en.wikipedia.org/wiki/Prime_number#Unique_factorization
"""
import math


def isprime(num: int) -> bool:
    """
    Returns boolean representing primality of given number num.

    >>> isprime(2)
    True
    >>> isprime(3)
    True
    >>> isprime(27)
    False
    >>> isprime(2999)
    True
    >>> isprime(0)
    Traceback (most recent call last):
        ...
    ValueError: Parameter num must be greater than or equal to two.
    >>> isprime(1)
    Traceback (most recent call last):
        ...
    ValueError: Parameter num must be greater than or equal to two.
    """

    if num <= 1:
        raise ValueError("Parameter num must be greater than or equal to two.")
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def solution(n: int = 600851475143) -> int:
    """
    Returns the largest prime factor of a given number n.

    >>> solution(13195)
    29
    >>> solution(10)
    5
    >>> solution(17)
    17
    >>> solution(3.4)
    3
    >>> solution(0)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater than or equal to one.
    >>> solution(-17)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater than or equal to one.
    >>> solution([])
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or castable to int.
    >>> solution("asd")
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or castable to int.
    """

    try:
        n = int(n)
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or castable to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater than or equal to one.")
    max_number = 0
    if isprime(n):
        return n
    while n % 2 == 0:
        n //= 2
    if isprime(n):
        return n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            if isprime(n / i):
                max_number = n / i
                break
            elif isprime(i):
                max_number = i
    return max_number


if __name__ == "__main__":
    print(f"{solution() = }")
