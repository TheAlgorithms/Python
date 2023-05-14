"""
An implementation of Graham's scan method for finding
the convex hull of a set of points.
pseudo-code from https://en.wikipedia.org/wiki/Graham_scan :

let points be the list of points
let stack = empty_stack()

find the lowest y-coordinate and leftmost point, called P0
sort points by polar angle with P0, if several points have the same
polar angle then only keep the farthest

for point in points:
    # pop the last point from the stack if we turn clockwise to reach this point
    while count stack > 1 and ccw(next_to_top(stack), top(stack), point) <= 0:
        pop stack
    push point to stack
end
"""
import math


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


def graham_scan(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """
    This function implements the Graham algorithm for finding
    the convex hull of a set of points.

    >>> graham_scan([(0, 0), (0, 1), (1, 0), (1, 1), (0.5, 0.5), (0.5, 1.5),
    ... (1.5, 0.5), (1.5, 1.5)])
    [(0, 0), (1, 0), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5), (0, 1)]
    >>> graham_scan([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)])
    [(0, 0), (7, 7)]
    """
    stack: list[tuple[float, float]] = []
    point_0 = min(
        points, key=lambda p: (p[1], p[0])
    )  # Find the point with the lowest y-coordinate.

    points.sort(
        key=lambda p: (
            math.atan2(p[1] - point_0[1], p[0] - point_0[0]),
            p[0] ** 2 + p[1] ** 2,
        )
    )  # Sort the points based on their angle with point_0.

    # Loop over sorted points and add necessary points to the convex hull.
    for point in points:
        # While the last points of the convex hull and
        # the current point do not form a convex orientation,
        # remove the last point from the convex hull.
        while len(stack) > 1 and cross_product(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        # Add the current point to the convex hull.
        stack.append(point)
    # The stack now contains the points forming
    # the convex hull of the original set of points.

    return stack


if __name__ == "__main__":
    import doctest

    doctest.testmod()
