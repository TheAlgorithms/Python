import unittest
import numpy as np
from data_structures.kd_tree.build_kdtree import build_kdtree
from data_structures.kd_tree.nearest_neighbour_search import nearest_neighbour_search
from data_structures.kd_tree.kd_node import KDNode
from data_structures.kd_tree.example.hypercube_points import hypercube_points

class TestKDTree(unittest.TestCase):

    def setUp(self):
        """
        Set up test data.
        """
        self.num_points = 10
        self.cube_size = 10.0
        self.num_dimensions = 2
        self.points = hypercube_points(self.num_points, self.cube_size, self.num_dimensions)
        self.kdtree = build_kdtree(self.points.tolist())

    def test_build_kdtree(self):
        """
        Test that KD-Tree is built correctly.
        """
        # Check if root is not None
        self.assertIsNotNone(self.kdtree)

        # Check if root has correct dimensions
        self.assertEqual(len(self.kdtree.point), self.num_dimensions)

        # Check that the tree is balanced to some extent (simplistic check)
        self.assertIsInstance(self.kdtree, KDNode)

    def test_nearest_neighbour_search(self):
        """
        Test the nearest neighbor search function.
        """
        rng = np.random.default_rng()
        query_point = rng.random(self.num_dimensions).tolist()

        nearest_point, nearest_dist, nodes_visited = nearest_neighbour_search(
            self.kdtree, query_point
        )

        # Check that nearest point is not None
        self.assertIsNotNone(nearest_point)

        # Check that distance is a non-negative number
        self.assertGreaterEqual(nearest_dist, 0)

        # Check that nodes visited is a non-negative integer
        self.assertGreaterEqual(nodes_visited, 0)

    def test_edge_cases(self):
        """
        Test edge cases such as an empty KD-Tree.
        """
        empty_kdtree = build_kdtree([])
        query_point = [0.0] * self.num_dimensions

        nearest_point, nearest_dist, nodes_visited = nearest_neighbour_search(
            empty_kdtree, query_point
        )

        # With an empty KD-Tree, nearest_point should be None
        self.assertIsNone(nearest_point)
        self.assertEqual(nearest_dist, float("inf"))
        self.assertEqual(nodes_visited, 0)

if __name__ == '__main__':
    unittest.main()
