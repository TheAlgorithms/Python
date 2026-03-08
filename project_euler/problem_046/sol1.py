"""
Problem 46: https://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2 x 12
15 = 7 + 2 x 22
21 = 3 + 2 x 32
25 = 7 + 2 x 32
27 = 19 + 2 x 22
33 = 31 + 2 x 12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

from __future__ import annotations

import math


def is_prime(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n)).

    A number is prime if it has exactly two factors: 1 and itself.

    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(27)
    False
    >>> is_prime(87)
    False
    >>> is_prime(563)
    True
    >>> is_prime(2999)
    True
    >>> is_prime(67483)
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


odd_composites = [num for num in range(3, 100001, 2) if not is_prime(num)]


def compute_nums(n: int) -> list[int]:
    """
    Returns a list of first n odd composite numbers which do
    not follow the conjecture.
    >>> compute_nums(1)
    [5777]
    >>> compute_nums(2)
    [5777, 5993]
    >>> compute_nums(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    >>> compute_nums("a")
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    >>> compute_nums(1.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer

    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be >= 0")

    list_nums = []
    for num in range(len(odd_composites)):
        i = 0
        while 2 * i * i <= odd_composites[num]:
            rem = odd_composites[num] - 2 * i * i
            if is_prime(rem):
                break
            i += 1
        else:
            list_nums.append(odd_composites[num])
            if len(list_nums) == n:
                return list_nums

    return []


def solution() -> int:
    """Return the solution to the problem"""
    return compute_nums(1)[0]


if __name__ == "__main__":
    print(f"{solution() = }")
