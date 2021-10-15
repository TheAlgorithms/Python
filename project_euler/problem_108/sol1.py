"""
Problem Title: Diophantine reciprocals I

Link to Problem: https://projecteuler.net/problem=108

Problem Description:

In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n

For n = 4 there are exactly three distinct solutions:

1/5 + 1/20 = 1/4
1/6 + 1/12 = 1/4
1/8 + 1/8 = 1/4

What is the least value of n for which the number
of distinct solutions exceeds one-thousand?

NOTE: The runtime of this solution is not great.
It can be improved by minimizing the difference upper_bound-lower_bound,
but this is accomplished by guessing and checking. Because of this,
I would consider this to be a less than optimal, brute-force solution.
"""


from sympy import Eq, S
from sympy.abc import x, y
from sympy.solvers.diophantine.diophantine import diophantine

"""
Helper function that will filter out solutions with x
or y values that are < 0.
"""


def check_xy_negative(solution: (int, int)) -> bool:
    """
    >>> check_xy_negative([-1, 1])
    True
    >>> check_xy_positive([5, -7])
    True
    >>> check_xy_positive([0, 0])
    False
    >>> check_xy_positive([7, 85])
    False
    """
    if solution[0] < 0 or solution[1] < 0:
        return True
    return False


"""
Helper function that finds the number of distinct solutions
to the Diophantine equation 1/x + 1/y = 1/n given n.
"""


def find_num_solutions(n: int) -> int:
    """
    >>> find_num_solutions(500)
    34
    >>> find_num_solutions(6789)
    26
    >>> find_num_solutions(180180)
    2024
    """
    solutions = diophantine(Eq(1 / x + 1 / y, S(1) / n))
    positive_solutions = filter(check_xy_negative, solutions)

    return len(list(set(positive_solutions)))


"""
Function that finds the first value of n for which
the distinct number of solutions to the Diophantine
equation 1/x + 1/y = 1/n exceeds 1000.

Returns n if found within the range
(lower_bound, upper_bound), -1 otherwise.
"""


def solution(lower_bound: int, upper_bound: int) -> int:
    """
    >>> solution(1, 10 ** 6)
    180180
    """
    for i in range(lower_bound, upper_bound):
        if find_num_solutions(i) > 1000:
            return i
    return -1


if __name__ == "__main__":
    print(f"{solution() = }")
