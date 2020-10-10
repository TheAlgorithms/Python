"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an
integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided
right angle triangle, and other lengths allow more than one solution to be found; for
example, using 120 cm it is possible to form exactly three different integer sided
right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can
exactly one integer sided right angle triangle be formed?
"""

from collections import defaultdict
from math import gcd
from typing import DefaultDict


def solution(limit: int = 1500000) -> int:
    """
    Return the number of values of L <= limit such that a wire of length L can be
    formmed into an integer sided right angle triangle in exactly one way.
    >>> solution(50)
    6
    >>> solution(1000)
    112
    """
    freqs: DefaultDict = defaultdict(int)
    m = 2
    while 2 * m * (m + 1) <= limit:
        for n in range((m % 2) + 1, m, 2):
            if gcd(m, n) > 1:
                continue
            perim = 2 * m * (m + n)
            for p in range(perim, limit + 1, perim):
                freqs[p] += 1
        m += 1
    return sum(1 for v in freqs.values() if v == 1)


if __name__ == "__main__":
    print(solution())
