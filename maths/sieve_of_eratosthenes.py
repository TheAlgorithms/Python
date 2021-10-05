"""
Sieve of Eratosthones

The sieve of Eratosthenes is an algorithm used to find prime numbers, less than or
equal to a given value.
Illustration:
https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

doctest provider: Bruno Simas Hadlich (https://github.com/brunohadlich)
Also thanks to Dmitry (https://github.com/LizardWizzard) for finding the problem
"""


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

    if num < 2:
        return []

    sieve = [True] * (num + 1)
    sieve[0] = sieve[1] = False

    # Do even numbers separately
    primes = [2]
    for i in range(4, num + 1, 2):
        sieve[i] = False

    p = 3
    while p * p <= num:
        # If p is a prime
        if sieve[p] is True:
            primes.append(p)

            # Set multiples of start be False
            for i in range(p * p, num + 1, p):
                sieve[i] = False
        p += 2

    for i in range(p, num + 1, 2):
        if sieve[i] is True:
            primes.append(i)

    return primes


if __name__ == "__main__":
    print(prime_sieve(int(input("Get all primes less than or equal to: ").strip())))
