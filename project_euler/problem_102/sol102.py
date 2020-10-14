"""Project Euler Problem 102: https://projecteuler.net/problem=80

"It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square
roots is infinite without any repeating pattern at all.

"The square root of two is 1.41421356237309504880..., and the digital
sum of the first one hundred decimal digits is 475.

"For the first one hundred natural numbers, find the total of the
digital sums of the first one hundred decimal digits for all the
irrational square roots."

To solve this problem, create vectors from (0,0) to each of the points
of the triangle. Then, add the angles between all the vector. If the
triangle includes the origin, the angles will add to 2*pi
radians. Otherwise, they will add to less.

References:
 - https://stackoverflow.com/questions/2049582/

"""

# For type hints for methods using a parameter of the enclosing class
from __future__ import annotations

import math
import os


class Vector:
    """
    A simple two-dimensional vector class. It provides the following
    public methods:

    __init__: Initialize a vector from the origin to point (x,y)

    dot: Provide the dot product of this vector with another

    length: Return the length of the vector

    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initialize a vector with x and y coordinates from the origin.

        >>> isinstance(Vector(1,2), Vector)
        True
        """

        self.x = x
        self.y = y

    def length(self) -> float:
        """
        Compute the length of the vector

        >>> Vector(3,4).length()
        5.0
        """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def dot_product(self, v: Vector) -> float:
        """
        Compute the dot product of two vectors

        >>> Vector(1,2).dot_product(Vector(3,4))
        11.0
        """
        return float(self.x * v.x + self.y * v.y)


def solution() -> int:
    """
    Returns the number of triangles from the input that contains the origin.


    >>> solution()
    228
    """

    ninside = 0
    filename = os.path.join(os.path.dirname(__file__), "p102_triangles.txt")
    with open(filename) as infile:
        for line in infile:
            coords = line.strip().split(",")
            triangle_vectors = []
            for coord_id in range(3):
                triangle_vectors.append(Vector(float(coords[coord_id * 2]), \
                                               float(coords[coord_id * 2 + 1])))
            angle_sum = 0.0
            for vertex_id in range(len(triangle_vectors)):
                angle_start = triangle_vectors[vertex_id]
                angle_end = triangle_vectors[(vertex_id + 1) % len(triangle_vectors)]
                angle = math.acos(angle_start.dot_product(angle_end) / \
                                  (angle_start.length() * angle_end.length()))
                angle_sum += angle
            if math.isclose(angle_sum, 2 * math.pi):
                ninside += 1
    return ninside


if __name__ == "__main__":
    import doctest

    doctest.testmod()
