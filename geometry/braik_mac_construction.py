from __future__ import annotations

from dataclasses import dataclass, field

from numpy import array, linalg

# braikenridge_maclaurin_construction
# https://mathworld.wolfram.com/ConicSection.html
# 5 Points define a conic section on a 2D normal
# orthogonal plane using this technique


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
class BraikMac:
    """
    Given a list of 5 points, determine the corresponding
    conic section equation and provide it to the user

    | x**2   xy  y**2  x  y  1 |
    | x1**2 x1y1 y1**2 x1 y1 1 |
    | x2**2 x2y2 y2**2 x2 y2 1 | = 0
    | x3**2 x3y3 y3**2 x3 y3 1 |
    | x4**2 x4y4 y4**2 x4 y4 1 |
    | x5**2 x5y5 y5**2 x5 y5 1 |

    >>> p1 = Point(0.0,0.0)
    >>> p2 = Point(5.0,0.0)
    >>> p3 = Point(2.0,3.0)
    >>> p4 = Point(1.0,10.0)
    >>> p5 = Point(6.0,7.0)
    >>> BraikMac([p1,p2,p3,p4,p5]) # doctest: +NORMALIZE_WHITESPACE
    BraikMac(p_list=[Point(x=0.0, y=0.0), Point(x=5.0, y=0.0),
    Point(x=2.0, y=3.0), Point(x=1.0, y=10.0), Point(x=6.0, y=7.0)])
    """

    p_list: list[Point] = field(default_factory=list)

    def __post_init__(self) -> None:
        n = 0
        for p in self.p_list:
            if not isinstance(p, Point):
                raise TypeError("Array must be point objects.")
            n += 1
        if n != 5:
            raise TypeError("Array must be 5 point objects.")

    @property
    def generate(self) -> None:
        x1 = self.p_list[0].x
        y1 = self.p_list[0].y
        x2 = self.p_list[1].x
        y2 = self.p_list[1].y
        x3 = self.p_list[2].x
        y3 = self.p_list[2].y
        x4 = self.p_list[3].x
        y4 = self.p_list[3].y
        x5 = self.p_list[4].x
        y5 = self.p_list[4].y

        x2_matrix = array(
            [
                [x1 * y1, y1**2, x1, y1, 1],
                [x2 * y2, y2**2, x2, y2, 1],
                [x3 * y3, y3**2, x3, y3, 1],
                [x4 * y4, y4**2, x4, y4, 1],
                [x5 * y5, y5**2, x5, y5, 1],
            ]
        )

        a = linalg.det(x2_matrix)

        xy_matrix = array(
            [
                [x1**2, y1**2, x1, y1, 1],
                [x2**2, y2**2, x2, y2, 1],
                [x3**2, y3**2, x3, y3, 1],
                [x4**2, y4**2, x4, y4, 1],
                [x5**2, y5**2, x5, y5, 1],
            ]
        )

        b = -linalg.det(xy_matrix)

        y2_matrix = array(
            [
                [x1**2, x1 * y1, x1, y1, 1],
                [x2**2, x2 * y2, x2, y2, 1],
                [x3**2, x3 * y3, x3, y3, 1],
                [x4**2, x4 * y4, x4, y4, 1],
                [x5**2, x5 * y5, x5, y5, 1],
            ]
        )

        c = linalg.det(y2_matrix)

        x_matrix = array(
            [
                [x1**2, x1 * y1, y1**2, y1, 1],
                [x2**2, x2 * y2, y2**2, y2, 1],
                [x3**2, x3 * y3, y3**2, y3, 1],
                [x4**2, x4 * y4, y4**2, y4, 1],
                [x5**2, x5 * y5, y5**2, y5, 1],
            ]
        )

        d = -linalg.det(x_matrix)

        y_matrix = array(
            [
                [x1**2, x1 * y1, y1**2, x1, 1],
                [x2**2, x2 * y2, y2**2, x2, 1],
                [x3**2, x3 * y3, y3**2, x3, 1],
                [x4**2, x4 * y4, y4**2, x4, 1],
                [x5**2, x5 * y5, y5**2, x5, 1],
            ]
        )

        e = linalg.det(y_matrix)

        const_matrix = array(
            [
                [x1**2, x1 * y1, y1**2, x1, y1],
                [x2**2, x2 * y2, y2**2, x2, y2],
                [x3**2, x3 * y3, y3**2, x3, y3],
                [x4**2, x4 * y4, y4**2, x4, y4],
                [x5**2, x5 * y5, y5**2, x5, y5],
            ]
        )

        f = -linalg.det(const_matrix)

        s = f"0 = {a:+.2} X**2 {b:+.2} XY {c:+.2} Y**2 {d:+.2} X {e:+.2} Y {f:+.2}"
        print(s)
