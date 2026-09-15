"""
Point in Polygon (PIP) Algorithm using Ray Casting (Even-Odd Rule).

References:
- https://en.wikipedia.org/wiki/Point_in_polygon
- https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
- Shimrat, M. (1962). "Algorithm 112: Position of point relative to polygon".
  Communications of the ACM, 5(8), 434.

The ray casting algorithm determines whether a given point in the plane lies
inside, outside, or on the boundary of an arbitrary polygon (convex or concave).
It works by casting a horizontal ray from the query point to infinity in the positive
x-direction and counting how many polygon edges intersect this ray:
- An odd number of intersections indicates the point is inside the polygon.
- An even number of intersections indicates the point is outside the polygon.

Boundary handling:
Points lying exactly on an edge or vertex of the polygon are detected explicitly
via segment collinearity and bounding box checks.
"""

from __future__ import annotations

from typing import NamedTuple


class Point(NamedTuple):
    """
    A 2D point with real-valued coordinates.

    >>> Point(0.0, 0.0)
    Point(x=0.0, y=0.0)
    >>> Point(1.5, -2.0)
    Point(x=1.5, y=-2.0)
    """

    x: float
    y: float


def is_point_on_segment(
    point: Point, seg_start: Point, seg_end: Point, tolerance: float = 0.0
) -> bool:
    """
    Determine whether a point lies on the line segment between seg_start and seg_end.

    The check verifies that:
    1. The point is collinear with the segment endpoints
       (cross product within tolerance).
    2. The point lies within the bounding box of the segment (within tolerance).

    Parameters:
        point: The query Point.
        seg_start: The start Point of the line segment.
        seg_end: The end Point of the line segment.
        tolerance: Non-negative tolerance for collinearity and bounding box
            checks (default 0.0 for exact mathematical boundary testing).

    Raises:
        ValueError: If tolerance is negative.

    >>> is_point_on_segment(Point(1.0, 1.0), Point(0.0, 0.0), Point(2.0, 2.0))
    True
    >>> is_point_on_segment(Point(0.0, 0.0), Point(0.0, 0.0), Point(2.0, 2.0))
    True
    >>> is_point_on_segment(Point(2.0, 2.0), Point(0.0, 0.0), Point(2.0, 2.0))
    True
    >>> is_point_on_segment(Point(3.0, 3.0), Point(0.0, 0.0), Point(2.0, 2.0))
    False
    >>> is_point_on_segment(Point(1.0, 2.0), Point(0.0, 0.0), Point(2.0, 2.0))
    False
    >>> is_point_on_segment(Point(2.0, 0.0), Point(0.0, 0.0), Point(4.0, 0.0))
    True
    >>> is_point_on_segment(Point(2.0, 1e-10), Point(0.0, 0.0), Point(4.0, 0.0))
    False
    >>> is_point_on_segment(
    ...     Point(2.0, 1e-10), Point(0.0, 0.0), Point(4.0, 0.0), tolerance=1e-9
    ... )
    True
    >>> is_point_on_segment(Point(0.0, 0.0), Point(0.0, 0.0), Point(1.0, 1.0), -1.0)
    Traceback (most recent call last):
        ...
    ValueError: tolerance must be non-negative.
    """
    if tolerance < 0.0:
        raise ValueError("tolerance must be non-negative.")

    # Cross product of vector (seg_start -> seg_end) and (seg_start -> point)
    cross_product = (seg_end.x - seg_start.x) * (point.y - seg_start.y) - (
        seg_end.y - seg_start.y
    ) * (point.x - seg_start.x)
    if abs(cross_product) > tolerance:
        return False

    # Check bounding box
    is_within_x_bounds = (
        min(seg_start.x, seg_end.x) - tolerance
        <= point.x
        <= max(seg_start.x, seg_end.x) + tolerance
    )
    is_within_y_bounds = (
        min(seg_start.y, seg_end.y) - tolerance
        <= point.y
        <= max(seg_start.y, seg_end.y) + tolerance
    )
    return is_within_x_bounds and is_within_y_bounds


def point_in_polygon(
    point: Point,
    polygon: list[Point],
    include_boundary: bool = True,
    tolerance: float = 0.0,
) -> bool:
    """
    Determine whether a 2D point lies inside an arbitrary polygon using ray casting.

    Parameters:
        point: The query Point(x, y).
        polygon: A list of Point instances representing vertices of the polygon
            in cyclic order (clockwise or counter-clockwise). Must have >= 3 vertices.
        include_boundary: Whether points on the boundary (edges or vertices)
            are considered inside (default True).
        tolerance: Non-negative tolerance for boundary testing (default 0.0
            for exact mathematical boundary testing).

    Returns:
        True if the point is inside (or on the boundary if include_boundary=True),
        False otherwise.

    Raises:
        ValueError: If the polygon has fewer than 3 vertices or tolerance is negative.

    Examples:
    >>> square = [Point(0.0, 0.0), Point(4.0, 0.0), Point(4.0, 4.0), Point(0.0, 4.0)]
    >>> point_in_polygon(Point(2.0, 2.0), square)
    True
    >>> point_in_polygon(Point(5.0, 2.0), square)
    False
    >>> point_in_polygon(Point(-1.0, 2.0), square)
    False
    >>> point_in_polygon(Point(2.0, 5.0), square)
    False

    Boundary tests (exact boundary testing with tolerance=0.0):
    >>> point_in_polygon(Point(0.0, 2.0), square, include_boundary=True)
    True
    >>> point_in_polygon(Point(0.0, 2.0), square, include_boundary=False)
    False
    >>> point_in_polygon(Point(4.0, 4.0), square, include_boundary=True)
    True
    >>> point_in_polygon(Point(4.0, 4.0), square, include_boundary=False)
    False
    >>> point_in_polygon(Point(2.0, 0.0), square, include_boundary=True)
    True
    >>> point_in_polygon(Point(2.0, 0.0), square, include_boundary=False)
    False

    Points very close to boundary:
    >>> point_in_polygon(Point(2.0, -1e-10), square)
    False
    >>> point_in_polygon(Point(2.0, 1e-10), square, include_boundary=False)
    True
    >>> point_in_polygon(Point(2.0, -1e-10), square, tolerance=1e-9)
    True

    Concave (arrowhead) polygon:
    >>> arrowhead = [Point(0.0, 0.0), Point(5.0, 2.0), Point(0.0, 4.0), Point(2.0, 2.0)]
    >>> point_in_polygon(Point(3.0, 2.0), arrowhead)
    True
    >>> point_in_polygon(Point(1.0, 2.0), arrowhead)
    False

    Triangle with negative and floating point coordinates:
    >>> triangle = [Point(-2.5, -2.5), Point(2.5, -2.5), Point(0.0, 2.5)]
    >>> point_in_polygon(Point(0.0, 0.0), triangle)
    True
    >>> point_in_polygon(Point(0.0, 3.0), triangle)
    False
    >>> point_in_polygon(Point(-3.0, 0.0), triangle)
    False

    Invalid input (fewer than 3 vertices or negative tolerance):
    >>> point_in_polygon(Point(0.0, 0.0), [Point(0.0, 0.0), Point(1.0, 1.0)])
    Traceback (most recent call last):
        ...
    ValueError: A polygon must have at least 3 vertices.
    >>> point_in_polygon(Point(0.0, 0.0), square, tolerance=-1.0)
    Traceback (most recent call last):
        ...
    ValueError: tolerance must be non-negative.
    """
    if len(polygon) < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    if tolerance < 0.0:
        raise ValueError("tolerance must be non-negative.")

    num_vertices = len(polygon)

    # Check if point lies on any boundary edge or vertex
    for vertex_index in range(num_vertices):
        edge_start = polygon[vertex_index]
        edge_end = polygon[(vertex_index + 1) % num_vertices]
        if is_point_on_segment(point, edge_start, edge_end, tolerance=tolerance):
            return include_boundary

    # Ray casting: cast a horizontal ray from point towards positive x-infinity
    is_inside = False
    for vertex_index in range(num_vertices):
        current_vertex = polygon[vertex_index]
        next_vertex = polygon[(vertex_index + 1) % num_vertices]

        # Check whether the edge crosses the horizontal ray.
        # The condition (current_vertex.y > point.y) != (next_vertex.y > point.y)
        # ensures:
        # 1. Strictly horizontal edges (current_vertex.y == next_vertex.y) are skipped.
        # 2. Vertices intersecting the ray are counted exactly once when crossed.
        if (current_vertex.y > point.y) != (next_vertex.y > point.y):
            # Compute x-coordinate of intersection with line y = point.y
            ray_x_intersection = current_vertex.x + (point.y - current_vertex.y) * (
                next_vertex.x - current_vertex.x
            ) / (next_vertex.y - current_vertex.y)
            if point.x < ray_x_intersection:
                is_inside = not is_inside

    return is_inside


if __name__ == "__main__":
    import doctest

    doctest.testmod()
