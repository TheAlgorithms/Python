"""
Problem 123: https://projecteuler.net/problem=123

Name: Prime square remainders

Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and
let r be the remainder when (pn−1)^n + (pn+1)^n is divided by pn^2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.
The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.


Solution:

n=1: (p-1) + (p+1) = 2p
n=2: (p-1)^2 + (p+1)^2
     = p^2 + 1 - 2p + p^2 + 1 + 2p  (Using (p+b)^2 = (p^2 + b^2 + 2pb),
                                           (p-b)^2 = (p^2 + b^2 - 2pb) and b = 1)
     = 2p^2 + 2
n=3: (p-1)^3 + (p+1)^3  (Similarly using (p+b)^3 & (p-b)^3 formula and so on)
     = 2p^3 + 6p
n=4: 2p^4 + 12p^2 + 2
n=5: 2p^5 + 20p^3 + 10p

As you could see, when the expression is divided by p^2.
Except for the last term, the rest will result in the remainder 0.

n=1: 2p
n=2: 2
n=3: 6p
n=4: 2
n=5: 10p

So it could be simplified as,
    r = 2pn when n is odd
    r = 2   when n is even.
"""
from __future__ import annotations

from typing import Generator


def sieve() -> Generator[int, None, None]:
    """
    Returns a prime number generator using sieve method.
    >>> type(sieve())
    <class 'generator'>
    >>> primes = sieve()
    >>> next(primes)
    2
    >>> next(primes)
    3
    >>> next(primes)
    5
    >>> next(primes)
    7
    >>> next(primes)
    11
    >>> next(primes)
    13
    """
    factor_map: dict[int, int] = {}
    prime = 2
    while True:
        factor = factor_map.pop(prime, None)
        if factor:
            x = factor + prime
            while x in factor_map:
                x += factor
            factor_map[x] = factor
        else:
            factor_map[prime * prime] = prime
            yield prime
        prime += 1


def solution(limit: float = 1e10) -> int:
    """
    Returns the least value of n for which the remainder first exceeds 10^10.
    >>> solution(1e8)
    2371
    >>> solution(1e9)
    7037
    """
    primes = sieve()

    n = 1
    while True:
        prime = next(primes)
        if (2 * prime * n) > limit:
            return n
        # Ignore the next prime as the reminder will be 2.
        next(primes)
        n += 2


if __name__ == "__main__":
    print(solution())
