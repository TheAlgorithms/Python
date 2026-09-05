"""
Jarvis March (Gift Wrapping) algorithm for finding the convex hull of a set of points.

The convex hull is the smallest convex polygon that contains all the points.

Time Complexity: O(n*h) where n is the number of points and h is the number of
hull points.
Space Complexity: O(h) where h is the number of hull points.

USAGE:
    -> Import this file into your project.
    -> Use the jarvis_march() function to find the convex hull of a set of points.
    -> Parameters:
        -> points: A list of Point objects representing 2D coordinates

REFERENCES:
    -> Wikipedia reference: https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
    -> GeeksforGeeks:
       https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
"""

from __future__ import annotations


class Point:
    """Represents a 2D point with x and y coordinates."""

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = x_coordinate
        self.y = y_coordinate

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def _cross_product(origin: Point, point_a: Point, point_b: Point) -> float:
    """
    Calculate the cross product of vectors OA and OB.

    Returns:
        > 0: Counter-clockwise turn (left turn)
        = 0: Collinear
        < 0: Clockwise turn (right turn)
    """
    return (point_a.x - origin.x) * (point_b.y - origin.y) - (point_a.y - origin.y) * (
        point_b.x - origin.x
    )


def _is_point_on_segment(p1: Point, p2: Point, point: Point) -> bool:
    """Check if a point lies on the line segment between p1 and p2."""
    # Check if point is collinear with segment endpoints
    cross = (point.y - p1.y) * (p2.x - p1.x) - (point.x - p1.x) * (p2.y - p1.y)

    if abs(cross) > 1e-9:
        return False

    # Check if point is within the bounding box of the segment
    return min(p1.x, p2.x) <= point.x <= max(p1.x, p2.x) and min(
        p1.y, p2.y
    ) <= point.y <= max(p1.y, p2.y)


def _find_leftmost_point(points: list[Point]) -> int:
    """Find index of leftmost point (and bottom-most in case of tie)."""
    left_idx = 0
    for i in range(1, len(points)):
        if points[i].x < points[left_idx].x or (
            points[i].x == points[left_idx].x and points[i].y < points[left_idx].y
        ):
            left_idx = i
    return left_idx


def _find_next_hull_point(points: list[Point], current_idx: int) -> int:
    """Find the next point on the convex hull."""
    next_idx = (current_idx + 1) % len(points)
    # Ensure next_idx is not the same as current_idx
    while next_idx == current_idx:
        next_idx = (next_idx + 1) % len(points)

    for i in range(len(points)):
        if i == current_idx:
            continue
        cross = _cross_product(points[current_idx], points[i], points[next_idx])
        if cross > 0:
            next_idx = i

    return next_idx


def _is_valid_polygon(hull: list[Point]) -> bool:
    """Check if hull forms a valid polygon (has at least one non-collinear turn)."""
    for i in range(len(hull)):
        p1 = hull[i]
        p2 = hull[(i + 1) % len(hull)]
        p3 = hull[(i + 2) % len(hull)]
        if abs(_cross_product(p1, p2, p3)) > 1e-9:
            return True
    return False


def _add_point_to_hull(hull: list[Point], point: Point) -> None:
    """Add a point to hull, removing collinear intermediate points."""
    last = len(hull) - 1
    if len(hull) > 1 and _is_point_on_segment(hull[last - 1], hull[last], point):
        hull[last] = Point(point.x, point.y)
    else:
        hull.append(Point(point.x, point.y))


def jarvis_march(points: list[Point]) -> list[Point]:
    """
    Find the convex hull of a set of points using the Jarvis March algorithm.

    The algorithm starts with the leftmost point and wraps around the set of
    points, selecting the most counter-clockwise point at each step.

    Args:
        points: List of Point objects representing 2D coordinates

    Returns:
        List of Points that form the convex hull in counter-clockwise order.
        Returns empty list if there are fewer than 3 non-collinear points.
    """
    if len(points) <= 2:
        return []

    # Remove duplicate points to avoid infinite loops
    unique_points = list(set(points))

    if len(unique_points) <= 2:
        return []

    convex_hull: list[Point] = []

    # Find the leftmost point
    left_point_idx = _find_leftmost_point(unique_points)
    convex_hull.append(
        Point(unique_points[left_point_idx].x, unique_points[left_point_idx].y)
    )

    current_idx = left_point_idx
    while True:
        # Find the next counter-clockwise point
        next_idx = _find_next_hull_point(unique_points, current_idx)

        if next_idx == left_point_idx:
            break

        if next_idx == current_idx:
            break

        current_idx = next_idx
        _add_point_to_hull(convex_hull, unique_points[current_idx])

    # Check for degenerate cases
    if len(convex_hull) <= 2:
        return []

    # Check if last point is collinear with first and second-to-last
    last = len(convex_hull) - 1
    if _is_point_on_segment(convex_hull[last - 1], convex_hull[last], convex_hull[0]):
        convex_hull.pop()
        if len(convex_hull) == 2:
            return []

    # Verify the hull forms a valid polygon
    if not _is_valid_polygon(convex_hull):
        return []

    return convex_hull


if __name__ == "__main__":
    # Example usage
    points = [Point(0, 0), Point(1, 1), Point(0, 1), Point(1, 0), Point(0.5, 0.5)]
    hull = jarvis_march(points)
    print(f"Convex hull: {hull}")
