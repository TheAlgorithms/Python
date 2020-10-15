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


def solution():
    """
    Finds the maximum total in a triangle as described by the problem statement
    above.

    >>> solution()
    7273
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    triangle = os.path.join(script_dir, "triangle.txt")

    with open(triangle, "r") as f:
        triangle = f.readlines()

    a = map(lambda x: x.rstrip("\r\n").split(" "), triangle)
    a = list(map(lambda x: list(map(lambda y: int(y), x)), a))

    for i in range(1, len(a)):
        for j in range(len(a[i])):
            if j != len(a[i - 1]):
                number1 = a[i - 1][j]
            else:
                number1 = 0
            if j > 0:
                number2 = a[i - 1][j - 1]
            else:
                number2 = 0
            a[i][j] += max(number1, number2)
    return max(a[-1])


if __name__ == "__main__":
    print(solution())
