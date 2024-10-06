"""
Project Euler Problem 231: https://projecteuler.net/problem=231

The binomial coefficient choose(10, 3)=120.
120 = 2^3 * 3 * 5 = 2 * 2 * 2 * 3 * 5, and 2 + 2 + 2 + 3 + 5 = 14.
So the sum of the terms in the prime factorisation of choose(10, 3) is 14.

Find the sum of the terms in the prime factorisation of choose(20_000_000, 15_000_000).
"""

from sympy import factorint
from collections import Counter


def solution(n: int = 20_000_000, k: int = 15_000_000) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(10, 3)
    14
    """

    a, b = 20_000_000, 15_000_000
    top, bot = [], []
    for t in range(b + 1, a + 1):
        top.extend(factorint(t, multiple=True))
    for b in range(1, a - b + 1):
        bot.extend(factorint(b, multiple=True))

    top = Counter(top)
    bot = Counter(bot)
    s = 0
    for k, v in top.items():
        s += k * (v - bot[k])
    return s


if __name__ == "__main__":
    print(f"{solution() = }")
