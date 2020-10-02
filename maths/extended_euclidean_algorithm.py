"""
Extended Euclidean Algorithm.

Finds 2 numbers a and b such that it satisfies
the equation am + bn = gcd(m, n) (a.k.a Bezout's Identity)

https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
"""

# @Author: S. Sharma <silentcat>
# @Date:   2019-02-25T12:08:53-06:00
# @Email:  silentcat@protonmail.com
# @Last modified by:   pikulet
# @Last modified time: 2020-10-02

import sys


def sign(n: int) -> int:
    """
    Returns sign of number for correction of negative numbers in algorithm

    >>> sign(4)
    1

    >>> sign(0)
    0

    >>> sign(-8)
    -1

    """
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def extended_euclidean_algorithm(a: int, b: int) -> (int, int):
    """
    Extended Euclidean Algorithm.

    Finds 2 numbers a and b such that it satisfies
    the equation am + bn = gcd(m, n) (a.k.a Bezout's Identity)

    >>> extended_euclidean_algorithm(1, 24)
    (1, 0)

    >>> extended_euclidean_algorithm(8, 14)
    (2, -1)

    >>> extended_euclidean_algorithm(240, 46)
    (-9, 47)

    >>> extended_euclidean_algorithm(1, -4)
    (1, 0)

    >>> extended_euclidean_algorithm(-2, -4)
    (-1, 0)

    >>> extended_euclidean_algorithm(0, -4)
    (0, -1)

    >>> extended_euclidean_algorithm(2, 0)
    (1, 0)

    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # sign correction for negative numbers
    if abs(a) == 1:
        return sign(a), 0
    elif abs(b) == 1:
        return 0, sign(b)
    else:
        return (sign(a) * old_s, sign(b) * old_t)


def main():
    """Call Extended Euclidean Algorithm."""
    if len(sys.argv) < 3:
        print("2 integer arguments required")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(extended_euclidean_algorithm(a, b))


if __name__ == "__main__":
    main()
