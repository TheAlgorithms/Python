"""
Project Euler Problem 7: https://projecteuler.net/problem=7

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""


def is_prime(number: int) -> bool:
    """
    Determines whether the given number is prime or not

    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(29)
    True
    """

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
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
