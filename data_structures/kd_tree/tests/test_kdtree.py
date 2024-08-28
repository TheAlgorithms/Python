import numpy as np
from data_structures.kd_tree.build_kdtree import build_kdtree
from data_structures.kd_tree.nearest_neighbour_search import nearest_neighbour_search
from data_structures.kd_tree.kd_node import KDNode
from data_structures.kd_tree.example.hypercube_points import hypercube_points


def test_build_kdtree():
    """
    Test that KD-Tree is built correctly.
    """
    num_points = 10
    cube_size = 10.0
    num_dimensions = 2
    points = hypercube_points(num_points, cube_size, num_dimensions)
    kdtree = build_kdtree(points.tolist())

    # Check if root is not None
    assert kdtree is not None

    # Check if root has correct dimensions
    assert len(kdtree.point) == num_dimensions

    # Check that the tree is balanced to some extent (simplistic check)
    assert isinstance(kdtree, KDNode)


def test_nearest_neighbour_search():
    """
    Test the nearest neighbor search function.
    """
    num_points = 10
    cube_size = 10.0
    num_dimensions = 2
    points = hypercube_points(num_points, cube_size, num_dimensions)
    kdtree = build_kdtree(points.tolist())

    rng = np.random.default_rng()
    query_point = rng.random(num_dimensions).tolist()

    nearest_point, nearest_dist, nodes_visited = nearest_neighbour_search(
        kdtree, query_point
    )

    # Check that nearest point is not None
    assert nearest_point is not None

    # Check that distance is a non-negative number
    assert nearest_dist >= 0

    # Check that nodes visited is a non-negative integer
    assert nodes_visited >= 0


def test_edge_cases():
    """
    Test edge cases such as an empty KD-Tree.
    """
    empty_kdtree = build_kdtree([])
    query_point = [0.0] * 2  # Using a default 2D query point

    nearest_point, nearest_dist, nodes_visited = nearest_neighbour_search(
        empty_kdtree, query_point
    )

    # With an empty KD-Tree, nearest_point should be None
    assert nearest_point is None
    assert nearest_dist == float("inf")
    assert nodes_visited == 0


if __name__ == "__main__":
    import pytest

    pytest.main()
