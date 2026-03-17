"""
Given two line segments, determine whether they intersect.

This is based on the algorithm described in Introduction to Algorithms
(CLRS), Chapter 33.

Reference:
    - https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    - https://en.wikipedia.org/wiki/Orientation_(geometry)
"""

from __future__ import annotations

from typing import NamedTuple


class Point(NamedTuple):
    """A point in 2D space.

    >>> Point(0, 0)
    Point(x=0, y=0)
    >>> Point(1, -3)
    Point(x=1, y=-3)
    """

    x: float
    y: float


def direction(a: Point, b: Point, c: Point) -> float:
    """Return the cross product of vectors (a→c) and (a→b).

    The sign of the result encodes the orientation of the ordered triple
    (a, b, c):
      - Negative  →  counter-clockwise (left turn)
      - Positive  →  clockwise (right turn)
      - Zero      →  collinear

    >>> direction(Point(0, 0), Point(1, 0), Point(0, 1))
    -1
    >>> direction(Point(0, 0), Point(0, 1), Point(1, 0))
    1
    >>> direction(Point(0, 0), Point(1, 1), Point(2, 2))
    0
    """
    return (c.x - a.x) * (b.y - a.y) - (b.x - a.x) * (c.y - a.y)


def on_segment(a: Point, b: Point, p: Point) -> bool:
    """Check whether point *p*, known to be collinear with segment ab, lies on it.

    >>> on_segment(Point(0, 0), Point(4, 4), Point(2, 2))
    True
    >>> on_segment(Point(0, 0), Point(4, 4), Point(5, 5))
    False
    >>> on_segment(Point(0, 0), Point(4, 0), Point(2, 0))
    True
    """
    return min(a.x, b.x) <= p.x <= max(a.x, b.x) and min(a.y, b.y) <= p.y <= max(
        a.y, b.y
    )


def segments_intersect(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    """Return True if line segment p1p2 intersects line segment p3p4.

    Uses the CLRS cross-product / orientation method.  Handles both the
    general case (proper crossing) and degenerate cases where one endpoint
    lies exactly on the other segment.

    >>> segments_intersect(Point(0, 0), Point(2, 2), Point(0, 2), Point(2, 0))
    True
    >>> segments_intersect(Point(0, 0), Point(2, 2), Point(1, 1), Point(3, 3))
    True
    >>> segments_intersect(Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0))
    False
    >>> segments_intersect(Point(0, 0), Point(1, 1), Point(1, 0), Point(2, 1))
    False
    >>> segments_intersect(Point(0, 0), Point(1, 1), Point(0, 1), Point(0, 2))
    False
    >>> segments_intersect(Point(0, 0), Point(1, 0), Point(1, 0), Point(2, 0))
    True
    """
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)

    if ((d1 < 0 < d2) or (d2 < 0 < d1)) and ((d3 < 0 < d4) or (d4 < 0 < d3)):
        return True

    if d1 == 0 and on_segment(p3, p4, p1):
        return True
    if d2 == 0 and on_segment(p3, p4, p2):
        return True
    if d3 == 0 and on_segment(p1, p2, p3):
        return True
    return d4 == 0 and on_segment(p1, p2, p4)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Enter four points as 'x y' pairs (one per line):")
    points = [Point(*map(float, input().split())) for _ in range(4)]
    p1, p2, p3, p4 = points
    result = segments_intersect(p1, p2, p3, p4)
    print(1 if result else 0)
