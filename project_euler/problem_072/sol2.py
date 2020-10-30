"""
Project Euler Problem 72: https://projecteuler.net/problem=72

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size,
we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions
for d ≤ 1,000,000?
"""


def solution(limit: int = 1000000) -> int:
    """
    Return the number of reduced proper fractions with denominator less than limit.
    >>> solution(8)
    21
    >>> solution(1000)
    304191
    """
    primes = set(range(3, limit, 2))
    primes.add(2)
    for p in range(3, limit, 2):
        if p not in primes:
            continue
        primes.difference_update(set(range(p * p, limit, p)))

    phi = [float(n) for n in range(limit + 1)]

    for p in primes:
        for n in range(p, limit + 1, p):
            phi[n] *= 1 - 1 / p

    return int(sum(phi[2:]))


if __name__ == "__main__":
    print(f"{solution() = }")
