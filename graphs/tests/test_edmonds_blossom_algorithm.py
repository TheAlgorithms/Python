import unittest
from collections import deque

from graphs.edmonds_blossom_algorithm import (
    UNMATCHED,
    BlossomAuxData,
    BlossomData,
    EdmondsBlossomAlgorithm,
)


class TestEdmondsBlossomAlgorithm(unittest.TestCase):
    def test_maximum_matching(self):
        # Test case: Basic matching in a simple graph
        edges = [(0, 1), (1, 2), (2, 3)]
        vertex_count = 4
        result = EdmondsBlossomAlgorithm.maximum_matching(edges, vertex_count)
        expected_result = [(0, 1), (2, 3)]
        assert result == expected_result

        # Test case: Graph with no matching
        edges = []
        vertex_count = 4
        result = EdmondsBlossomAlgorithm.maximum_matching(edges, vertex_count)
        expected_result = []
        assert result == expected_result

    def test_update_matching(self):
        # Test case: Update matching on a simple augmenting path
        match = [UNMATCHED, UNMATCHED, UNMATCHED]
        parent = [1, 0, UNMATCHED]
        current_vertex = 2
        EdmondsBlossomAlgorithm.update_matching(match, parent, current_vertex)
        expected_result = [1, 0, UNMATCHED]
        assert match == expected_result

    def test_find_base(self):
        # Test case: Find base of blossom
        base = [0, 1, 2, 3]
        parent = [1, 0, UNMATCHED, UNMATCHED]
        vertex_u = 2
        vertex_v = 3
        result = EdmondsBlossomAlgorithm.find_base(base, parent, vertex_u, vertex_v)
        expected_result = 2
        assert result == expected_result

    def test_contract_blossom(self):
        # Test case: Contracting a simple blossom
        queue = deque()
        parent = [UNMATCHED, UNMATCHED, UNMATCHED]
        base = [0, 1, 2]
        in_blossom = [False] * 3
        match = [UNMATCHED, UNMATCHED, UNMATCHED]
        in_queue = [False] * 3
        aux_data = BlossomAuxData(queue, parent, base, in_blossom, match, in_queue)
        blossom_data = BlossomData(aux_data, 0, 1, 2)

        # Contract the blossom
        EdmondsBlossomAlgorithm.contract_blossom(blossom_data)

        # Ensure base is updated correctly
        assert aux_data.base == [2, 2, 2]
        # Check that the queue has the contracted vertices
        assert 0 in aux_data.queue
        assert 1 in aux_data.queue
        assert aux_data.in_queue[0]
        assert aux_data.in_queue[1]


if __name__ == "__main__":
    unittest.main()
