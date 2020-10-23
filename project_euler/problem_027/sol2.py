"""
Project Euler Problem 27
https://projecteuler.net/problem=27

Problem Statement:

Euler discovered the remarkable quadratic formula:
n2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 412 + 41 + 41 is clearly divisible by 41.
The incredible formula  n2 − 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, −79 and
1601, is −126479.
Considering quadratics of the form:
n² + an + b, where |a| &lt; 1000 and |b| &lt; 1000
where |n| is the modulus/absolute value of ne.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.

Solution:
This is almost the same algorithm as sol1.py authored by @cclauss. The main
difference is that we generate the primes at the beginning rather than checking
for primeness on the fly. since for n=b, n^2 + a*n + b will always be divisible
by b, the theoretical maximum number we have to check for primeness is
(b_limit - 1)^2 + a_limit * b_limit + b_limit. For the real problem,
a_limit = b_limit = 1000 so we need to generate primes up to 1998000, just under 2m.
In practice, the largest prime we actually end up checking for primeness is 12989,
but I can't see any way we could have determined that before running the algorithm.
If there was, we'd only need to generate primes up to 13000 instead of 2000000,
which would result in a code speedup of about 50%

"""

from typing import Set


def sieve(limit: int) -> Set[int]:
    primes = set(range(3, limit, 2))
    primes.add(2)
    p = 3
    while p * p < limit:
        if p in primes:
            primes.difference_update(set(range(p * p, limit, p)))
        p += 2

    return primes


def solution(a_limit: int = 1000, b_limit: int = 1000) -> int:
    """
    >>> solution(1000, 1000)
    -59231
    >>> solution(200, 1000)
    -59231
    >>> solution(200, 200)
    -4925
    >>> solution(-1000, 1000)
    0
    >>> solution(-1000, -1000)
    0
    """

    primes = sieve(2000000)

    longest = (0, 0, 0)  # length, a, b
    for a in range((a_limit * -1) + 1, a_limit):
        for b in range(2, b_limit):
            if b in primes:
                count = 0
                n = 0
                while (n ** 2) + (a * n) + b in primes:
                    count += 1
                    n += 1
                if count > longest[0]:
                    longest = (count, a, b)
    ans = longest[1] * longest[2]
    return ans


if __name__ == "__main__":
    print(f"solution() = {solution()}")
