from __future__ import annotations

import math
from dataclasses import dataclass, field

from numpy import array, linalg

# Define a Point on a 2D normalized orthogonal euclidean grid
# https://mathworld.wolfram.com/Circumcenter.html
# https://mathworld.wolfram.com/Incenter.html
# https://mathworld.wolfram.com/Orthocenter.html


@dataclass
class Point:
    """
    A point defined by 2 floats representing a length on a normalized
    orthogonal coordinate system
    default coordinate is the origin

    >>> Point(-1.0, 0.0)
    Point(x=-1.0, y=0.0)

    """

    x: float = 0.0
    y: float = 0.0

    def __post_init__(self) -> None:
        if not isinstance(self.x, (int, float)):
            raise TypeError("x must be an int or float numeric value")
        if not isinstance(self.y, (int, float)):
            raise TypeError("y must be an int or float numeric value")


@dataclass
class Triangle:
    """
    A 3 point Triangle on a 2D normalized orthogonal euclidean grid

    >>> p1 = Point(-1.0,0.0)
    >>> p2 = Point(1.0,0.0)
    >>> p3 = Point(0.0,1.0)
    >>> Triangle(p1, p2, p3) # doctest: +NORMALIZE_WHITESPACE
    Triangle(v1=Point(x=-1.0, y=0.0), v2=Point(x=1.0, y=0.0), v3=Point(x=0.0, y=1.0),
    circum=Point(x=0.0, y=0.0), incen=Point(x=0.0, y=0.0),
    ortho=Point(x=0.0, y=0.0))
    """

    v1: Point = field(default_factory=Point)
    v2: Point = field(default_factory=Point)
    v3: Point = field(default_factory=Point)
    circum: Point = field(default_factory=Point)
    incen: Point = field(default_factory=Point)
    ortho: Point = field(default_factory=Point)

    def __post_init__(self) -> None:
        # Check for valid arguments
        if (
            not isinstance(self.v1, Point)
            or not isinstance(self.v2, Point)
            or not isinstance(self.v3, Point)
        ):
            raise TypeError("All 3 arguments should be Point Objects")
        # Check for 3 unique points
        if self.v1 in (self.v2, self.v3):
            raise TypeError("All 3 arguments should be unique")
        # Check for linearity
        if self.v1.x == self.v2.x:
            if self.v3.y == self.v2.y:
                raise TypeError("One or more arguments are redundant")
        m = (self.v1.y - self.v2.y) / (self.v1.x - self.v2.x)
        yb = self.v1.y - m * self.v1.x
        if self.v3.y == m * self.v3.x + yb:
            raise TypeError("One or more arguments are redundant")

    # Circumcenter
    @property
    def circumcenter(self) -> Point:
        m_0 = array(
            [
                [self.v1.x, self.v1.y, 1],
                [self.v2.x, self.v2.y, 1],
                [self.v3.x, self.v3.y, 1],
            ]
        )
        m_1 = array(
            [
                [self.v1.x**2 + self.v1.y**2, self.v1.y, 1],
                [self.v2.x**2 + self.v2.y**2, self.v2.y, 1],
                [self.v3.x**2 + self.v3.y**2, self.v3.y, 1],
            ]
        )
        m_2 = array(
            [
                [self.v1.x**2 + self.v1.y**2, self.v1.x, 1],
                [self.v2.x**2 + self.v2.y**2, self.v2.x, 1],
                [self.v3.x**2 + self.v3.y**2, self.v3.x, 1],
            ]
        )
        a = linalg.det(m_0)
        bx = -linalg.det(m_1)
        by = linalg.det(m_2)
        self.circum.x = -bx / (2 * a)
        self.circum.y = -by / (2 * a)
        return self.circum

    # Incenter
    @property
    def incenter(self) -> Point:
        a = math.sqrt((self.v2.x - self.v3.x) ** 2 + (self.v2.y - self.v3.y) ** 2)
        b = math.sqrt((self.v1.x - self.v3.x) ** 2 + (self.v1.y - self.v3.y) ** 2)
        c = math.sqrt((self.v1.x - self.v2.x) ** 2 + (self.v1.y - self.v2.y) ** 2)
        self.incen.x = (a * self.v1.x + b * self.v2.x + c * self.v3.x) / (a + b + c)
        self.incen.y = (a * self.v1.y + b * self.v2.y + c * self.v3.y) / (a + b + c)
        return self.incen

    # Orthocenter
    @property
    def orthocenter(self) -> Point:
        inv_m1 = -1 / ((self.v3.y - self.v1.y) / (self.v3.x - self.v1.x))
        inv_m2 = -1 / ((self.v3.y - self.v2.y) / (self.v3.x - self.v2.x))
        m = array([[inv_m2, -1], [inv_m1, -1]])
        b = array([[inv_m2 * self.v1.x - self.v1.y], [inv_m1 * self.v2.x - self.v2.y]])
        soln = linalg.solve(m, b)
        self.ortho.x = soln[0][0]
        self.ortho.y = soln[1][0]
        return self.ortho


if __name__ == "__main__":
    __import__("doctest").testmod()
