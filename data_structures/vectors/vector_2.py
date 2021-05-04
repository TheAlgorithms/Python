from __future__ import annotations

import math

"""
In mathematics and physics, a vector is an element of a vector space. The Vector2-class
implements 2-dimensional vectors together with various vector-operations
(description adapted from
https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)).
"""


class Vector2:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def equals_exactly(self, vector: Vector2) -> bool:
        """
        Check for exact vector equality

        >>> Vector2(1, 0).equals_exactly(Vector2(1, 0))
        True
        >>> Vector2(1.23, 4.56).equals_exactly(Vector2(0, 0))
        False
        """

        return self.x == vector.x and self.y == vector.y

    def equals_approximately(self, vector: Vector2, epsilon: float) -> bool:
        """
        Check for approximate vector equality

        >>> Vector2(1, 0).equals_approximately(Vector2(1, 0.0000001), 0.000001)
        True
        >>> Vector2(1.23, 4.56).equals_approximately(Vector2(1.24, 4.56), 0.000001)
        False
        """

        return abs(self.x - vector.x) < epsilon and abs(self.y - vector.y) < epsilon

    def length(self) -> float:
        """
        Vector length

        >>> Vector2(1, 0).length() == 1
        True
        >>> Vector2(-1, 1).length() == math.sqrt(2)
        True
        """

        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self) -> Vector2:
        """
        Normalization sets the vector to length 1 while maintaining its direction

        >>> Vector2(1, 0).normalize().equals_approximately(Vector2(1, 0), 0.000001)
        True
        >>> Vector2(1, -1).normalize().equals_approximately(Vector2(math.sqrt(2) / 2,
        ... -math.sqrt(2) / 2), 0.000001)
        True
        """
        length = self.length()
        if length == 0:
            raise Exception("Cannot normalize vectors of length 0")
        return Vector2(self.x / length, self.y / length)

    def add(self, vector: Vector2) -> Vector2:
        """
        Vector addition

        >>> Vector2(1, 0).add(Vector2(0, 1)).equals_approximately(Vector2(1, 1),
        ... 0.000001)
        True
        >>> Vector2(-3.3, -9).add(Vector2(-2.2, 3)).equals_approximately(Vector2(-5.5,
        ... -6), 0.000001)
        True
        """
        x = self.x + vector.x
        y = self.y + vector.y
        return Vector2(x, y)

    def subtract(self, vector: Vector2) -> Vector2:
        """
        Vector subtraction

        >>> Vector2(1, 0).subtract(Vector2(0, 1)).equals_approximately(Vector2(1,
        ... -1), 0.000001)
        True
        >>> Vector2(234.5, 1.7).subtract(Vector2(3.3, 2.7)).equals_approximately(
        ... Vector2(231.2, -1), 0.000001)
        True
        """
        x = self.x - vector.x
        y = self.y - vector.y
        return Vector2(x, y)

    def multiply(self, scalar: float) -> Vector2:
        """
        Vector scalar multiplication

        >>> Vector2(1, 0).multiply(5).equals_approximately(Vector2(5, 0), 0.000001)
        True
        >>> Vector2(3.41, -7.12).multiply(-3.1).equals_approximately(Vector2(-10.571,
        ... 22.072), 0.000001)
        True
        """
        x = self.x * scalar
        y = self.y * scalar
        return Vector2(x, y)

    def distance(self, vector: Vector2) -> float:
        """
        Distance between this vector and another vector

        >>> Vector2(0, 0).distance(Vector2(0, -1)) == 1
        True
        >>> Vector2(1, 0).distance(Vector2(0, 1)) == math.sqrt(2)
        True
        """
        difference = vector.subtract(self)
        return difference.length()

    def dot_product(self, vector: Vector2) -> float:
        """
        Vector dot product

        >>> Vector2(1, 0).dot_product(Vector2(0, 1)) == 0
        True
        >>> Vector2(1, 2).dot_product(Vector2(3, 4)) == 1 * 3 + 2 * 4
        True
        """
        return self.x * vector.x + self.y * vector.y

    def rotate(self, angle_in_radians: float) -> Vector2:
        """
        Vector rotation (see https://en.wikipedia.org/wiki/Rotation_matrix)

        >>> Vector2(0, -1).rotate(math.pi / 2).equals_approximately(Vector2(1,
        ... 0), 0.000001)
        True
        >>> Vector2(1.23, -4.56).rotate(math.pi).equals_approximately(Vector2(-1.23,
        ... 4.56), 0.000001)
        True
        """
        ca = math.cos(angle_in_radians)
        sa = math.sin(angle_in_radians)
        x = ca * self.x - sa * self.y
        y = sa * self.x + ca * self.y
        return Vector2(x, y)

    def angle_between(self, vector: Vector2) -> float:
        """
        Measure angle between two vectors

        >>> Vector2(1, 0).angle_between(Vector2(0, 1)) == math.pi / 2
        True
        >>> Vector2(1, 0).angle_between(Vector2(1, -1)) == -math.pi / 4
        True
        """
        return math.atan2(vector.y, vector.x) - math.atan2(self.y, self.x)
