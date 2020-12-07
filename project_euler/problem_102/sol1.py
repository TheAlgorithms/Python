"""
Three distinct points are plotted at random on a Cartesian plane,
for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas
triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text
file containing the coordinates of one thousand "random" triangles, find
the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the
example given above.
"""

import os
from typing import List, Tuple

Vector = Tuple[int, int]


def vector_product(point1: Vector, point2: Vector) -> int:
    """
    Return the 2-d vector product of two vectors.
    >>> vector_product((1, 2), (-5, 0))
    10
    >>> vector_product((3, 1), (6, 10))
    24
    """
    return point1[0] * point2[1] - point1[1] * point2[0]


def contains_origin(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> bool:
    """
    Check if the triangle given by the points A(x1, y1), B(x2, y2), C(x3, y3)
    contains the origin.
    >>> contains_origin(-340, 495, -153, -910, 835, -947)
    True
    >>> contains_origin(-175, 41, -421, -714, 574, -645)
    False
    """
    vector_A: Vector = (x1, y1)
    vector_A_to_B: Vector = (x2 - x1, y2 - y1)
    vector_A_to_C: Vector = (x3 - x1, y3 - y1)
    a: float = -vector_product(vector_A, vector_A_to_B) / vector_product(
        vector_A_to_C, vector_A_to_B
    )
    b: float = +vector_product(vector_A, vector_A_to_C) / vector_product(
        vector_A_to_C, vector_A_to_B
    )

    return a > 0 and b > 0 and a + b < 1


def solution() -> int:
    """
    Find the number of triangles whose interior contains the origin.
    """
    script_dir: str = os.path.abspath(os.path.dirname(__file__))
    triangle_file: str = os.path.join(script_dir, "p102_triangles.txt")

    with open(triangle_file, "r") as f:
        data = f.read()

    triangles: List[List[int]] = [
        list(map(int, line.split(","))) for line in data.strip().split("\n")
    ]
    ret: int = 0
    triangle: List[int]

    for triangle in triangles:
        ret += contains_origin(*triangle)

    return ret


if __name__ == "__main__":
    print(f"{solution() = }")
