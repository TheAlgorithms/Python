"""
Project Euler Problem 58: https://projecteuler.net/problem=58

Starting with 1 and spiralling anticlockwise in the
following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares
lie along the bottom right diagonal, but what
is more interesting is that 8 out of the 13
numbers lying along both diagonals are prime;
that is, a ratio of 8/13 ≈ 62%. If one complete
new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed.
If this process is continued, what is the side length
of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?

Solution: Iteratively add layers around the spiral.
Keep track of number of primes so far and always
calculate that number divided by all diagonal values.
Stop as soon as the ratio falls below 10%.
"""
import math


def prime(n: int) -> bool:
    """
    Check if n is a prime.
    >>> prime(3)
    True
    >>> prime(4)
    False
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


def f(k: int, n_primes: int, x: int) -> (int, int):
    """
    Return total number of primes after adding the kth
    layer to the spiral and the last number added.

    >>> f(1,0,1)
    (3, 9)
    """
    diff_corners = (k - 1) * 2 + 1
    corner_numbers = [
        x + diff_corners + 1,
        x + diff_corners * 2 + 2,
        x + diff_corners * 3 + 3,
        x + diff_corners * 4 + 4,
    ]
    return (
        n_primes + sum([prime(corner) for corner in corner_numbers]),
        corner_numbers[3],
    )


def solution(limit: int = 0.1) -> int:
    """Return the smallest side length of the square spiral
    where the fraction of primes in the diagonals is < 0.1

    >>> solution()
    26241
    """

    p = 1
    k = 1
    n_primes = 0
    x = 1
    while p > limit:
        n_primes, x = f(k, n_primes, x)
        n_diags = k * 4 + 1
        p = n_primes / n_diags
        k += 1
    return (k - 1) * 2 + 1


if __name__ == "__main__":
    print(solution())
