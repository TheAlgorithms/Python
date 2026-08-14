"""
Project Euler Problem 7: https://projecteuler.net/problem=7

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""

import math


def is_prime(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n)).
    A number is prime if it has exactly two factors: 1 and itself.
    Returns boolean representing primality of given number (i.e., if the
    result is true, then the number is indeed prime else it is not).

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(27)
    False
    >>> is_prime(2999)
    True
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    """

    if 1 < number < 4:
        # 2 and 3 are primes
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        # Negatives, 0, 1, all even numbers, all multiples of 3 are not primes
        return False

    # All primes number are in format of 6k +/- 1
    for i in range(5, int(math.sqrt(number) + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
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
    >>> solution(3.4)
    5
    >>> solution(0)
    Traceback (most recent call last):
        ...
    ValueError: Parameter nth must be greater than or equal to one.
    >>> solution(-17)
    Traceback (most recent call last):
        ...
    ValueError: Parameter nth must be greater than or equal to one.
    >>> solution([])
    Traceback (most recent call last):
        ...
    TypeError: Parameter nth must be int or castable to int.
    >>> solution("asd")
    Traceback (most recent call last):
        ...
    TypeError: Parameter nth must be int or castable to int.
    """

    try:
        nth = int(nth)
    except (TypeError, ValueError):
        raise TypeError("Parameter nth must be int or castable to int.") from None
    if nth <= 0:
        raise ValueError("Parameter nth must be greater than or equal to one.")
    primes: list[int] = []
    num = 2
    while len(primes) < nth:
        if is_prime(num):
            primes.append(num)
            num += 1
        else:
            num += 1
    return primes[len(primes) - 1]


if __name__ == "__main__":
    print(f"{solution() = }")
