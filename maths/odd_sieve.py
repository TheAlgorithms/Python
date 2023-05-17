from itertools import compress, repeat
from math import ceil, sqrt


def odd_sieve(num: int) -> list[int]:
    """
    Returns the prime numbers < `num`. The prime numbers are calculated using an
    odd sieve implementation of the Sieve of Eratosthenes algorithm
    (see for reference https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

    >>> odd_sieve(2)
    []
    >>> odd_sieve(3)
    [2]
    >>> odd_sieve(10)
    [2, 3, 5, 7]
    >>> odd_sieve(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """

    if num <= 2:
        return []
    if num == 3:
        return [2]

    # Odd sieve for numbers in range [3, num - 1]
    sieve = bytearray(b"\x01") * ((num >> 1) - 1)

    for i in range(3, int(sqrt(num)) + 1, 2):
        if sieve[(i >> 1) - 1]:
            i_squared = i**2
            sieve[(i_squared >> 1) - 1 :: i] = repeat(
                0, ceil((num - i_squared) / (i << 1))
            )

    return [2] + list(compress(range(3, num, 2), sieve))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
