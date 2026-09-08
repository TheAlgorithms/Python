"""
Project Euler Problem 91: https://projecteuler.net/problem=91

The points P (x1, y1) and Q (x2, y2) are plotted at integer coordinates and
are joined to the origin, O(0,0), to form ΔOPQ.
￼
There are exactly fourteen triangles containing a right angle that can be formed
when each coordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.
￼
Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""

from itertools import combinations, product


def is_right(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Check if the triangle described by P(x1,y1), Q(x2,y2) and O(0,0) is right-angled.
    Note: this doesn't check if P and Q are equal, but that's handled by the use of
    itertools.combinations in the solution function.

    >>> is_right(0, 1, 2, 0)
    True
    >>> is_right(1, 0, 2, 2)
    False
    """
    if x1 == y1 == 0 or x2 == y2 == 0:
        return False
    a_square = x1 * x1 + y1 * y1
    b_square = x2 * x2 + y2 * y2
    c_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    return (
        a_square + b_square == c_square
        or a_square + c_square == b_square
        or b_square + c_square == a_square
    )


def solution(limit: int = 50) -> int:
    """
    Return the number of right triangles OPQ that can be formed by two points P, Q
    which have both x- and y- coordinates between 0 and limit inclusive.

    >>> solution(2)
    14
    >>> solution(10)
    448
    """
    return sum(
        1
        for pt1, pt2 in combinations(product(range(limit + 1), repeat=2), 2)
        if is_right(*pt1, *pt2)
    )


if __name__ == "__main__":
    print(f"{solution() = }")
