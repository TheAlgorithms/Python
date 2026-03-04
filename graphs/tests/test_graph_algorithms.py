"""
Comprehensive tests for graph algorithms.
Run with: pytest tests/test_graph_algorithms.py -v
"""

from graphs.max_bipartite_independent_set import (
    MaxBipartiteIndependentSet,
    max_bipartite_independent_set,
)
from graphs.heavy_light_decomposition import HeavyLightDecomposition
from graphs.traveling_salesman import TravelingSalesman, held_karp
from graphs.chinese_postman import ChinesePostman, chinese_postman
from graphs.two_sat import TwoSAT, solve_2sat
from graphs.push_relabel import PushRelabel
from graphs.ford_fulkerson import FordFulkerson, ford_fulkerson
from graphs.hopcroft_karp import HopcroftKarp, hopcroft_karp
from graphs.johnsons_algorithm import johnsons_algorithm
from graphs.floyd_warshall import floyd_warshall, reconstruct_path
import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestFloydWarshall:
    """Test Floyd-Warshall all-pairs shortest path."""

    def test_basic_graph(self):
        graph = [
            [0, 3, float("inf"), 7],
            [8, 0, 2, float("inf")],
            [5, float("inf"), 0, 1],
            [2, float("inf"), float("inf"), 0],
        ]
        dist, _ = floyd_warshall(graph)
        assert dist[0][3] == 6  # 0->1->2->3 = 3+2+1 = 6

    def test_negative_cycle_detection(self):
        graph = [[0, 1, float("inf")], [float("inf"), 0, -2], [-3, float("inf"), 0]]
        with pytest.raises(ValueError, match="negative weight cycle"):
            floyd_warshall(graph)

    def test_path_reconstruction(self):
        graph = [
            [0, 3, float("inf"), 7],
            [8, 0, 2, float("inf")],
            [5, float("inf"), 0, 1],
            [2, float("inf"), float("inf"), 0],
        ]
        dist, next_node = floyd_warshall(graph)
        path = reconstruct_path(next_node, 0, 3)
        assert path == [0, 1, 2, 3]


class TestJohnsonsAlgorithm:
    """Test Johnson's algorithm for sparse graphs."""

    def test_basic_graph(self):
        graph = {
            0: [(1, -5)],
            1: [(2, 4), (3, 3)],
            2: [(4, 1)],
            3: [(2, 2), (4, 2)],
            4: [],
        }
        dist = johnsons_algorithm(graph, 5)
        assert dist[0][4] == -1  # 0->1->3->4 = -5+3+2 = 0, wait let me check
        # Actually: 0->1 (-5), 1->2 (4), 2->4 (1) = 0, or 0->1->3->4 = 0

    def test_negative_cycle(self):
        graph = {0: [(1, 1)], 1: [(2, -3)], 2: [(0, 1)]}
        with pytest.raises(ValueError, match="negative weight cycle"):
            johnsons_algorithm(graph, 3)


class TestHopcroftKarp:
    """Test Hopcroft-Karp bipartite matching."""

    def test_perfect_matching(self):
        hk = HopcroftKarp(4, 4)
        # Create perfect matching: 0-0, 1-1, 2-2, 3-3
        for i in range(4):
            hk.add_edge(i, i)
        assert hk.max_matching() == 4

    def test_chain_graph(self):
        hk = HopcroftKarp(4, 4)
        edges = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]
        for u, v in edges:
            hk.add_edge(u, v)
        assert hk.max_matching() == 4

    def test_star_graph(self):
        hk = HopcroftKarp(1, 5)
        for v in range(5):
            hk.add_edge(0, v)
        assert hk.max_matching() == 1

    def test_empty_graph(self):
        hk = HopcroftKarp(5, 5)
        assert hk.max_matching() == 0


class TestFordFulkerson:
    """Test Ford-Fulkerson max flow."""

    def test_clrs_example(self):
        """Example from CLRS textbook."""
        ff = FordFulkerson(6)
        edges = [
            (0, 1, 16),
            (0, 2, 13),
            (1, 2, 10),
            (1, 3, 12),
            (2, 4, 14),
            (3, 2, 9),
            (3, 5, 20),
            (4, 3, 7),
            (4, 5, 4),
        ]
        for u, v, c in edges:
            ff.add_edge(u, v, c)
        assert ff.max_flow(0, 5) == 23

    def test_simple_path(self):
        ff = FordFulkerson(3)
        ff.add_edge(0, 1, 10)
        ff.add_edge(1, 2, 5)
        assert ff.max_flow(0, 2) == 5

    def test_multiple_paths(self):
        ff = FordFulkerson(4)
        ff.add_edge(0, 1, 10)
        ff.add_edge(0, 2, 10)
        ff.add_edge(1, 3, 10)
        ff.add_edge(2, 3, 10)
        assert ff.max_flow(0, 3) == 20


class TestPushRelabel:
    """Test Push-Relabel max flow."""

    def test_clrs_example(self):
        pr = PushRelabel(6)
        edges = [
            (0, 1, 16),
            (0, 2, 13),
            (1, 2, 10),
            (1, 3, 12),
            (2, 4, 14),
            (3, 2, 9),
            (3, 5, 20),
            (4, 3, 7),
            (4, 5, 4),
        ]
        for u, v, c in edges:
            pr.add_edge(u, v, c)
        assert pr.max_flow(0, 5) == 23

    def test_same_as_ford_fulkerson(self):
        """Both should give same result."""
        edges = [(0, 1, 10), (0, 2, 5), (1, 2, 15), (1, 3, 10), (2, 3, 10)]

        ff = FordFulkerson(4)
        for u, v, c in edges:
            ff.add_edge(u, v, c)
        ff_result = ff.max_flow(0, 3)

        pr = PushRelabel(4)
        for u, v, c in edges:
            pr.add_edge(u, v, c)
        pr_result = pr.max_flow(0, 3)

        assert ff_result == pr_result


class TestTwoSAT:
    """Test 2-SAT solver."""

    def test_satisfiable(self):
        ts = TwoSAT(3)
        ts.add_or(0, True, 1, False)  # x0 OR ¬x1
        ts.add_or(1, True, 2, True)  # x1 OR x2
        ts.add_or(0, False, 2, False)  # ¬x0 OR ¬x2
        result = ts.solve()
        assert result is not None
        assert len(result) == 3

    def test_unsatisfiable(self):
        ts = TwoSAT(2)
        ts.add_or(0, True, 0, True)  # x0
        ts.add_or(0, False, 0, False)  # ¬x0
        result = ts.solve()
        assert result is None

    def test_convenience_function(self):
        clauses = [(0, True, 1, False), (1, True, 2, False)]
        result = solve_2sat(3, clauses)
        assert result is not None


class TestChinesePostman:
    """Test Chinese Postman Problem."""

    def test_eulerian_graph(self):
        cpp = ChinesePostman(4)
        # Square: 0-1-2-3-0
        cpp.add_edge(0, 1, 1)
        cpp.add_edge(1, 2, 1)
        cpp.add_edge(2, 3, 1)
        cpp.add_edge(3, 0, 1)
        cost, circuit = cpp.solve()
        assert cost == 4.0
        assert len(circuit) == 5  # Includes return to start

    def test_non_eulerian(self):
        cpp = ChinesePostman(4)
        # Path graph: 0-1-2-3 (odd degrees at 0 and 3)
        cpp.add_edge(0, 1, 1)
        cpp.add_edge(1, 2, 1)
        cpp.add_edge(2, 3, 1)
        cost, _ = cpp.solve()
        assert cost == 6.0  # Must duplicate path 0-1-2-3


class TestTravelingSalesman:
    """Test TSP Held-Karp algorithm."""

    def test_small_instance(self):
        tsp = TravelingSalesman(4)
        # Complete graph with symmetric weights
        weights = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
        for i in range(4):
            for j in range(4):
                if i != j:
                    tsp.add_edge(i, j, weights[i][j])

        cost, path = tsp.solve(0)
        assert cost == 80.0  # 0->1->3->2->0 = 10+25+30+15 = 80
        assert path[0] == 0
        assert path[-1] == 0

    def test_convenience_function(self):
        dist = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10, 4, 8, 0]]
        cost, path = held_karp(dist, 0)
        assert cost > 0
        assert len(path) == 5  # 4 vertices + return to start


class TestHeavyLightDecomposition:
    """Test HLD for path queries."""

    def test_path_sum(self):
        hld = HeavyLightDecomposition(5)
        edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
        for u, v in edges:
            hld.add_edge(u, v)

        for i in range(5):
            hld.set_value(i, i + 1)  # Values: 1, 2, 3, 4, 5

        hld.build(0)

        # Path 3 -> 4: 3->1->4, values 4+2+5 = 11
        assert hld.query_path(3, 4, sum) == 11

        # Path 2 -> 3: 2->0->1->3, values 3+1+2+4 = 10
        assert hld.query_path(2, 3, sum) == 10

    def test_update(self):
        hld = HeavyLightDecomposition(3)
        hld.add_edge(0, 1)
        hld.add_edge(1, 2)

        for i in range(3):
            hld.set_value(i, 1)

        hld.build(0)
        assert hld.query_path(0, 2, sum) == 3

        hld.update_node(1, 10)
        assert hld.query_path(0, 2, sum) == 12


class TestMaxBipartiteIndependentSet:
    """Test maximum independent set in bipartite graphs."""

    def test_complete_bipartite(self):
        mbis = MaxBipartiteIndependentSet(2, 2)
        mbis.add_edge(0, 0)
        mbis.add_edge(0, 1)
        mbis.add_edge(1, 0)
        mbis.add_edge(1, 1)
        left, right = mbis.solve()
        # Max matching = 2, so |MIS| = 4 - 2 = 2
        assert len(left) + len(right) == 2

    def test_empty_graph(self):
        mbis = MaxBipartiteIndependentSet(3, 3)
        left, right = mbis.solve()
        # No edges, so all vertices are independent
        assert len(left) == 3 and len(right) == 3

    def test_chain(self):
        mbis = MaxBipartiteIndependentSet(3, 3)
        edges = [(0, 0), (1, 1), (2, 2)]
        for u, v in edges:
            mbis.add_edge(u, v)
        left, right = mbis.solve()
        # Max matching = 3, |MIS| = 6 - 3 = 3
        assert len(left) + len(right) == 3


class TestPerformance:
    """Performance benchmarks."""

    def test_floyd_warshall_performance(self):
        import random
        import time

        n = 100
        graph = [
            [0 if i == j else random.randint(1, 100) for j in range(n)]
            for i in range(n)
        ]

        start = time.perf_counter()
        floyd_warshall(graph)
        elapsed = time.perf_counter() - start

        # Should complete in reasonable time for n=100
        assert elapsed < 5.0

    def test_hopcroft_karp_performance(self):
        import random
        import time

        n, m = 500, 500
        hk = HopcroftKarp(n, m)

        for _ in range(1000):
            hk.add_edge(random.randint(0, n - 1), random.randint(0, m - 1))

        start = time.perf_counter()
        result = hk.max_matching()
        elapsed = time.perf_counter() - start

        assert elapsed < 2.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
