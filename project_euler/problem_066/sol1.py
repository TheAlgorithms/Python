"""
Problem Title: Problem 66 - Diophantine equation

Link to Problem: https://projecteuler.net/problem=66

Problem Description:

Consider quadratic Diophantine equations of the form:

x**2 – D*(y**2) = 1

For example, when D=13,
the minimal solution in x is 6492 – 13*1802 = 1.

It can be assumed that there are no solutions
in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
we obtain the following:

32 – 2*22 = 1
22 – 3*12 = 1
92 – 5*42 = 1
52 – 6*22 = 1
82 – 7*32 = 1

Hence, by considering minimal solutions in x for D ≤ 7,
the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x
for which the largest value of x is obtained.
"""

from sympy.solvers.diophantine.diophantine import diop_DN


def solution(D_limit: int = 1001) -> int:
    """
    This function finds the value of D in minimal solutions of x
    in the Diophantine equation x**2 – D*(y**2) = 1 for which the
    largest value of x is obtained.

    >>> solution(1001)
    661
    """
    largest_x = 0
    corresponding_D = 0

    for D in range(1, D_limit):
        # diop_DN(D, 1)       --> [(x,y)]
        # diop_DN(D, 1)[0]    --> (x,y)
        # diop_DN(D, 1)[0][0] --> x
        x_value = diop_DN(D, 1)[0][0]

        if x_value > largest_x:
            largest_x = x_value
            corresponding_D = D

    return corresponding_D


if __name__ == "__main__":
    print(f"{solution() = }")
