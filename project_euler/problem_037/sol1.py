"""
Truncatable primes
Problem 37: https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right
and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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


def list_truncated_nums(n: int) -> list[int]:
    """
    Returns a list of all left and right truncated numbers of n
    >>> list_truncated_nums(927628)
    [927628, 27628, 92762, 7628, 9276, 628, 927, 28, 92, 8, 9]
    >>> list_truncated_nums(467)
    [467, 67, 46, 7, 4]
    >>> list_truncated_nums(58)
    [58, 8, 5]
    """
    str_num = str(n)
    list_nums = [n]
    for i in range(1, len(str_num)):
        list_nums.append(int(str_num[i:]))
        list_nums.append(int(str_num[:-i]))
    return list_nums


def validate(n: int) -> bool:
    """
    To optimize the approach, we will rule out the numbers above 1000,
    whose first or last three digits are not prime
    >>> validate(74679)
    False
    >>> validate(235693)
    False
    >>> validate(3797)
    True
    """
    if len(str(n)) > 3 and (
        not is_prime(int(str(n)[-3:])) or not is_prime(int(str(n)[:3]))
    ):
        return False
    return True


def compute_truncated_primes(count: int = 11) -> list[int]:
    """
    Returns the list of truncated primes
    >>> compute_truncated_primes(11)
    [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
    """
    list_truncated_primes: list[int] = []
    num = 13
    while len(list_truncated_primes) != count:
        if validate(num):
            list_nums = list_truncated_nums(num)
            if all(is_prime(i) for i in list_nums):
                list_truncated_primes.append(num)
        num += 2
    return list_truncated_primes


def solution() -> int:
    """
    Returns the sum of truncated primes
    """
    return sum(compute_truncated_primes(11))


if __name__ == "__main__":
    print(f"{sum(compute_truncated_primes(11)) = }")
