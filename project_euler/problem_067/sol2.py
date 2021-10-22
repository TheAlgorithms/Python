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

    a = []
    with open(triangle) as f:
        for line in f:
            a.append(list(map(int, line.split(" "))))

    while len(a) != 1:
        b = a.pop()
        x = a[-1]
        for j in range(len(b) - 1):
            x[j] += max(b[j], b[j + 1])
    return a[0][0]


if __name__ == "__main__":
    print(solution())
