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
     1. a < b < c
     2. a**2 + b**2 = c**2
     3. a + b + c = 1000

    # The code below has been commented due to slow execution affecting Travis.
    # >>> solution()
    # 31875000
    """
    for a in range(300):
        for b in range(400):
            c = 1000 - a - b
            if a < b < c and (a ** 2) + (b ** 2) == (c ** 2):
                return a * b * c


if __name__ == "__main__":
    print("Please Wait...")
    print(solution())
