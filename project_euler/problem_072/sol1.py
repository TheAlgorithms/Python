"""
Problem 72 Counting fractions: https://projecteuler.net/problem=72

Description:

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we
get: 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper fractions for
d ≤ 1,000,000?

Solution:

Number of numbers between 1 and n that are coprime to n is given by the Euler's Totient
function, phi(n). So, the answer is simply the sum of phi(n) for 2 <= n <= 1,000,000
Sum of phi(d), for all d|n = n. This result can be used to find phi(n) using a sieve.

Time: 1 sec
"""

import numpy as np


def solution(limit: int = 1_000_000) -> int:
    """
    Returns an integer, the solution to the problem
    >>> solution(10)
    31
    >>> solution(100)
    3043
    >>> solution(1_000)
    304191
    """

    # generating an array from -1 to limit
    phi = np.arange(-1, limit)

    for i in range(2, limit + 1):
        if phi[i] == i - 1:
            ind = np.arange(2 * i, limit + 1, i)  # indexes for selection
            phi[ind] -= phi[ind] // i

    return int(np.sum(phi[2 : limit + 1]))


if __name__ == "__main__":
    print(solution())
