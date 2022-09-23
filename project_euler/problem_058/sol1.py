"""
Project Euler Problem 58:https://projecteuler.net/problem=58


Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal ,but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed.
If this process is continued,
what is the side length of the square spiral for which
the ratio of primes along both diagonals first falls below 10%?

Solution: We have to find an odd length side for which square falls below
10%. With every layer we add 4 elements are being added to the diagonals
,lets say we have a square spiral of odd length with side length j,
then if we move from j to j+2, we are adding j*j+j+1,j*j+2*(j+1),j*j+3*(j+1)
j*j+4*(j+1). Out of these 4 only the first three can become prime
because last one reduces to (j+2)*(j+2).
So we check individually each one of these before incrementing our
count of current primes.

"""
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


def solution(ratio: float = 0.1) -> int:
    """
    Returns the side length of the square spiral of odd length greater
    than 1 for which the ratio of primes along both diagonals
    first falls below the given ratio.
    >>> solution(.5)
    11
    >>> solution(.2)
    309
    >>> solution(.111)
    11317
    """

    j = 3
    primes = 3

    while primes / (2 * j - 1) >= ratio:
        for i in range(j * j + j + 1, (j + 2) * (j + 2), j + 1):
            primes += is_prime(i)
        j += 2
    return j


if __name__ == "__main__":
    import doctest

    doctest.testmod()
