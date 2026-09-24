import unittest

from graphs.edmonds_blossom_algorithm import EdmondsBlossomAlgorithm


class EdmondsBlossomAlgorithmTest(unittest.TestCase):
    def convert_matching_to_array(self, matching):
        """Helper method to convert a
        list of matching pairs into a sorted 2D array.
        """
        # Convert the list of pairs into a list of lists
        result = [list(pair) for pair in matching]

        # Sort each individual pair for consistency
        for pair in result:
            pair.sort()

        # Sort the array of pairs to ensure consistent order
        result.sort(key=lambda x: x[0])
        return result

    def test_case_1(self):
        """Test Case 1: A triangle graph where vertices 0, 1, and 2 form a cycle."""
        edges = [[0, 1], [1, 2], [2, 0]]
        matching = EdmondsBlossomAlgorithm.maximum_matching(edges, 3)

        expected = [[0, 1]]
        assert expected == self.convert_matching_to_array(matching)

    def test_case_2(self):
        """Test Case 2: A disconnected graph with two components."""
        edges = [[0, 1], [1, 2], [3, 4]]
        matching = EdmondsBlossomAlgorithm.maximum_matching(edges, 5)

        expected = [[0, 1], [3, 4]]
        assert expected == self.convert_matching_to_array(matching)

    def test_case_3(self):
        """Test Case 3: A cycle graph with an additional edge outside the cycle."""
        edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5]]
        matching = EdmondsBlossomAlgorithm.maximum_matching(edges, 6)

        expected = [[0, 1], [2, 3], [4, 5]]
        assert expected == self.convert_matching_to_array(matching)

    def test_case_no_matching(self):
        """Test Case 4: A graph with no edges."""
        edges = []  # No edges
        matching = EdmondsBlossomAlgorithm.maximum_matching(edges, 3)

        expected = []
        assert expected == self.convert_matching_to_array(matching)

    def test_case_large_graph(self):
        """Test Case 5: A complex graph with multiple cycles and extra edges."""
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [1, 4], [2, 5]]
        matching = EdmondsBlossomAlgorithm.maximum_matching(edges, 6)

        # Check if the size of the matching is correct (i.e., 3 pairs)
        assert len(matching) == 3

        # Check that the result contains valid pairs (any order is fine)
        possible_matching_1 = [[0, 1], [2, 5], [3, 4]]
        possible_matching_2 = [[0, 1], [2, 3], [4, 5]]
        result = self.convert_matching_to_array(matching)

        # Assert that the result is one of the valid maximum matchings
        assert result in (possible_matching_1, possible_matching_2)


if __name__ == "__main__":
    unittest.main()
