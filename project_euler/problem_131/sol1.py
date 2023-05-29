"""
Project Euler Problem 131: https://projecteuler.net/problem=131

There are some prime values, p, for which there exists a positive integer, n,
such that the expression n^3 + n^2p is a perfect cube.

For example, when p = 19, 8^3 + 8^2 x 19 = 12^3.

What is perhaps most surprising is that for each prime with this property
the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
"""

from math import isqrt


def is_prime(number: int) -> bool:
    """
    Determines whether number is prime

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False
    """

    return all(number % divisor != 0 for divisor in range(2, isqrt(number) + 1))


def solution(max_prime: int = 10**6) -> int:
    """
    Returns number of primes below max_prime with the property

    >>> solution(100)
    4
    """

    primes_count = 0
    cube_index = 1
    prime_candidate = 7
    while prime_candidate < max_prime:
        primes_count += is_prime(prime_candidate)

        cube_index += 1
        prime_candidate += 6 * cube_index

    return primes_count


if __name__ == "__main__":
    print(f"{solution() = }")
