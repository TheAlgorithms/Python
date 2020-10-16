"""
Project Euler Problem 102: https://projecteuler.net/problem=102
Three distinct points are plotted at random
on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000,
such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC
contains the origin, whereas triangle XYZ does not.

Using triangles.txt, a 27K text file containing
the co-ordinates of one thousand "random" triangles,
find the number of triangles for which the interior
contains the origin.
"""
import math


def solution(file_path: str = "triangles.txt") -> int:
    """
    Return number of triangles that include the origin.
    Coordinates are given in the parameter text file path.
    >>> solution()
    228
    """

    f = open(file_path)
    list_of_lines = f.readlines()

    def Area(a1: int, a2: int, b1: int, b2: int, c1: int, c2: int) -> int:
        """
        Return the area of a triangle defined by given coordinates.
        >>> Area(0,0,0,2,2,0)
        2
        """

        a = math.sqrt((b1 - c1) ** 2 + (b2 - c2) ** 2)
        b = math.sqrt((a1 - c1) ** 2 + (a2 - c2) ** 2)
        c = math.sqrt((b1 - a1) ** 2 + (b2 - a2) ** 2)
        s = (a + b + c) / 2
        A = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return A

    count = 0
    for line in list_of_lines:
        a1, a2, b1, b2, c1, c2 = [int(x) for x in line.split(",")]
        A = Area(a1, a2, b1, b2, c1, c2)
        A1 = Area(0, 0, b1, b2, c1, c2)
        A2 = Area(a1, a2, 0, 0, c1, c2)
        A3 = Area(a1, a2, b1, b2, 0, 0)
        if math.isclose(A, A1 + A2 + A3):
            count += 1
    return count


if __name__ == "__main__":
    print(solution())
