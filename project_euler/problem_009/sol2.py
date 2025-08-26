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


def solution(n: int = 1000) -> int:
    """
    Return the product of a,b,c which are Pythagorean Triplet that satisfies
    the following:
      1. a < b < c
      2. a**2 + b**2 = c**2
      3. a + b + c = n

    >>> solution(36)
    1620
    >>> solution(126)
    66780
    """

    product = -1
    candidate = 0
    for a in range(1, n // 3):
        # Solving the two equations a**2+b**2=c**2 and a+b+c=N eliminating c
        b = (n * n - 2 * a * n) // (2 * n - 2 * a)
        c = n - a - b
        if c * c == (a * a + b * b):
            candidate = a * b * c
            product = max(product, candidate)
    return product


if __name__ == "__main__":
    print(f"{solution() = }")
