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

from pathlib import Path
from typing import List, Tuple


def vector_product(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
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
    point_a: Tuple[int, int] = (x1, y1)
    point_a_to_b: Tuple[int, int] = (x2 - x1, y2 - y1)
    point_a_to_c: Tuple[int, int] = (x3 - x1, y3 - y1)
    a: float = -vector_product(point_a, point_a_to_b) / vector_product(
        point_a_to_c, point_a_to_b
    )
    b: float = +vector_product(point_a, point_a_to_c) / vector_product(
        point_a_to_c, point_a_to_b
    )

    return a > 0 and b > 0 and a + b < 1


def solution(filename: str = "p102_triangles.txt") -> int:
    """
    Find the number of triangles whose interior contains the origin.
    >>> solution("test_triangles.txt")
    1
    """
    data: str = Path(__file__).parent.joinpath(filename).read_text(encoding="utf-8")

    triangles: List[List[int]] = []
    for line in data.strip().split("\n"):
        triangles.append([int(number) for number in line.split(",")])

    ret: int = 0
    triangle: List[int]

    for triangle in triangles:
        ret += contains_origin(*triangle)

    return ret


if __name__ == "__main__":
    print(f"{solution() = }")
