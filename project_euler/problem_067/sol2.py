"""
Problem Statement:
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.
"""

import os


def solution() -> int:
    """
    Finds the maximum total in a triangle as described by the problem statement
    above.
    >>> solution()
    7273
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    triangle_path = os.path.join(script_dir, "triangle.txt")

    with open(triangle_path) as in_file:
        triangle = [[int(i) for i in line.split()] for line in in_file]

    while len(triangle) != 1:
        last_row = triangle.pop()
        curr_row = triangle[-1]
        for j in range(len(last_row) - 1):
            curr_row[j] += max(last_row[j], last_row[j + 1])
    return triangle[0][0]


if __name__ == "__main__":
    print(solution())
