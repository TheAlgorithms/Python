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
from __future__ import annotations

import sys


def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int]:
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
    # base cases
    if abs(a) == 1:
        return a, 0
    elif abs(b) == 1:
        return 0, b

    old_remainder, remainder = a, b
    old_coeff_a, coeff_a = 1, 0
    old_coeff_b, coeff_b = 0, 1

    while remainder != 0:
        quotient = old_remainder // remainder
        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_coeff_a, coeff_a = coeff_a, old_coeff_a - quotient * coeff_a
        old_coeff_b, coeff_b = coeff_b, old_coeff_b - quotient * coeff_b

    # sign correction for negative numbers
    if a < 0:
        old_coeff_a = -old_coeff_a
    if b < 0:
        old_coeff_b = -old_coeff_b

    return old_coeff_a, old_coeff_b


def main():
    """Call Extended Euclidean Algorithm."""
    if len(sys.argv) < 3:
        print("2 integer arguments required")
        return 1
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(extended_euclidean_algorithm(a, b))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
