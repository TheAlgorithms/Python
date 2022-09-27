"""
Sieve of Eratosthones

Sieve of Eratosthenes is an algorithm used to find prime numbers less than
some given value n.

This implementation seeks to introduce space optimizations to the vanilla
implementation of the algorithm by restricting the search space to odd numbers
(and 2), and taking advantage of Python's bytearray type.

Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

from itertools import compress, count, takewhile
from math import ceil, sqrt


def sieve_of_eratosthenes_2(n: int) -> list[int]:
    """
    Computes the prime numbers < n

    >>> sieve_of_eratosthenes_2(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    >>> sieve_of_eratosthenes_2(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> sieve_of_eratosthenes_2(10)
    [2, 3, 5, 7]
    >>> sieve_of_eratosthenes_2(9)
    [2, 3, 5, 7]
    >>> sieve_of_eratosthenes_2(3)
    [2]
    >>> sieve_of_eratosthenes_2(2)
    []
    >>> sieve_of_eratosthenes_2(1)
    []
    """
    if n <= 2:
        return []
    if n == 3:
        return [2]

    # Odd sieve for numbers in range [3, n - 1]
    sieve = bytearray(b"\x01") * ((n >> 1) - 1)

    u_bound = int(sqrt(n)) + 1
    for i in takewhile(lambda x: x < u_bound, count(3, 2)):
        if sieve[(i >> 1) - 1]:  # Is prime
            sieve[(i * i >> 1) - 1 :: i] = bytearray(b"\x00") * ceil(
                n / (i << 1) - i / 2
            )

    return [2] + list(compress(range(3, n, 2), sieve))


if __name__ == "__main__":
    print(sieve_of_eratosthenes_2(int(input("Enter a positive integer: ").strip())))
