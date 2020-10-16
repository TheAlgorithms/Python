"""


Project Euler 66
https://projecteuler.net/problem=66
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm


Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal
solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in
positive integers when D is square.

By finding minimal solutions in x for
D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7,
the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of
x for which the largest value of x is obtained.

"""

from math import sqrt


def continued_fraction(n: int) -> list:

    """
    function to find continued fraction

    >>> continued_fraction(2)
    [1]

    >>> continued_fraction(3)
    [1, 1]

    >>> continued_fraction(5)
    [2]

    >>> continued_fraction(6)
    [2, 2]

    """
    mn = 0.0
    dn = 1.0
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    convergents = [a0]
    # period = 0
    if a0 != sqrt(n):
        while an != 2 * a0:
            mn = dn * an - mn
            dn = (n - mn ** 2) / dn
            an = int((a0 + mn) / dn)
            convergents.append(an)
    return convergents[:-1]


def simple_frac(cf: list()) -> int:
    """
    function to calculate the
    simple fraction from the continued
    fraction.

    >>> simple_frac([1])
    (1, 1)
    >>> simple_frac([1,1])
    (2, 2)
    >>> simple_frac([2])
    (2, 1)
    >>> simple_frac([2,2])
    (5, 5)

    """
    numerator = 1
    denominator = cf.pop()
    while cf:
        denominator = denominator * cf.pop() + numerator
        numerator = denominator
    return denominator, numerator


def solution(limit: int = 1001) -> int:

    """
    function to find value of D in minimal solutions of x
    for which x is largest.
    """
    """
    >>> solution(7)
    5

    """

    largest = 0, 0

    # for loop less than 1000
    for i in range(1, limit):
        if i % sqrt(i) != 0:
            # print("cc",i)
            continued_frac = continued_fraction(i)
            if len(continued_frac) % 2 != 0:
                u, v = simple_frac(continued_frac)
                u = 2 * u ** 2 + 1
                v = 2 * u * v
            else:
                u, v = simple_frac(continued_frac)
            if u > largest[1]:
                largest = i, u

    # print the largest value
    return largest[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution()}")
