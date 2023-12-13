from __future__ import annotations

import math
from dataclasses import dataclass, field

# polar_coordinates
# convert from normal, orthogonal coordinates
# to polar coordinates.  Can be a list of
# points or a singular point
# https://mathworld.wolfram.com/PolarCoordinates.html


@dataclass
class Point:
    """
    A point on an orthogonal unit cartesian plane

    >>> Point(2.0,4.0)
    Point(x=2.0, y=4.0)
    """

    x: float = 0.0
    y: float = 0.0

    def __post_init__(self) -> None:
        if not isinstance(self.x, (float, int)):
            raise TypeError("x must be a numeric values.")
        if not isinstance(self.y, (float, int)):
            raise TypeError("y must be a numeric values.")


@dataclass
class ConvertPolar:
    """
    Basic conversion of a list of points to polar (r,theta) coordinates

    >>> p1 = Point(2.0,4.0)
    >>> p2 = Point(1.0,-2.0)
    >>> p3 = Point(-1.0,1.0)
    >>> ConvertPolar([p1,p2,p3]) # doctest: +NORMALIZE_WHITESPACE
    ConvertPolar(points=[Point(x=2.0, y=4.0),
    Point(x=1.0, y=-2.0), Point(x=-1.0, y=1.0)])
    """

    points: list[Point] = field(default_factory=list)

    def __post_init__(self) -> None:
        for i in self.points:
            if not isinstance(i, Point):
                raise TypeError("vector must be a list of Point Objects.")

    @property
    def convert_points(self) -> None:
        for i in self.points:
            r = math.sqrt(i.x**2 + i.y**2)
            theta = math.atan2(i.y, i.x)
            s = f"r = {r:.2}, theta = {theta:.2}"
            print(s)
