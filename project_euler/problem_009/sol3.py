"""
Project Euler Problem 9: https://projecteuler.net/problem=9

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.

References:
    - https://en.wikipedia.org/wiki/Pythagorean_triple
"""


def solution() -> int:
    """
    Returns the product of a,b,c which are Pythagorean Triplet that satisfies
    the following:
      1. a**2 + b**2 = c**2
      2. a + b + c = 1000

    >>> solution()
    31875000
    """

    return next(
        iter(
            [
                a * b * (1000 - a - b)
                for a in range(1, 999)
                for b in range(a, 999)
                if (a * a + b * b == (1000 - a - b) ** 2)
            ]
        )
    )


if __name__ == "__main__":
    print(f"{solution() = }")
