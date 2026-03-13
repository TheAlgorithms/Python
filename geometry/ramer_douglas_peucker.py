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


def _euclidean_distance(
    point_1: tuple[float, float], point_2: tuple[float, float]
) -> float:
    """Return the Euclidean distance between two 2-D points.

    >>> _euclidean_distance((0.0, 0.0), (3.0, 4.0))
    5.0
    >>> _euclidean_distance((1.0, 1.0), (1.0, 1.0))
    0.0
    """
    return math.hypot(point_2[0] - point_1[0], point_2[1] - point_1[1])


def _perpendicular_distance(
    point: tuple[float, float],
    line_start: tuple[float, float],
    line_end: tuple[float, float],
) -> float:
    """Return the perpendicular distance from *point* to the line through
    *line_start* and *line_end*.

    The result is the absolute value of the signed area of the triangle
    (line_start, line_end, point) divided by the length of the segment, which
    equals the altitude of that triangle from point.

    >>> _perpendicular_distance((4.0, 0.0), (0.0, 0.0), (0.0, 3.0))
    4.0
    >>> # order of line_start and line_end does not affect the result
    >>> _perpendicular_distance((4.0, 0.0), (0.0, 3.0), (0.0, 0.0))
    4.0
    >>> _perpendicular_distance((4.0, 1.0), (0.0, 1.0), (0.0, 4.0))
    4.0
    >>> _perpendicular_distance((2.0, 1.0), (-2.0, 1.0), (-2.0, 4.0))
    4.0
    """
    px, py = point
    ax, ay = line_start
    bx, by = line_end
    numerator = abs((by - ay) * px - (bx - ax) * py + bx * ay - by * ax)
    denominator = _euclidean_distance(line_start, line_end)
    if denominator == 0.0:
        # line_start and line_end coincide; fall back to point-to-point distance
        return _euclidean_distance(point, line_start)
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
