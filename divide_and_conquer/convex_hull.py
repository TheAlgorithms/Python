"""
The convex hull problem is problem of finding all the vertices of convex polygon, P of
a set of points in a plane such that all the points are either on the vertices of P or
inside P. TH convex hull problem has several applications in geometrical problems,
computer graphics and game development.

Two algorithms have been implemented for the convex hull problem here.
1. A brute-force algorithm which runs in O(n^3)
2. A divide-and-conquer algorithm which runs in O(n log(n))

There are other several other algorithms for the convex hull problem
which have not been implemented here, yet.

"""
from __future__ import annotations

from collections.abc import Iterable


class Point:
    """
    Defines a 2-d point for use by all convex-hull algorithms.

    Parameters
    ----------
    x: an int or a float, the x-coordinate of the 2-d point
    y: an int or a float, the y-coordinate of the 2-d point

    Examples
    --------
    >>> Point(1, 2)
    (1.0, 2.0)
    >>> Point("1", "2")
    (1.0, 2.0)
    >>> Point(1, 2) > Point(0, 1)
    True
    >>> Point(1, 1) == Point(1, 1)
    True
    >>> Point(-0.5, 1) == Point(0.5, 1)
    False
    >>> Point("pi", "e")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'pi'
    """

    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y > other.y
        return False

    def __lt__(self, other):
        return not self > other

    def __ge__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y >= other.y
        return False

    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y <= other.y
        return False

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash(self.x)


def _construct_points(
    list_of_tuples: list[Point] | list[list[float]] | Iterable[list[float]],
) -> list[Point]:
    """
    constructs a list of points from an array-like object of numbers

    Arguments
    ---------

    list_of_tuples: array-like object of type numbers. Acceptable types so far
    are lists, tuples and sets.

    Returns
    --------
    points: a list where each item is of type Point. This contains only objects
    which can be converted into a Point.

    Examples
    -------
    >>> _construct_points([[1, 1], [2, -1], [0.3, 4]])
    [(1.0, 1.0), (2.0, -1.0), (0.3, 4.0)]
    >>> _construct_points([1, 2])
    Ignoring deformed point 1. All points must have at least 2 coordinates.
    Ignoring deformed point 2. All points must have at least 2 coordinates.
    []
    >>> _construct_points([])
    []
    >>> _construct_points(None)
    []
    """

    points: list[Point] = []
    if list_of_tuples:
        for p in list_of_tuples:
            if isinstance(p, Point):
                points.append(p)
            else:
                try:
                    points.append(Point(p[0], p[1]))
                except (IndexError, TypeError):
                    print(
                        f"Ignoring deformed point {p}. All points"
                        " must have at least 2 coordinates."
                    )
    return points


def _validate_input(points: list[Point] | list[list[float]]) -> list[Point]:
    """
    validates an input instance before a convex-hull algorithms uses it

    Parameters
    ---------
    points: array-like, the 2d points to validate before using with
    a convex-hull algorithm. The elements of points must be either lists, tuples or
    Points.

    Returns
    -------
    points: array_like, an iterable of all well-defined Points constructed passed in.


    Exception
    ---------
    ValueError: if points is empty or None, or if a wrong data structure like a scalar
                 is passed

    TypeError: if an iterable but non-indexable object (eg. dictionary) is passed.
                The exception to this a set which we'll convert to a list before using


    Examples
    -------
    >>> _validate_input([[1, 2]])
    [(1.0, 2.0)]
    >>> _validate_input([(1, 2)])
    [(1.0, 2.0)]
    >>> _validate_input([Point(2, 1), Point(-1, 2)])
    [(2.0, 1.0), (-1.0, 2.0)]
    >>> _validate_input([])
    Traceback (most recent call last):
        ...
    ValueError: Expecting a list of points but got []
    >>> _validate_input(1)
    Traceback (most recent call last):
        ...
    ValueError: Expecting an iterable object but got an non-iterable type 1
    """

    if not hasattr(points, "__iter__"):
        msg = f"Expecting an iterable object but got an non-iterable type {points}"
        raise ValueError(msg)

    if not points:
        msg = f"Expecting a list of points but got {points}"
        raise ValueError(msg)

    return _construct_points(points)


def _det(a: Point, b: Point, c: Point) -> float:
    """
    Computes the sign perpendicular distance of a 2d point c from a line segment
    ab. The sign indicates the direction of c relative to ab.
    A Positive value means c is above ab (to the left), while a negative value
    means c is below ab (to the right). 0 means all three points are on a straight line.

    As a side note, 0.5 * abs|det| is the area of triangle abc

    Parameters
    ----------
    a: point, the point on the left end of line segment ab
    b: point, the point on the right end of line segment ab
    c: point, the point for which the direction and location is desired.

    Returns
    --------
    det: float, abs(det) is the distance of c from ab. The sign
    indicates which side of line segment ab c is. det is computed as
    (a_xb_y + c_xa_y + b_xc_y) - (a_yb_x + c_ya_x + b_yc_x)

    Examples
    ----------
    >>> _det(Point(1, 1), Point(1, 2), Point(1, 5))
    0.0
    >>> _det(Point(0, 0), Point(10, 0), Point(0, 10))
    100.0
    >>> _det(Point(0, 0), Point(10, 0), Point(0, -10))
    -100.0
    """

    det = (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x)
    return det


def convex_hull_bf(points: list[Point]) -> list[Point]:
    """
    Constructs the convex hull of a set of 2D points using a brute force algorithm.
    The algorithm basically considers all combinations of points (i, j) and uses the
    definition of convexity to determine whether (i, j) is part of the convex hull or
    not.  (i, j) is part of the convex hull if and only iff there are no points on both
    sides of the line segment connecting the ij, and there is no point k such that k is
    on either end of the ij.

    Runtime: O(n^3) - definitely horrible

    Parameters
    ---------
    points: array-like of object of Points, lists or tuples.
    The set of  2d points for which the convex-hull is needed

    Returns
    ------
    convex_set: list, the convex-hull of points sorted in non-decreasing order.

    See Also
    --------
    convex_hull_recursive,

     Examples
     ---------
     >>> convex_hull_bf([[0, 0], [1, 0], [10, 1]])
     [(0.0, 0.0), (1.0, 0.0), (10.0, 1.0)]
     >>> convex_hull_bf([[0, 0], [1, 0], [10, 0]])
     [(0.0, 0.0), (10.0, 0.0)]
     >>> convex_hull_bf([[-1, 1],[-1, -1], [0, 0], [0.5, 0.5], [1, -1], [1, 1],
     ...                 [-0.75, 1]])
     [(-1.0, -1.0), (-1.0, 1.0), (1.0, -1.0), (1.0, 1.0)]
     >>> convex_hull_bf([(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3),
     ...                 (2, -1), (2, -4), (1, -3)])
     [(0.0, 0.0), (0.0, 3.0), (1.0, -3.0), (2.0, -4.0), (3.0, 0.0), (3.0, 3.0)]
    """

    points = sorted(_validate_input(points))
    n = len(points)
    convex_set = set()

    for i in range(n - 1):
        for j in range(i + 1, n):
            points_left_of_ij = points_right_of_ij = False
            ij_part_of_convex_hull = True
            for k in range(n):
                if k != i and k != j:
                    det_k = _det(points[i], points[j], points[k])

                    if det_k > 0:
                        points_left_of_ij = True
                    elif det_k < 0:
                        points_right_of_ij = True
                    else:
                        # point[i], point[j], point[k] all lie on a straight line
                        # if point[k] is to the left of point[i] or it's to the
                        # right of point[j], then point[i], point[j] cannot be
                        # part of the convex hull of A
                        if points[k] < points[i] or points[k] > points[j]:
                            ij_part_of_convex_hull = False
                            break

                if points_left_of_ij and points_right_of_ij:
                    ij_part_of_convex_hull = False
                    break

            if ij_part_of_convex_hull:
                convex_set.update([points[i], points[j]])

    return sorted(convex_set)


def convex_hull_recursive(points: list[Point]) -> list[Point]:
    """
    Constructs the convex hull of a set of 2D points using a divide-and-conquer strategy
    The algorithm exploits the geometric properties of the problem by repeatedly
    partitioning the set of points into smaller hulls, and finding the convex hull of
    these smaller hulls.  The union of the convex hull from smaller hulls is the
    solution to the convex hull of the larger problem.

    Parameter
    ---------
    points: array-like of object of Points, lists or tuples.
    The set of  2d points for which the convex-hull is needed

    Runtime: O(n log n)

    Returns
    -------
    convex_set: list, the convex-hull of points sorted in non-decreasing order.

    Examples
    ---------
    >>> convex_hull_recursive([[0, 0], [1, 0], [10, 1]])
    [(0.0, 0.0), (1.0, 0.0), (10.0, 1.0)]
    >>> convex_hull_recursive([[0, 0], [1, 0], [10, 0]])
    [(0.0, 0.0), (10.0, 0.0)]
    >>> convex_hull_recursive([[-1, 1],[-1, -1], [0, 0], [0.5, 0.5], [1, -1], [1, 1],
    ...                        [-0.75, 1]])
    [(-1.0, -1.0), (-1.0, 1.0), (1.0, -1.0), (1.0, 1.0)]
    >>> convex_hull_recursive([(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3),
    ...                        (2, -1), (2, -4), (1, -3)])
    [(0.0, 0.0), (0.0, 3.0), (1.0, -3.0), (2.0, -4.0), (3.0, 0.0), (3.0, 3.0)]

    """
    points = sorted(_validate_input(points))
    n = len(points)

    # divide all the points into an upper hull and a lower hull
    # the left most point and the right most point are definitely
    # members of the convex hull by definition.
    # use these two anchors to divide all the points into two hulls,
    # an upper hull and a lower hull.

    # all points to the left (above) the line joining the extreme points belong to the
    # upper hull
    # all points to the right (below) the line joining the extreme points below to the
    # lower hull
    # ignore all points on the line joining the extreme points since they cannot be
    # part of the convex hull

    left_most_point = points[0]
    right_most_point = points[n - 1]

    convex_set = {left_most_point, right_most_point}
    upper_hull = []
    lower_hull = []

    for i in range(1, n - 1):
        det = _det(left_most_point, right_most_point, points[i])

        if det > 0:
            upper_hull.append(points[i])
        elif det < 0:
            lower_hull.append(points[i])

    _construct_hull(upper_hull, left_most_point, right_most_point, convex_set)
    _construct_hull(lower_hull, right_most_point, left_most_point, convex_set)

    return sorted(convex_set)


def _construct_hull(
    points: list[Point], left: Point, right: Point, convex_set: set[Point]
) -> None:
    """

    Parameters
    ---------
    points: list or None, the hull of points from which to choose the next convex-hull
        point
    left: Point, the point to the left  of line segment joining left and right
    right: The point to the right of the line segment joining left and right
    convex_set: set, the current convex-hull. The state of convex-set gets updated by
        this function

    Note
    ----
    For the line segment 'ab', 'a' is on the left and 'b' on the right.
    but the reverse is true for the line segment 'ba'.

    Returns
    -------
    Nothing, only updates the state of convex-set
    """
    if points:
        extreme_point = None
        extreme_point_distance = float("-inf")
        candidate_points = []

        for p in points:
            det = _det(left, right, p)

            if det > 0:
                candidate_points.append(p)

                if det > extreme_point_distance:
                    extreme_point_distance = det
                    extreme_point = p

        if extreme_point:
            _construct_hull(candidate_points, left, extreme_point, convex_set)
            convex_set.add(extreme_point)
            _construct_hull(candidate_points, extreme_point, right, convex_set)


def convex_hull_melkman(points: list[Point]) -> list[Point]:
    """
    Constructs the convex hull of a set of 2D points using the melkman algorithm.
    The algorithm works by iteratively inserting points of a simple polygonal chain
    (meaning that no line segments between two consecutive points cross each other).
    Sorting the points yields such a polygonal chain.

    For a detailed description, see http://cgm.cs.mcgill.ca/~athens/cs601/Melkman.html

    Runtime: O(n log n) - O(n) if points are already sorted in the input

    Parameters
    ---------
    points: array-like of object of Points, lists or tuples.
    The set of 2d points for which the convex-hull is needed

    Returns
    ------
    convex_set: list, the convex-hull of points sorted in non-decreasing order.

    See Also
    --------

    Examples
    ---------
    >>> convex_hull_melkman([[0, 0], [1, 0], [10, 1]])
    [(0.0, 0.0), (1.0, 0.0), (10.0, 1.0)]
    >>> convex_hull_melkman([[0, 0], [1, 0], [10, 0]])
    [(0.0, 0.0), (10.0, 0.0)]
    >>> convex_hull_melkman([[-1, 1],[-1, -1], [0, 0], [0.5, 0.5], [1, -1], [1, 1],
    ...                 [-0.75, 1]])
    [(-1.0, -1.0), (-1.0, 1.0), (1.0, -1.0), (1.0, 1.0)]
    >>> convex_hull_melkman([(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3),
    ...                 (2, -1), (2, -4), (1, -3)])
    [(0.0, 0.0), (0.0, 3.0), (1.0, -3.0), (2.0, -4.0), (3.0, 0.0), (3.0, 3.0)]
    """
    points = sorted(_validate_input(points))
    n = len(points)

    convex_hull = points[:2]
    for i in range(2, n):
        det = _det(convex_hull[1], convex_hull[0], points[i])
        if det > 0:
            convex_hull.insert(0, points[i])
            break
        elif det < 0:
            convex_hull.append(points[i])
            break
        else:
            convex_hull[1] = points[i]
    i += 1

    for j in range(i, n):
        if (
            _det(convex_hull[0], convex_hull[-1], points[j]) > 0
            and _det(convex_hull[-1], convex_hull[0], points[1]) < 0
        ):
            # The point lies within the convex hull
            continue

        convex_hull.insert(0, points[j])
        convex_hull.append(points[j])
        while _det(convex_hull[0], convex_hull[1], convex_hull[2]) >= 0:
            del convex_hull[1]
        while _det(convex_hull[-1], convex_hull[-2], convex_hull[-3]) <= 0:
            del convex_hull[-2]

    # `convex_hull` is contains the convex hull in circular order
    return sorted(convex_hull[1:] if len(convex_hull) > 3 else convex_hull)


def main():
    points = [
        (0, 3),
        (2, 2),
        (1, 1),
        (2, 1),
        (3, 0),
        (0, 0),
        (3, 3),
        (2, -1),
        (2, -4),
        (1, -3),
    ]
    # the convex set of points is
    # [(0, 0), (0, 3), (1, -3), (2, -4), (3, 0), (3, 3)]
    results_bf = convex_hull_bf(points)

    results_recursive = convex_hull_recursive(points)
    assert results_bf == results_recursive

    results_melkman = convex_hull_melkman(points)
    assert results_bf == results_melkman

    print(results_bf)


if __name__ == "__main__":
    main()
