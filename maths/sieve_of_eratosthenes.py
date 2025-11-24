"""
Sieve of Eratosthenes

The sieve of Eratosthenes is an algorithm used to find prime numbers, less than or
equal to a given value.
Illustration:
https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

doctest provider: Bruno Simas Hadlich (https://github.com/brunohadlich)
Also thanks to Dmitry (https://github.com/LizardWizzard) for finding the problem
optimized by : Sumit Nayak (https://github.com/Sumit210106/)
"""

from __future__ import annotations


def prime_sieve(num: int) -> list[int]:
    """
    Returns a list with all prime numbers up to n.

    >>> prime_sieve(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    >>> prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> prime_sieve(10)
    [2, 3, 5, 7]
    >>> prime_sieve(9)
    [2, 3, 5, 7]
    >>> prime_sieve(2)
    [2]
    >>> prime_sieve(1)
    []
    """

    if num <= 0:
        msg = f"{num}: Invalid input, please enter a positive integer."
        raise ValueError(msg)

    if num < 2:
        return []

    sieve = [True] * (num + 1)
    prime = [2]

    # marked all even numbers as non-prime
    for i in range(3, int(pow(num, 0.5)) + 1, 2):
        if sieve[i]:
            for j in range(pow(i, 2), num + 1, 2 * i):
                sieve[j] = False

    # collect odd primes
    for k in range(3, num + 1, 2):
        if sieve[k]:
            prime.append(k)

    return prime


if __name__ == "__main__":
    print(prime_sieve(int(input("Enter a positive integer: ").strip())))
