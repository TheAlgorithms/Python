"""
Ramer-Douglas-Peucker (RDP) algorithm for polyline simplification.

Given a curve represented as a sequence of points and a tolerance epsilon,
the algorithm recursively reduces the number of points while preserving the
overall shape of the curve. Points that deviate from the simplified line by
less than epsilon are removed.

Time complexity:  O(n log n) on average, O(n²) worst case
Space complexity: O(n) for the recursion stack

References:
- https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
- Ramer, U. (1972). "An iterative procedure for the polygonal approximation
  of plane curves". Computer Graphics and Image Processing. 1 (3): 244-256.
- Douglas, D.; Peucker, T. (1973). "Algorithms for the reduction of the number
  of points required to represent a digitized line or its caricature".
  Cartographica. 10 (2): 112-122.
"""

from __future__ import annotations

import math
from collections.abc import Sequence

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _euclidean_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Return the Euclidean distance between two 2-D points.

    >>> _euclidean_distance((0.0, 0.0), (3.0, 4.0))
    5.0
    >>> _euclidean_distance((1.0, 1.0), (1.0, 1.0))
    0.0
    """
    return math.hypot(b[0] - a[0], b[1] - a[1])


def _perpendicular_distance(
    p: tuple[float, float],
    a: tuple[float, float],
    b: tuple[float, float],
) -> float:
    """Return the perpendicular distance from point *p* to the line through *a* and *b*.

    The result is the absolute value of the signed area of the triangle (a, b, p)
    divided by the length of segment ab, which equals the altitude of that triangle
    from p.

    >>> _perpendicular_distance((4.0, 0.0), (0.0, 0.0), (0.0, 3.0))
    4.0
    >>> _perpendicular_distance((4.0, 0.0), (0.0, 0.0), (0.0, 3.0))
    4.0
    >>> # order of a and b does not affect the result
    >>> _perpendicular_distance((4.0, 0.0), (0.0, 3.0), (0.0, 0.0))
    4.0
    >>> _perpendicular_distance((4.0, 1.0), (0.0, 1.0), (0.0, 4.0))
    4.0
    >>> _perpendicular_distance((2.0, 1.0), (-2.0, 1.0), (-2.0, 4.0))
    4.0
    """
    px, py = p
    ax, ay = a
    bx, by = b
    numerator = abs((by - ay) * px - (bx - ax) * py + bx * ay - by * ax)
    denominator = _euclidean_distance(a, b)
    if denominator == 0.0:
        # a and b coincide; fall back to point-to-point distance
        return _euclidean_distance(p, a)
    return numerator / denominator


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def ramer_douglas_peucker(
    points: Sequence[tuple[float, float]],
    epsilon: float,
) -> list[tuple[float, float]]:
    """Simplify a polyline using the Ramer-Douglas-Peucker algorithm.

    Parameters
    ----------
    points:
        An ordered sequence of ``(x, y)`` tuples that form the polyline.
    epsilon:
        Maximum allowable perpendicular deviation.  Points whose distance
        to the simplified segment is less than or equal to *epsilon* are
        discarded.  Must be non-negative.

    Returns
    -------
    list[tuple[float, float]]
        A simplified list of ``(x, y)`` points that is a subset of *points*.

    Raises
    ------
    ValueError
        If *epsilon* is negative.

    Examples
    --------
    Collinear points - middle point is redundant for any positive epsilon:

    >>> ramer_douglas_peucker([(0.0, 0.0), (1.0, 0.0), (2.0, 0.0)], epsilon=0.5)
    [(0.0, 0.0), (2.0, 0.0)]

    Empty / tiny inputs are returned unchanged:

    >>> ramer_douglas_peucker([], epsilon=1.0)
    []
    >>> ramer_douglas_peucker([(0.0, 0.0)], epsilon=1.0)
    [(0.0, 0.0)]
    >>> ramer_douglas_peucker([(0.0, 0.0), (1.0, 1.0)], epsilon=1.0)
    [(0.0, 0.0), (1.0, 1.0)]

    A simple square outline where epsilon removes mid-edge points:

    >>> square = [
    ...     (0.0, 0.0), (1.0, 0.0), (2.0, 0.0),
    ...     (2.0, 1.0), (2.0, 2.0), (1.0, 2.0),
    ...     (0.0, 2.0), (0.0, 1.0),
    ... ]
    >>> ramer_douglas_peucker(square, epsilon=0.7)
    [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (0.0, 2.0), (0.0, 1.0)]

    A polygonal chain simplified to a single segment for large epsilon:

    >>> chain = [(0.0, 0.0), (2.0, 0.5), (3.0, 3.0), (6.0, 3.0), (8.0, 4.0)]
    >>> ramer_douglas_peucker(chain, epsilon=3.0)
    [(0.0, 0.0), (8.0, 4.0)]

    Zero epsilon keeps all points:

    >>> ramer_douglas_peucker([(0.0, 0.0), (0.5, 0.1), (1.0, 0.0)], epsilon=0.0)
    [(0.0, 0.0), (0.5, 0.1), (1.0, 0.0)]
    """
    if epsilon < 0:
        msg = f"epsilon must be non-negative, got {epsilon!r}"
        raise ValueError(msg)

    pts = list(points)

    if len(pts) < 3:
        return pts

    # Find the point with the greatest perpendicular distance from the line
    # connecting the first and last points.
    start, end = pts[0], pts[-1]
    max_dist = 0.0
    max_index = 0
    for i in range(1, len(pts) - 1):
        dist = _perpendicular_distance(pts[i], start, end)
        if dist > max_dist:
            max_dist = dist
            max_index = i

    if max_dist > epsilon:
        # Recursively simplify both halves and join them (drop the duplicate
        # point at the junction).
        left = ramer_douglas_peucker(pts[: max_index + 1], epsilon)
        right = ramer_douglas_peucker(pts[max_index:], epsilon)
        return left[:-1] + right

    # All intermediate points are within tolerance - keep only the endpoints.
    return [start, end]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
