"""
Project Euler Problem 9: https://projecteuler.net/problem=9

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.

Solution:
Let's consider the constraint a + b + c = n (n = 1000) and think of the values
we can get for each variable while satisfying the constraint. We can have:
    a = 333, b = 333, c = 334
    a = 500, b = 500, c = 0
    a = 5, b = 990, c = 5
and various other combinations. Note that at least one value has to be
at least 333 (or n//3 as n = 1000). Raising at least one variable to
nearly n//2 value decreases another variable's value.

When we introduce the constraint a < b < c, we will have combinations of
three distinct values. The triplet cannot form an isoceles triangle.
Thus, we observe:
    a = 167, b = 333, c = 500
    a = 331, b = 333, c = 336
    a = 1, b = 499, c = 500
If n is even, only two variables will be odd or all will have even values.
Furthermore, the constraint a**2 + b**2 = c**2 suggest the if 'a' or 'b' is odd
then 'c' is odd too and vice versa.

Therefore, our solution will:
- use "a + b + c = 1000" to elimiate 'c' (and hence remove a third for loop)
  by having "c = 1000 - a - b" and hence comparing a**2 + b**2 = (1000-a-b)**2
- have an odd number and an even number to ensure 'a' and 'b' are distinct
- iterate for values of 'b' from (n//2 - 1) to (n//3 + 1) to ensure
  that minimum value of 'c' can be (n//2) and 'a' can be (n//3) at maximum,
  thus satisfying the constraint a < b < c and a + b + c = n

References:
    - https://en.wikipedia.org/wiki/Pythagorean_triple
"""


def solution(n: int = 1000) -> int:
    """
    Returns the product of a,b,c which are Pythagorean Triplet that satisfies
    the following:
      1. a < b < c
      2. a**2 + b**2 = c**2
      3. a + b + c = 1000

    >>> solution()
    31875000
    >>> solution(910)
    11602500
    >>> solution(2002)
    123543420
    """

    for b in range(n // 2 - 1, n // 3, -2):
        for a in range(b - 1, 0, -2):
            c = n - b - a
            if b > c:  # constraint a < b < c should be satisfied
                continue
            if a**2 + b**2 == c**2:  # is it a pythagorean triplet
                return a * b * c


if __name__ == "__main__":
    print(f"{solution() = }")
