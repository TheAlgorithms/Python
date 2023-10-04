"""
Project Euler Problem 73: https://projecteuler.net/problem=73

Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size,
we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set
of reduced proper fractions for d ≤ 12,000?
"""

from math import gcd


def solution(max_d: int = 12_000) -> int:
    """
    Returns number of fractions lie between 1/3 and 1/2 in the sorted set
    of reduced proper fractions for d ≤ max_d

    >>> solution(4)
    0

    >>> solution(5)
    1

    >>> solution(8)
    3
    """

    fractions_number = 0
    for d in range(max_d + 1):
        for n in range(d // 3 + 1, (d + 1) // 2):
            if gcd(n, d) == 1:
                fractions_number += 1
    return fractions_number


if __name__ == "__main__":
    print(f"{solution() = }")
