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
def solution(limit: int = 12_000) -> int:
    """
    Returns the number of fractions lying between 1/3 and 1/2
    in the sorted set of reduced proper fractions for d ≤ limit.

    Args:
    - limit (int): The maximum denominator value.

    Returns:
    - int: Number of fractions between 1/3 and 1/2.

    Example:
    >>> solution(4)
    0
    >>> solution(5)
    1
    >>> solution(8)
    3
    """
    phi = [i for i in range(limit + 1)]
    count = 0

    for d in range(2, limit + 1):
        if phi[d] == d:
            for j in range(d, limit + 1, d):
                phi[j] -= phi[j] // d

        count += phi[d] // 2 - phi[(d + 2) // 3]

    return count

if __name__ == "__main__":
    print(f"{solution() = }")
