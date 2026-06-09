"""
Ramer-Douglas-Peucker polyline simplification algorithm.

Given a sequence of 2-D points and a tolerance epsilon, the algorithm
reduces the number of points while preserving the overall shape of the curve.

Time complexity:  O(n log n) average, O(n²) worst case
Space complexity: O(n)

References:
    https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
"""

from __future__ import annotations

import math


def _euclidean_distance(
    point_a: tuple[float, float],
    point_b: tuple[float, float],
) -> float:
    """Return the Euclidean distance between two 2-D points.

    >>> _euclidean_distance((0.0, 0.0), (3.0, 4.0))
    5.0
    >>> _euclidean_distance((1.0, 1.0), (1.0, 1.0))
    0.0
    """
    return math.hypot(point_b[0] - point_a[0], point_b[1] - point_a[1])


def _perpendicular_distance(
    point: tuple[float, float],
    line_start: tuple[float, float],
    line_end: tuple[float, float],
) -> float:
    """Return the distance from *point* to the line **segment** between
    *line_start* and *line_end*.

    When the perpendicular projection of *point* onto the infinite line falls
    within the segment, this equals the perpendicular distance to that line.
    When the projection falls outside the segment, the distance to the nearest
    endpoint is returned instead (projection clamped to [0, 1]).

    This is the correct distance measure for the Ramer-Douglas-Peucker
    algorithm: using the infinite-line distance can incorrectly discard points
    whose projection lies beyond a segment endpoint.

    >>> _perpendicular_distance((4.0, 0.0), (0.0, 0.0), (0.0, 3.0))
    4.0
    >>> # order of line_start and line_end does not affect the result
    >>> _perpendicular_distance((4.0, 0.0), (0.0, 3.0), (0.0, 0.0))
    4.0
    >>> _perpendicular_distance((4.0, 1.0), (0.0, 1.0), (0.0, 4.0))
    4.0
    >>> _perpendicular_distance((2.0, 1.0), (-2.0, 1.0), (-2.0, 4.0))
    4.0
    >>> # projection falls outside the segment; distance to nearest endpoint
    >>> round(_perpendicular_distance((0.0, 2.0), (1.0, 0.0), (3.0, 0.0)), 6)
    2.236068
    """
    px, py = point
    ax, ay = line_start
    bx, by = line_end
    dx, dy = bx - ax, by - ay
    seg_len_sq = dx * dx + dy * dy
    if seg_len_sq == 0.0:
        # line_start and line_end coincide; fall back to point-to-point distance
        return _euclidean_distance(point, line_start)
    # Project point onto the segment line, then clamp t to [0, 1] so the
    # nearest point is always on the segment rather than the infinite line.
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / seg_len_sq))
    nearest_x = ax + t * dx
    nearest_y = ay + t * dy
    return math.hypot(px - nearest_x, py - nearest_y)


def ramer_douglas_peucker(
    pts: list[tuple[float, float]],
    epsilon: float,
) -> list[tuple[float, float]]:
    """Simplify a polyline using the Ramer-Douglas-Peucker algorithm.

    Given a sequence of 2-D points and a maximum allowable deviation
    *epsilon* (>= 0), returns a simplified list of points such that no
    discarded point is farther than *epsilon* from the simplified polyline.

    Parameters
    ----------
    pts:
        Ordered sequence of ``(x, y)`` points describing the polyline.
    epsilon:
        Maximum allowable distance of any discarded point from the
        simplified polyline.  Must be non-negative.

    Returns
    -------
    list[tuple[float, float]]
        Simplified list of ``(x, y)`` points.  The first and last points of
        *pts* are always preserved.

    Raises
    ------
    ValueError
        If *epsilon* is negative.

    References
    ----------
    https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm

    Examples
    --------
    >>> ramer_douglas_peucker([], epsilon=1.0)
    []
    >>> ramer_douglas_peucker([(0.0, 0.0)], epsilon=1.0)
    [(0.0, 0.0)]
    >>> ramer_douglas_peucker([(0.0, 0.0), (1.0, 0.0)], epsilon=1.0)
    [(0.0, 0.0), (1.0, 0.0)]
    >>> # middle point is within epsilon - it is discarded
    >>> ramer_douglas_peucker([(0.0, 0.0), (1.0, 0.1), (2.0, 0.0)], epsilon=0.5)
    [(0.0, 0.0), (2.0, 0.0)]
    >>> # middle point exceeds epsilon - it is kept
    >>> ramer_douglas_peucker([(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)], epsilon=0.5)
    [(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)]
    >>> ramer_douglas_peucker([(0.0, 0.0), (1.0, 0.5), (2.0, 0.0)], epsilon=-1.0)
    Traceback (most recent call last):
        ...
    ValueError: epsilon must be non-negative, got -1.0
    """
    if epsilon < 0:
        msg = f"epsilon must be non-negative, got {epsilon!r}"
        raise ValueError(msg)

    if len(pts) < 3:
        return list(pts)

    # ---------------------------------------------------------------------------
    # Iterative, stack-based implementation.
    #
    # The naive recursive approach copies sublists at every level via slicing
    # (pts[:max_index+1] / pts[max_index:]), which is O(n) per call and makes
    # the overall algorithm O(n²) in memory even for well-balanced splits.  An
    # explicit stack operating on index ranges avoids all copying and also
    # eliminates the risk of hitting Python's recursion limit for long polylines.
    # ---------------------------------------------------------------------------
    n = len(pts)

    # keep[i] is True when pts[i] must appear in the output.
    keep: list[bool] = [False] * n
    keep[0] = True
    keep[-1] = True

    # Stack of (start_index, end_index) pairs still to be examined.
    stack: list[tuple[int, int]] = [(0, n - 1)]

    while stack:
        start, end = stack.pop()
        if end - start < 2:
            # Only one interior candidate at most; nothing to split further.
            continue

        # Find the interior point with the greatest distance to the segment.
        max_dist = 0.0
        max_index = start
        for i in range(start + 1, end):
            dist = _perpendicular_distance(pts[i], pts[start], pts[end])
            if dist > max_dist:
                max_dist = dist
                max_index = i

        if max_dist > epsilon:
            keep[max_index] = True
            stack.append((start, max_index))
            stack.append((max_index, end))
        # else: all interior points are within epsilon; discard them all.

    return [pts[i] for i in range(n) if keep[i]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
