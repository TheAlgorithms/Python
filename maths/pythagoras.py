"""Uses Pythagoras theorem to calculate the distance between two points in space."""

import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"


def distance(a: Point, b: Point) -> float:
    """
    >>> point1 = Point(2, -1, 7)
    >>> point2 = Point(1, -3, 5)
    >>> print(f"Distance from {point1} to {point2} is {distance(point1, point2)}")
    Distance from Point(2, -1, 7) to Point(1, -3, 5) is 3.0
    """
    return math.sqrt(abs((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
