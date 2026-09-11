"""
Rotating Calipers Algorithm for Convex Polygon Diameter.

References:
- https://en.wikipedia.org/wiki/Rotating_calipers
- https://cp-algorithms.com/geometry/convex-hull-kernel.html
- Toussaint, G. T. (1983). "Solving geometric problems with the rotating calipers".
  Proceedings of IEEE MELECON '83, Athens, Greece.

The rotating calipers paradigm allows computing the diameter (the maximum Euclidean
distance between any pair of points) of a set of 2D points in O(n log n) time
(O(n log n) for the convex hull and O(n) for the calipers sweep).
"""

from __future__ import annotations

import math

Point = tuple[float, float]


def cross_product(origin: Point, point_a: Point, point_b: Point) -> float:
    """
    Compute the 2D cross product of vectors (origin -> point_a) and (origin -> point_b).

    The return value represents twice the signed area of triangle
    (origin, point_a, point_b):
        > 0 : Counter-clockwise turn (left turn)
        < 0 : Clockwise turn (right turn)
        = 0 : Collinear points

    >>> cross_product((0.0, 0.0), (1.0, 0.0), (1.0, 1.0))
    1.0
    >>> cross_product((0.0, 0.0), (1.0, 1.0), (1.0, 0.0))
    -1.0
    >>> cross_product((0.0, 0.0), (1.0, 1.0), (2.0, 2.0))
    0.0
    """
    return (point_a[0] - origin[0]) * (point_b[1] - origin[1]) - (
        point_a[1] - origin[1]
    ) * (point_b[0] - origin[0])


def distance_squared(point_a: Point, point_b: Point) -> float:
    """
    Compute the squared Euclidean distance between point_a and point_b.

    >>> distance_squared((0.0, 0.0), (3.0, 4.0))
    25.0
    >>> distance_squared((1.0, 1.0), (1.0, 1.0))
    0.0
    >>> distance_squared((-1.0, -1.0), (2.0, 3.0))
    25.0
    """
    return (point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2


def convex_hull(points: list[Point]) -> list[Point]:
    """
    Compute the convex hull of a set of 2D points in counter-clockwise order
    using Andrew's monotone chain algorithm.

    Time Complexity: O(n log n) where n is the number of points.
    Space Complexity: O(n)

    >>> convex_hull([(0.0, 0.0), (1.0, 1.0)])
    [(0.0, 0.0), (1.0, 1.0)]
    >>> convex_hull([(0.0, 0.0), (3.0, 0.0), (3.0, 3.0), (0.0, 3.0), (1.0, 1.0)])
    [(0.0, 0.0), (3.0, 0.0), (3.0, 3.0), (0.0, 3.0)]
    >>> convex_hull([(0.0, 0.0), (1.0, 1.0), (2.0, 2.0)])
    [(0.0, 0.0), (2.0, 2.0)]
    >>> convex_hull([(1.0, 1.0)])
    [(1.0, 1.0)]
    """
    unique_points = sorted(set(points))
    if len(unique_points) <= 1:
        return unique_points

    lower_hull: list[Point] = []
    for candidate_point in unique_points:
        while (
            len(lower_hull) >= 2
            and cross_product(lower_hull[-2], lower_hull[-1], candidate_point) <= 0.0
        ):
            lower_hull.pop()
        lower_hull.append(candidate_point)

    upper_hull: list[Point] = []
    for candidate_point in reversed(unique_points):
        while (
            len(upper_hull) >= 2
            and cross_product(upper_hull[-2], upper_hull[-1], candidate_point) <= 0.0
        ):
            upper_hull.pop()
        upper_hull.append(candidate_point)

    return lower_hull[:-1] + upper_hull[:-1]


def rotating_calipers(points: list[Point]) -> tuple[float, tuple[Point, Point]]:
    """
    Find the maximum Euclidean distance (polygon diameter) and an antipodal pair
    of points for a given set of 2D points using the rotating calipers algorithm.

    Time Complexity: O(n log n) for convex hull construction
        + O(n) for the calipers sweep.
    Space Complexity: O(n) for the convex hull.

    Raises:
        ValueError: If fewer than 2 points are provided.

    >>> points = [(0.0, 0.0), (3.0, 0.0), (3.0, 4.0), (0.0, 4.0)]
    >>> max_dist, pair = rotating_calipers(points)
    >>> max_dist
    5.0
    >>> pair in [
    ...     ((0.0, 0.0), (3.0, 4.0)),
    ...     ((3.0, 4.0), (0.0, 0.0)),
    ...     ((3.0, 0.0), (0.0, 4.0)),
    ...     ((0.0, 4.0), (3.0, 0.0)),
    ... ]
    True
    >>> rotating_calipers([(0.0, 0.0), (0.0, 5.0)])
    (5.0, ((0.0, 0.0), (0.0, 5.0)))
    >>> rotating_calipers([(1.0, 1.0), (1.0, 1.0)])
    (0.0, ((1.0, 1.0), (1.0, 1.0)))
    >>> rotating_calipers([(0.0, 0.0), (1.0, 1.0), (2.0, 2.0), (3.0, 3.0)])[0]
    4.242640687119285
    >>> rotating_calipers([(1.0, 1.0)])
    Traceback (most recent call last):
        ...
    ValueError: At least 2 points are required to compute polygon diameter.
    """
    if len(points) < 2:
        raise ValueError("At least 2 points are required to compute polygon diameter.")

    hull = convex_hull(points)
    hull_size = len(hull)

    if hull_size == 1:
        return 0.0, (hull[0], hull[0])
    if hull_size == 2:
        return math.hypot(hull[0][0] - hull[1][0], hull[0][1] - hull[1][1]), (
            hull[0],
            hull[1],
        )

    max_dist_squared = 0.0
    best_pair = (hull[0], hull[1])

    # Find initial antipodal point furthest from edge hull[0]-hull[1]
    antipodal_idx = 1
    while cross_product(
        hull[0], hull[1], hull[(antipodal_idx + 1) % hull_size]
    ) > cross_product(hull[0], hull[1], hull[antipodal_idx]):
        antipodal_idx = (antipodal_idx + 1) % hull_size

    for current_idx in range(hull_size):
        next_idx = (current_idx + 1) % hull_size
        while cross_product(
            hull[current_idx], hull[next_idx], hull[(antipodal_idx + 1) % hull_size]
        ) > cross_product(hull[current_idx], hull[next_idx], hull[antipodal_idx]):
            antipodal_idx = (antipodal_idx + 1) % hull_size

        for p in (hull[current_idx], hull[next_idx]):
            for candidate_idx in (antipodal_idx, (antipodal_idx + 1) % hull_size):
                dist_sq = distance_squared(p, hull[candidate_idx])
                if dist_sq > max_dist_squared:
                    max_dist_squared = dist_sq
                    best_pair = (p, hull[candidate_idx])

    return math.sqrt(max_dist_squared), best_pair


if __name__ == "__main__":
    import doctest

    doctest.testmod()
