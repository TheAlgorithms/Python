"""
Graham Scan algorithm for finding the convex hull of a set of points.

The Graham scan is a method of computing the convex hull of a finite set of points
in the plane with time complexity O(n log n). It is named after Ronald Graham, who
published the original algorithm in 1972.

The algorithm finds all vertices of the convex hull ordered along its boundary.
It uses a stack to efficiently identify and remove points that would create
non-convex angles.

References:
- https://en.wikipedia.org/wiki/Graham_scan
- Graham, R.L. (1972). "An Efficient Algorithm for Determining the Convex Hull of a
  Finite Planar Set"
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T", bound="Point")


@dataclass
class Point:
    """
    A point in 2D space.

    >>> Point(0, 0)
    Point(x=0.0, y=0.0)
    >>> Point(1.5, 2.5)
    Point(x=1.5, y=2.5)
    """

    x: float
    y: float

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        """
        Initialize a 2D point.

        Args:
            x_coordinate: The x-coordinate (horizontal position) of the point
            y_coordinate: The y-coordinate (vertical position) of the point
        """
        self.x = float(x_coordinate)
        self.y = float(y_coordinate)

    def __eq__(self, other: object) -> bool:
        """
        Check if two points are equal.

        >>> Point(1, 2) == Point(1, 2)
        True
        >>> Point(1, 2) == Point(2, 1)
        False
        """
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other: Point) -> bool:
        """
        Compare two points for sorting (bottom-most, then left-most).

        >>> Point(1, 2) < Point(1, 3)
        True
        >>> Point(1, 2) < Point(2, 2)
        True
        >>> Point(2, 2) < Point(1, 2)
        False
        """
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y

    def euclidean_distance(self, other: Point) -> float:
        """
        Calculate Euclidean distance between two points.

        >>> Point(0, 0).euclidean_distance(Point(3, 4))
        5.0
        >>> Point(1, 1).euclidean_distance(Point(4, 5))
        5.0
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def consecutive_orientation(self, point_a: Point, point_b: Point) -> float:
        """
        Calculate the cross product of vectors (self -> point_a) and
        (point_a -> point_b).

        Returns:
        - Positive value: counter-clockwise turn
        - Negative value: clockwise turn
        - Zero: collinear points

        >>> Point(0, 0).consecutive_orientation(Point(1, 0), Point(1, 1))
        1.0
        >>> Point(0, 0).consecutive_orientation(Point(1, 0), Point(1, -1))
        -1.0
        >>> Point(0, 0).consecutive_orientation(Point(1, 0), Point(2, 0))
        0.0
        """
        return (point_a.x - self.x) * (point_b.y - point_a.y) - (point_a.y - self.y) * (
            point_b.x - point_a.x
        )


def graham_scan(points: Sequence[Point]) -> list[Point]:
    """
    Find the convex hull of a set of points using the Graham scan algorithm.

    The algorithm works as follows:
    1. Find the bottom-most point (or left-most in case of tie)
    2. Sort all other points by polar angle with respect to the bottom-most point
    3. Process points in order, maintaining a stack of hull candidates
    4. Remove points that would create a clockwise turn

    Args:
        points: A sequence of Point objects

    Returns:
        A list of Point objects representing the convex hull in counter-clockwise order.
        Returns an empty list if there are fewer than 3 distinct points or if all
        points are collinear.

    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for the output hull

    >>> graham_scan([])
    []
    >>> graham_scan([Point(0, 0)])
    []
    >>> graham_scan([Point(0, 0), Point(1, 1)])
    []
    >>> hull = graham_scan([Point(0, 0), Point(1, 0), Point(0.5, 1)])
    >>> len(hull)
    3
    >>> Point(0, 0) in hull and Point(1, 0) in hull and Point(0.5, 1) in hull
    True
    """
    if len(points) <= 2:
        return []

    # Find the bottom-most point (left-most in case of tie)
    min_point = min(points)

    # Remove the min_point from the list
    points_list = [p for p in points if p != min_point]
    if not points_list:
        # Edge case where all points are the same
        return []

    def polar_angle_key(point: Point) -> tuple[float, float, float]:
        """
        Key function for sorting points by polar angle relative to min_point.

        Points are sorted counter-clockwise. When two points have the same angle,
        the farther point comes first (we'll remove duplicates later).
        """
        # We use a dummy third point (min_point itself) to calculate relative angles
        # Instead, we'll compute the angle between points
        dx = point.x - min_point.x
        dy = point.y - min_point.y

        # Use atan2 for angle, but we can also use cross product for comparison
        # For sorting, we compare orientations between consecutive points
        distance = min_point.euclidean_distance(point)
        return (dx, dy, -distance)  # Negative distance to sort farther points first

    # Sort by polar angle using a comparison based on cross product
    def compare_points(point_a: Point, point_b: Point) -> int:
        """Compare two points by polar angle relative to min_point."""
        orientation = min_point.consecutive_orientation(point_a, point_b)
        if orientation < 0.0:
            return 1  # point_a comes after point_b (clockwise)
        elif orientation > 0.0:
            return -1  # point_a comes before point_b (counter-clockwise)
        else:
            # Collinear: farther point should come first
            dist_a = min_point.euclidean_distance(point_a)
            dist_b = min_point.euclidean_distance(point_b)
            if dist_b < dist_a:
                return -1
            elif dist_b > dist_a:
                return 1
            else:
                return 0

    from functools import cmp_to_key

    points_list.sort(key=cmp_to_key(compare_points))

    # Build the convex hull
    convex_hull: list[Point] = [min_point, points_list[0]]

    for point in points_list[1:]:
        # Skip consecutive points with the same angle (collinear with min_point)
        if min_point.consecutive_orientation(point, convex_hull[-1]) == 0.0:
            continue

        # Remove points that create a clockwise turn (or are collinear)
        while len(convex_hull) >= 2:
            orientation = convex_hull[-2].consecutive_orientation(
                convex_hull[-1], point
            )
            if orientation <= 0.0:
                convex_hull.pop()
            else:
                break

        convex_hull.append(point)

    # Need at least 3 points for a valid convex hull
    if len(convex_hull) <= 2:
        return []

    return convex_hull


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    points = [
        Point(0, 0),
        Point(1, 0),
        Point(2, 0),
        Point(2, 1),
        Point(2, 2),
        Point(1, 2),
        Point(0, 2),
        Point(0, 1),
        Point(1, 1),  # Interior point
    ]

    hull = graham_scan(points)
    print("Convex hull vertices:")
    for point in hull:
        print(f"  ({point.x}, {point.y})")
