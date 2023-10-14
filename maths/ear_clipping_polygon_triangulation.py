"""
An implementation of the ear clipping method for triangulating a simple polygon.

Wikipedia : https://en.wikipedia.org/wiki/Polygon_triangulation
"""


def is_ear(polygon: list[tuple[float, float]], point_idx: int, direction: str) -> bool:
    """
    This function determines whether three points form an ear.

    >>> is_ear([(0, 2), (2, 2), (2,0), (1, 0), (1, 1), (0, 1)], 4,
    ... "counter-clockwise")
    False
    >>> is_ear([(0, 2), (2, 2), (2,0), (1, 0), (1, 1), (0, 1)], 3,
    ... "counter-clockwise")
    True
    >>> is_ear([(0, 3), (2, 2), (3, 0), (3, 3)], 3, "clockwise")
    False
    >>> is_ear([(0, 0), (1, 0), (1, 1), (0, 1)], 0, "clockwise")
    True
    """
    # Calculate indices for the previous and next vertices in the polygon.
    prev_idx = (point_idx - 1) % len(polygon)
    next_idx = (point_idx + 1) % len(polygon)

    # Retrieve the coordinates of the previous, current, and next vertices.
    prev_point = polygon[prev_idx]
    point = polygon[point_idx]
    next_point = polygon[next_idx]

    # Check if the vertex is convex based on the polygon's orientation.
    if is_convex(prev_point, point, next_point, direction):
        # Check if there are any points inside the triangle formed by the current vertex
        # and its neighbors.
        for j in range(len(polygon)):
            if j not in (prev_idx, point_idx, next_idx) and is_point_inside_triangle(
                prev_point, point, next_point, polygon[j]
            ):
                return False  # The 'ear' is not valid because there's a point
                # inside the triangle.
        return True  # The vertex is an 'ear' because it's convex and no points are
        # inside the triangle.
    return False  # The vertex is not an 'ear' because it's not convex.


def is_convex(
    point: tuple[float, float],
    prev_p: tuple[float, float],
    next_p: tuple[float, float],
    direction: str,
) -> bool:
    """
    Determine with the ccw, if 3 points are convex.
    >>> is_convex((1,1), (2, 2), (1, 2), "clockwise")
    True
    >>> is_convex((1,1), (2, 2), (1, 2), "counter-clockwise")
    False
    >>> is_convex((1,1), (2, 2), (3, 3), "clockwise")
    True
    >>> is_convex((1,1), (2, 2), (3, 3), "counter-clockwise")
    True
    """
    # Calculate the cross product based on the polygon's orientation.
    if direction == "counter-clockwise":
        cross_product = (next_p[0] - point[0]) * (prev_p[1] - point[1]) - (
            prev_p[0] - point[0]
        ) * (next_p[1] - point[1])
    else:
        cross_product = (prev_p[0] - point[0]) * (next_p[1] - point[1]) - (
            next_p[0] - point[0]
        ) * (prev_p[1] - point[1])
    # Determine if the angle is convex (cross product is non-negative).
    return cross_product >= 0


def cross_product(
    p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]
) -> float:
    """
    This function computes the product of two vectors, with 3 points.
    If the vectors are collinear, the output is 0.
    If the three points rotate counterclockwise, the output is positive.
    If three points rotate clockwise, the output is negative.

    >>> cross_product((0, 0), (1, 0), (1.5, 0.5))
    0.5
    >>> cross_product((1.5, 0.5), (1, 1), (1.5, 1.5))
    -0.5
    >>> cross_product((0, 0), (1, 1), (2, 2))
    0
    """
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def direction(polygon: list[tuple[float, float]]) -> str:
    """
    Determine the orientation (clockwise or counterclockwise) of a polygon defined
    by a list of points.
    >>> direction([(1, 1), (2, 2), (3, 4)])
    'clockwise'
    >>> direction([(1, 1), (2, 2), (3, -1)])
    'counter-clockwise'
    """
    # Find the point with the lowest y-coordinate (and leftmost if tied).
    point_0 = min(polygon, key=lambda point: (point[1], point[0]))
    idx_p0 = polygon.index(point_0)

    # Calculate the indices of the previous and next points.
    prev_idx = (idx_p0 - 1) % len(polygon)
    next_idx = (idx_p0 + 1) % len(polygon)

    prev_point = polygon[prev_idx]
    next_point = polygon[next_idx]
    # Handle cases where multiple points share the same y-coordinate.
    while cross_product(point_0, next_point, prev_point) == 0:
        next_idx += 1
        next_point = polygon[next_idx]
    # Determine the polygon's orientation based on the cross product.
    if cross_product(point_0, next_point, prev_point) > 0:
        return "clockwise"  # The polygon is in a clockwise direction.
    return "counter-clockwise"  # The polygon is in a counter-clockwise direction.


def is_point_inside_triangle(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    test_point: tuple[float, float],
) -> bool:
    """
    Determine whether a given point is located inside a triangle
    formed by three other points.

    This function calculates the area of both the triangle formed by
    the three input points (p1, p2, p3)
    and the sub-triangles formed by replacing one vertex of the main
    triangle with the test_point.
    If the sum of the areas of the sub-triangles is equal to the area of
    the main triangle, the test_point
    is considered to be inside the triangle. Otherwise, it is considered outside.

    >>> is_point_inside_triangle((0, 0), (0, 2), (2, 0), (3, 3))
    False
    >>> is_point_inside_triangle((0, 0), (0, 2), (2, 0), (1, 1))
    True
    >>> is_point_inside_triangle((0, 0), (2, 1), (2, 0), (1, 1))
    False
    >>> is_point_inside_triangle((0, 0), (2, 1), (2, 0), (2, 0))
    True
    >>> is_point_inside_triangle((0, 0), (1, 1), (2, 0), (1, 0))
    True
    """
    # Calculate the area of the main triangle.
    area_triangle = abs(
        0.5
        * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
    )
    # Calculate the areas of the sub-triangles formed by replacing one vertex
    # with the test_point.
    area1 = abs(
        0.5
        * (
            test_point[0] * (p2[1] - p3[1])
            + p2[0] * (p3[1] - test_point[1])
            + p3[0] * (test_point[1] - p2[1])
        )
    )
    area2 = abs(
        0.5
        * (
            p1[0] * (test_point[1] - p3[1])
            + test_point[0] * (p3[1] - p1[1])
            + p3[0] * (p1[1] - test_point[1])
        )
    )
    area3 = abs(
        0.5
        * (
            p1[0] * (p2[1] - test_point[1])
            + p2[0] * (test_point[1] - p1[1])
            + test_point[0] * (p1[1] - p2[1])
        )
    )

    # Check if the test_point is inside the triangle by comparing areas.
    return area_triangle == area1 + area2 + area3


def triangulate_polygon(
    coordinates: list[tuple[float, float]]
) -> list[list[tuple[float, float]]]:
    """
    Triangulate a polygon and provide the points of the resulting triangles.
    This function takes a list of coordinates that represent the vertices of a polygon.
    It iteratively finds and removes 'ears' from the polygon to create a list
    of triangles that triangulate the entire polygon.
    The order of vertices in the coordinates list is assumed to be
    consistent (either clockwise or counterclockwise).
    The function uses helper functions 'direction' to determine the polygon's
    orientation and 'is_ear' to identify 'ear' vertices.

    Note: The function assumes that the input coordinates form a valid simple polygon.

    >>> triangulate_polygon([(0, 2), (2, 2), (2, 0), (1, 0), (1, 1), (0, 1)])
    [[(0, 1), (0, 2), (2, 2)], [(2, 2), (2, 0), (1, 0)], [(2, 2), (1, 0), (1, 1)], \
[(0, 1), (2, 2), (1, 1)]]
    >>> triangulate_polygon([(0, 3), (2, 2), (3, 0), (3, 3)])
    [[(3, 3), (0, 3), (2, 2)], [(3, 3), (2, 2), (3, 0)]]
    >>> triangulate_polygon([(0, 0),(2, 0), (1, 1), (2, 2), (0,2)])
    [[(0, 0), (2, 0), (1, 1)], [(0, 2), (0, 0), (1, 1)], [(0, 2), (1, 1), (2, 2)]]

    """
    polygon: list[tuple[float, float]] = coordinates.copy()

    # Initialize an empty list to store the triangles
    triangles: list = []

    # Determine the orientation (clockwise or counterclockwise) of the polygon.
    orientation: str = direction(polygon)

    # Iterate while there are at least three vertices in the polygon.
    while len(polygon) >= 3:
        ear_found: bool = False

        # Find an 'ear' vertex and append the triangle to the list.
        for i in range(len(polygon)):
            if is_ear(polygon, i, orientation):
                ear_found = True
                prev_idx: int = (i - 1) % len(polygon)
                next_idx: int = (i + 1) % len(polygon)
                prev_point: tuple[float, float] = polygon[prev_idx]
                point: tuple[float, float] = polygon[i]
                next_point: tuple[float, float] = polygon[next_idx]
                triangles.append(
                    [
                        prev_point,
                        point,
                        next_point,
                    ]
                )
                polygon.pop(i)
                break

        # If no 'ear' is found, exit the loop.
        if not ear_found:
            break

    return triangles


if __name__ == "__main__":
    import doctest

    doctest.testmod()
