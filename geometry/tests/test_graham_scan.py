"""
Tests for the Graham scan convex hull algorithm.
"""

from geometry.graham_scan import Point, graham_scan


def test_empty_points() -> None:
    """Test with no points."""
    assert graham_scan([]) == []


def test_single_point() -> None:
    """Test with a single point."""
    assert graham_scan([Point(0, 0)]) == []


def test_two_points() -> None:
    """Test with two points."""
    assert graham_scan([Point(0, 0), Point(1, 1)]) == []


def test_duplicate_points() -> None:
    """Test with all duplicate points."""
    p = Point(0, 0)
    points = [p, Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0)]
    assert graham_scan(points) == []


def test_collinear_points() -> None:
    """Test with all points on the same line."""
    points = [
        Point(1, 0),
        Point(2, 0),
        Point(3, 0),
        Point(4, 0),
        Point(5, 0),
    ]
    assert graham_scan(points) == []


def test_triangle() -> None:
    """Test with a triangle (3 points)."""
    p1 = Point(1, 1)
    p2 = Point(2, 1)
    p3 = Point(1.5, 2)
    points = [p1, p2, p3]
    hull = graham_scan(points)

    assert len(hull) == 3
    assert p1 in hull
    assert p2 in hull
    assert p3 in hull


def test_rectangle() -> None:
    """Test with a rectangle (4 points)."""
    p1 = Point(1, 1)
    p2 = Point(2, 1)
    p3 = Point(2, 2)
    p4 = Point(1, 2)
    points = [p1, p2, p3, p4]
    hull = graham_scan(points)

    assert len(hull) == 4
    assert all(p in hull for p in points)


def test_triangle_with_interior_points() -> None:
    """Test triangle with points inside."""
    p1 = Point(1, 1)
    p2 = Point(2, 1)
    p3 = Point(1.5, 2)
    p4 = Point(1.5, 1.5)  # Interior
    p5 = Point(1.2, 1.3)  # Interior
    p6 = Point(1.8, 1.2)  # Interior
    p7 = Point(1.5, 1.9)  # Interior

    hull_points = [p1, p2, p3]
    interior_points = [p4, p5, p6, p7]
    all_points = hull_points + interior_points

    hull = graham_scan(all_points)

    # All hull points should be in the result
    for p in hull_points:
        assert p in hull

    # No interior points should be in the result
    for p in interior_points:
        assert p not in hull


def test_rectangle_with_interior_points() -> None:
    """Test rectangle with points inside."""
    p1 = Point(1, 1)
    p2 = Point(2, 1)
    p3 = Point(2, 2)
    p4 = Point(1, 2)
    p5 = Point(1.5, 1.5)  # Interior
    p6 = Point(1.2, 1.3)  # Interior
    p7 = Point(1.8, 1.2)  # Interior
    p8 = Point(1.9, 1.7)  # Interior
    p9 = Point(1.4, 1.9)  # Interior

    hull_points = [p1, p2, p3, p4]
    interior_points = [p5, p6, p7, p8, p9]
    all_points = hull_points + interior_points

    hull = graham_scan(all_points)

    # All hull points should be in the result
    for p in hull_points:
        assert p in hull

    # No interior points should be in the result
    for p in interior_points:
        assert p not in hull


def test_star_shape() -> None:
    """Test with a star shape where only tips are on the convex hull."""
    # Tips of the star (on convex hull)
    p1 = Point(-5, 6)
    p2 = Point(-11, 0)
    p3 = Point(-9, -8)
    p4 = Point(4, 4)
    p5 = Point(6, -7)

    # Interior points (not on convex hull)
    p6 = Point(-7, -2)
    p7 = Point(-2, -4)
    p8 = Point(0, 1)
    p9 = Point(1, 0)
    p10 = Point(-6, 1)

    hull_points = [p1, p2, p3, p4, p5]
    interior_points = [p6, p7, p8, p9, p10]
    all_points = hull_points + interior_points

    hull = graham_scan(all_points)

    # All hull points should be in the result
    for p in hull_points:
        assert p in hull

    # No interior points should be in the result
    for p in interior_points:
        assert p not in hull


def test_rectangle_with_collinear_points() -> None:
    """Test rectangle with points on the edges (collinear with vertices)."""
    p1 = Point(1, 1)
    p2 = Point(2, 1)
    p3 = Point(2, 2)
    p4 = Point(1, 2)
    p5 = Point(1.5, 1)  # On edge p1-p2
    p6 = Point(1, 1.5)  # On edge p1-p4
    p7 = Point(2, 1.5)  # On edge p2-p3
    p8 = Point(1.5, 2)  # On edge p3-p4

    hull_points = [p1, p2, p3, p4]
    edge_points = [p5, p6, p7, p8]
    all_points = hull_points + edge_points

    hull = graham_scan(all_points)

    # All corner points should be in the result
    for p in hull_points:
        assert p in hull

    # Edge points should not be in the result (only corners)
    for p in edge_points:
        assert p not in hull


def test_point_equality() -> None:
    """Test Point equality."""
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(2, 1)

    assert p1 == p2
    assert p1 != p3


def test_point_comparison() -> None:
    """Test Point comparison for sorting."""
    p1 = Point(1, 2)
    p2 = Point(1, 3)
    p3 = Point(2, 2)

    assert p1 < p2  # Lower y value
    assert p1 < p3  # Same y, lower x
    assert not p2 < p1


def test_euclidean_distance() -> None:
    """Test Euclidean distance calculation."""
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    assert p1.euclidean_distance(p2) == 5.0


def test_consecutive_orientation() -> None:
    """Test orientation calculation."""
    p1 = Point(0, 0)
    p2 = Point(1, 0)
    p3_ccw = Point(1, 1)  # Counter-clockwise
    p3_cw = Point(1, -1)  # Clockwise
    p3_collinear = Point(2, 0)  # Collinear

    assert p1.consecutive_orientation(p2, p3_ccw) > 0  # Counter-clockwise
    assert p1.consecutive_orientation(p2, p3_cw) < 0  # Clockwise
    assert p1.consecutive_orientation(p2, p3_collinear) == 0  # Collinear


def test_large_hull() -> None:
    """Test with a larger set of points."""
    # Create a circle of points
    import math

    points = []
    for i in range(20):
        angle = 2 * math.pi * i / 20
        x = math.cos(angle)
        y = math.sin(angle)
        points.append(Point(x, y))

    # Add some interior points
    points.append(Point(0, 0))
    points.append(Point(0.5, 0.5))
    points.append(Point(-0.3, 0.2))

    hull = graham_scan(points)

    # The hull should contain the circle points but not the interior points
    assert len(hull) >= 3
    assert Point(0, 0) not in hull
    assert Point(0.5, 0.5) not in hull
    assert Point(-0.3, 0.2) not in hull


def test_random_order() -> None:
    """Test that point order doesn't affect the result."""
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)
    p5 = Point(2, 1.5)  # Interior

    # Try different orderings
    order1 = [p1, p2, p3, p4, p5]
    order2 = [p5, p4, p3, p2, p1]
    order3 = [p3, p5, p1, p4, p2]

    hull1 = graham_scan(order1)
    hull2 = graham_scan(order2)
    hull3 = graham_scan(order3)

    # All should have the same points (though possibly in different order)
    assert len(hull1) == len(hull2) == len(hull3) == 4
    assert {(p.x, p.y) for p in hull1} == {(p.x, p.y) for p in hull2}
    assert {(p.x, p.y) for p in hull2} == {(p.x, p.y) for p in hull3}
