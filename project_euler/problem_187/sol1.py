"""
Project Euler Problem 187: https://projecteuler.net/problem=187

A composite is a number containing at least two prime factors.
For example, 15 = 3 x 5; 9 = 3 x 3; 12 = 2 x 2 x 3.

There are ten composites below thirty containing precisely two,
not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10^8, have precisely two,
not necessarily distinct, prime factors?
"""

from math import isqrt


def calculate_prime_numbers(max_number: int) -> list[int]:
    """
    Returns prime numbers below max_number

    >>> calculate_prime_numbers(10)
    [2, 3, 5, 7]
    """

    is_prime = [True] * max_number
    for i in range(2, isqrt(max_number - 1) + 1):
        if is_prime[i]:
            for j in range(i**2, max_number, i):
                is_prime[j] = False

    return [i for i in range(2, max_number) if is_prime[i]]


def solution(max_number: int = 10**8) -> int:
    """
    Returns the number of composite integers below max_number have precisely two,
    not necessarily distinct, prime factors

    >>> solution(30)
    10
    """

    prime_numbers = calculate_prime_numbers(max_number // 2)

    semiprimes_count = 0
    left = 0
    right = len(prime_numbers) - 1
    while left <= right:
        while prime_numbers[left] * prime_numbers[right] >= max_number:
            right -= 1
        semiprimes_count += right - left + 1
        left += 1

    return semiprimes_count


if __name__ == "__main__":
    print(f"{solution() = }")
