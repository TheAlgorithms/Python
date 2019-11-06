"""
Problem Statement:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solution():
    """
     Returns the product of a,b,c which are Pythagorean Triplet that satisfies
     the following:

     1. a**2 + b**2 = c**2
     2. a + b + c = 1000

    # The code below has been commented due to slow execution affecting Travis.
    # >>> solution()
    # 31875000
    """
    return [
        a * b * c
        for a in range(1, 999)
        for b in range(a, 999)
        for c in range(b, 999)
        if (a * a + b * b == c * c) and (a + b + c == 1000)
    ][0]


if __name__ == "__main__":
    print(solution())
