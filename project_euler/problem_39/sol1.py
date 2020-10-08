"""
https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from __future__ import annotations

import typing
from collections import Counter


def pythagorean_triple(max_perimeter: int) -> typing.Counter[int]:
    """
    Returns a dictionary with keys as the perimeter of a right angled triangle
    and value as the number of corresponding triplets.
    >>> pythagorean_triple(15)
    Counter({12: 1})
    >>> pythagorean_triple(40)
    Counter({12: 1, 30: 1, 24: 1, 40: 1, 36: 1})
    >>> pythagorean_triple(50)
    Counter({12: 1, 30: 1, 24: 1, 40: 1, 36: 1, 48: 1})
    """
    triplets: typing.Counter[int] = Counter()
    for base in range(1, max_perimeter + 1):
        for perpendicular in range(base, max_perimeter + 1):
            hypotenuse = (base * base + perpendicular * perpendicular) ** 0.5
            if hypotenuse == int((hypotenuse)):
                perimeter = int(base + perpendicular + hypotenuse)
                if perimeter > max_perimeter:
                    continue
                else:
                    triplets[perimeter] += 1
    return triplets


def solution(n: int = 1000) -> int:
    """Returns perimeter with maximum solutions."""
    triplets = pythagorean_triple(n)
    perimeter, _ = triplets.most_common()[0]
    return perimeter


if __name__ == "__main__":
    result = solution(1000)
    print(f"Perimiter {result} has maximum solutions")
