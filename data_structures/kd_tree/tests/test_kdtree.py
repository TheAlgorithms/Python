import numpy as np
import pytest

from data_structures.kd_tree.build_kdtree import build_kdtree
from data_structures.kd_tree.example.hypercube_points import hypercube_points
from data_structures.kd_tree.kd_node import KDNode
from data_structures.kd_tree.nearest_neighbour_search import nearest_neighbour_search


@pytest.mark.parametrize(
    ("num_points", "cube_size", "num_dimensions", "depth", "expected_result"),
    [
        (0, 10.0, 2, 0, None),  # Empty points list
        (10, 10.0, 2, 2, KDNode),  # Depth = 2, 2D points
        (10, 10.0, 3, -2, KDNode),  # Depth = -2, 3D points
    ],
)
def test_build_kdtree(num_points, cube_size, num_dimensions, depth, expected_result):
    """
    Test that KD-Tree is built correctly.

    Cases:
        - Empty points list.
        - Positive depth value.
        - Negative depth value.
    """
    points = (
        hypercube_points(num_points, cube_size, num_dimensions).tolist()
        if num_points > 0
        else []
    )

    kdtree = build_kdtree(points, depth=depth)

    if expected_result is None:
        # Empty points list case
        assert kdtree is None, f"Expected None for empty points list, got {kdtree}"
    else:
        # Check if root node is not None
        assert kdtree is not None, "Expected a KDNode, got None"

        # Check if root has correct dimensions
        assert (
            len(kdtree.point) == num_dimensions
        ), f"Expected point dimension {num_dimensions}, got {len(kdtree.point)}"

        # Check that the tree is balanced to some extent (simplistic check)
        assert isinstance(
            kdtree, KDNode
        ), f"Expected KDNode instance, got {type(kdtree)}"


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
