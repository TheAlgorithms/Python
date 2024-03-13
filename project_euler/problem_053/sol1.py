"""
Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n!/(r!(n−r)!),where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are greater
than one-million?
"""

from math import factorial


def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def solution():
    """Returns the number of values of nCr, for 1 ≤ n ≤ 100, are greater than
    one-million

    >>> solution()
    4075
    """
    total = 0

    for i in range(1, 101):
        for j in range(1, i + 1):
            if combinations(i, j) > 1e6:
                total += 1
    return total


if __name__ == "__main__":
    print(solution())
