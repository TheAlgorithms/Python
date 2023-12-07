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

from numba import njit
from math import gcd

@njit
def solution(limit: int=12_000) -> int:
    """
    Returns the number of fractions lying between 1/3 and 1/2
    in the sorted set of reduced proper fractions for d ≤ limit.

    Args:
    - limit (int): The maximum denominator value.

    Returns:
    - int: Number of fractions between 1/3 and 1/2.

    Example:
    >>> count_fractions(4)
    0
    >>> count_fractions(5)
    1
    >>> count_fractions(8)
    3
    """

    count = 0

    for denominator in range(2, limit + 1):
        lower_limit = denominator // 3 + 1
        upper_limit = (denominator - 1) // 2
        divisors = 0

        for numerator in range(lower_limit, upper_limit + 1):
            if gcd(numerator, denominator) != 1:
                divisors += 1

        count += upper_limit - lower_limit + 1 - divisors

    return count


if __name__ == "__main__":
    print(f"{solution() = }")
