"""
Project Euler Problem 234: https://projecteuler.net/problem=234

For any integer n, consider the three functions

f1,n(x,y,z) = x^(n+1) + y^(n+1) - z^(n+1)
f2,n(x,y,z) = (xy + yz + zx)*(x^(n-1) + y^(n-1) - z^(n-1))
f3,n(x,y,z) = xyz*(xn-2 + yn-2 - zn-2)

and their combination

fn(x,y,z) = f1,n(x,y,z) + f2,n(x,y,z) - f3,n(x,y,z)

We call (x,y,z) a golden triple of order k if x, y, and z are all rational numbers
of the form a / b with 0 < a < b ≤ k and there is (at least) one integer n,
so that fn(x,y,z) = 0.

Let s(x,y,z) = x + y + z.
Let t = u / v be the sum of all distinct s(x,y,z) for all golden triples
(x,y,z) of order 35.
All the s(x,y,z) and t must be in reduced form.

Find u + v.


Solution:

By expanding the brackets it is easy to show that
fn(x, y, z) = (x + y + z) * (x^n + y^n - z^n).

Since x,y,z are positive, the requirement fn(x, y, z) = 0 is fulfilled if and
only if x^n + y^n = z^n.

By Fermat's Last Theorem, this means that the absolute value of n can not
exceed 2, i.e. n is in {-2, -1, 0, 1, 2}. We can eliminate n = 0 since then the
equation would reduce to 1 + 1 = 1, for which there are no solutions.

So all we have to do is iterate through the possible numerators and denominators
of x and y, calculate the corresponding z, and check if the corresponding numerator and
denominator are integer and satisfy 0 < z_num < z_den <= 0. We use a set "uniquq_s"
to make sure there are no duplicates, and the fractions.Fraction class to make sure
we get the right numerator and denominator.

Reference:
https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd, sqrt


def is_sq(number: int) -> bool:
    """
    Check if number is a perfect square.

    >>> is_sq(1)
    True
    >>> is_sq(1000001)
    False
    >>> is_sq(1000000)
    True
    """
    sq: int = int(number ** 0.5)
    return number == sq * sq


def add_three(
    x_num: int, x_den: int, y_num: int, y_den: int, z_num: int, z_den: int
) -> tuple[int, int]:
    """
    Given the numerators and denominators of three fractions, return the
    numerator and denominator of their sum in lowest form.
    >>> add_three(1, 3, 1, 3, 1, 3)
    (1, 1)
    >>> add_three(2, 5, 4, 11, 12, 3)
    (262, 55)
    """
    top: int = x_num * y_den * z_den + y_num * x_den * z_den + z_num * x_den * y_den
    bottom: int = x_den * y_den * z_den
    hcf: int = gcd(top, bottom)
    top //= hcf
    bottom //= hcf
    return top, bottom


def solution(order: int = 35) -> int:
    """
    Find the sum of the numerator and denominator of the sum of all s(x,y,z) for
    golden triples (x,y,z) of the given order.

    >>> solution(5)
    296
    >>> solution(10)
    12519
    >>> solution(20)
    19408891927
    """
    unique_s: set = set()
    hcf: int
    total: Fraction = Fraction(0)
    fraction_sum: tuple[int, int]

    for x_num in range(1, order + 1):
        for x_den in range(x_num + 1, order + 1):
            for y_num in range(1, order + 1):
                for y_den in range(y_num + 1, order + 1):
                    # n=1
                    z_num = x_num * y_den + x_den * y_num
                    z_den = x_den * y_den
                    hcf = gcd(z_num, z_den)
                    z_num //= hcf
                    z_den //= hcf
                    if 0 < z_num < z_den <= order:
                        fraction_sum = add_three(
                            x_num, x_den, y_num, y_den, z_num, z_den
                        )
                        unique_s.add(fraction_sum)

                    # n=2
                    z_num = (
                        x_num * x_num * y_den * y_den + x_den * x_den * y_num * y_num
                    )
                    z_den = x_den * x_den * y_den * y_den
                    if is_sq(z_num) and is_sq(z_den):
                        z_num = int(sqrt(z_num))
                        z_den = int(sqrt(z_den))
                        hcf = gcd(z_num, z_den)
                        z_num //= hcf
                        z_den //= hcf
                        if 0 < z_num < z_den <= order:
                            fraction_sum = add_three(
                                x_num, x_den, y_num, y_den, z_num, z_den
                            )
                            unique_s.add(fraction_sum)

                    # n=-1
                    z_num = x_num * y_num
                    z_den = x_den * y_num + x_num * y_den
                    hcf = gcd(z_num, z_den)
                    z_num //= hcf
                    z_den //= hcf
                    if 0 < z_num < z_den <= order:
                        fraction_sum = add_three(
                            x_num, x_den, y_num, y_den, z_num, z_den
                        )
                        unique_s.add(fraction_sum)

                    # n=2
                    z_num = x_num * x_num * y_num * y_num
                    z_den = (
                        x_den * x_den * y_num * y_num + x_num * x_num * y_den * y_den
                    )
                    if is_sq(z_num) and is_sq(z_den):
                        z_num = int(sqrt(z_num))
                        z_den = int(sqrt(z_den))
                        hcf = gcd(z_num, z_den)
                        z_num //= hcf
                        z_den //= hcf
                        if 0 < z_num < z_den <= order:
                            fraction_sum = add_three(
                                x_num, x_den, y_num, y_den, z_num, z_den
                            )
                            unique_s.add(fraction_sum)

    for num, den in unique_s:
        total += Fraction(num, den)

    return total.denominator + total.numerator


if __name__ == "__main__":
    print(f"{solution() = }")
