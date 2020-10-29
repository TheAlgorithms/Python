"""
Project Euler Problem 102: https://projecteuler.net/problem=102 
 
Problem statement: Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.
Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)
X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
NOTE: The first two examples in the file represent the triangles in the example given above.

Solution Explanation: Consider the triangle below.
            (x1, y1)
             A
            / \ 
           /   \
          /     \
         /   *   \
        /  P(x,y) \
       /___________\
      B             C
     (x2, y2)    (x3, y3)

     If the point P lies within the triangle, then,
     area(ABC) = area(APB) + area(BPC) + area(APC) 
 
"""

import os


def area(
    x1: float = -340,
    y1: float = 495,
    x2: float = -153,
    y2: float = -910,
    x3: float = 835,
    y3: float = -947,
) -> float:
    """
    Function to evaluate the area of triangel with given vertices.

    >>> area(1, 2, 4, 5, 6, 3)
    6.0

    >>> area(2, 2, 4, 5, 6, 3)
    5.0

    >>> area()
    690610.5

    """

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)


def isInside(
    x1: float = -340,
    y1: float = 495,
    x2: float = -153,
    y2: float = -910,
    x3: float = 835,
    y3: float = -947,
    x: float = 0,
    y: float = 0,
) -> bool:

    """
    Function to check if the given point lies inside the triangle
    with the given vertices.

    >>> isInside(5, 4, 6, 7, 11, 2, 0, 2)
    False

    >>> isInside()
    True

    """

    a = area(x1, y1, x2, y2, x3, y3)

    a1 = area(x, y, x2, y2, x3, y3)
    a2 = area(x1, y1, x, y, x3, y3)
    a3 = area(x1, y1, x2, y2, x, y)

    return a == a1 + a2 + a3


def solution(data_file: str = "p102_triangles.txt") -> int:
    """
    Function to count the number of triangles in the text file for which the
    interior contains the origin.

    >>> solution()
    228

    """
    f = open(os.path.join(os.path.dirname(__file__), data_file))

    count = 0
    for line in f.readlines():

        if isInside(*list(map(float, line.split(",")))):
            count += 1
    f.close()
    return count


if __name__ == "__main__":
    print(f"{solution() = }")
