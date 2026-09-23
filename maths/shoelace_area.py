"""
Shoelace formula (Gauss's area formula) for polygon area.

The function accepts an iterable of (x, y) pairs and returns the polygon area
as a non-negative float.

References:
- https://en.wikipedia.org/wiki/Shoelace_formula
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence


def shoelace_area(points: Iterable[tuple[float, float]]) -> float:
    """
    Compute the area of a simple polygon using the shoelace formula.

    Parameters
    ----------
    points:
        Iterable of (x, y) coordinate pairs. Points may be ints or floats.
        The polygon is assumed closed (the function will wrap the last point
        to the first).

    Returns
    -------
    float
        Non-negative area of the polygon.

    Raises
    ------
    ValueError
        If fewer than 3 points are provided.
    TypeError
        If points are not pairs of numbers.

    Examples
    >>> shoelace_area([(0, 0), (4, 0), (0, 3)])
    6.0
    >>> shoelace_area([(0, 0), (1, 0), (1, 1), (0, 1)])
    1.0
    >>> shoelace_area(list(reversed([(0, 0), (2, 0), (2, 2), (0, 2)])))
    4.0
    >>> shoelace_area([(0, 0), (2, 0), (2, 2), (0, 2)])
    4.0
    """
    pts = list(points)
    n = len(pts)
    if n < 3:
        raise ValueError("At least 3 points are required to form a polygon")

    try:
        coords: Sequence[tuple[float, float]] = [(float(x), float(y)) for x, y in pts]
    except Exception as exc:
        raise TypeError("points must be an iterable of (x, y) numeric pairs") from exc

    s = 0.0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        s += x1 * y2 - x2 * y1

    return abs(s) / 2.0


if __name__ == "__main__":
    example = [(0, 0), (4, 0), (0, 3)]
    print("example area:", shoelace_area(example))
