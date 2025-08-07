"""
Comprehensive tests for Johnson's Algorithm implementation.

This module contains unit tests for all components of Johnson's Algorithm:
- Graph data structure
- Bellman-Ford algorithm
- Dijkstra's algorithm
- Johnson's algorithm main implementation

Author: Zakariae Fakhri
Date: August 2025
"""

import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from graphs.johnsons_algorithm import Graph, JohnsonsAlgorithm
from graphs.bellman_ford import BellmanFord
from graphs.dijkstra import Dijkstra


class TestGraph(unittest.TestCase):
    """Test cases for the Graph class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.graph = Graph()
    
    def test_empty_graph(self):
        """Test empty graph properties."""
        self.assertTrue(self.graph.is_empty())
        self.assertEqual(self.graph.get_vertex_count(), 0)
        self.assertEqual(self.graph.get_edge_count(), 0)
        self.assertEqual(len(self.graph.get_vertices()), 0)
    
    def test_add_single_edge(self):
        """Test adding a single edge."""
        self.graph.add_edge(1, 2, 5.0)
        
        self.assertFalse(self.graph.is_empty())
        self.assertEqual(self.graph.get_vertex_count(), 2)
        self.assertEqual(self.graph.get_edge_count(), 1)
        self.assertTrue(self.graph.has_vertex(1))
        self.assertTrue(self.graph.has_vertex(2))
        self.assertTrue(self.graph.has_edge(1, 2))
        self.assertFalse(self.graph.has_edge(2, 1))
        self.assertEqual(self.graph.get_edge_weight(1, 2), 5.0)
    
    def test_add_multiple_edges(self):
        """Test adding multiple edges."""
        edges = [(1, 2, -1), (2, 3, 4), (3, 1, 2)]
        self.graph.add_edges(edges)
        
        self.assertEqual(self.graph.get_vertex_count(), 3)
        self.assertEqual(self.graph.get_edge_count(), 3)
        self.assertEqual(self.graph.get_edge_weight(1, 2), -1)
        self.assertEqual(self.graph.get_edge_weight(2, 3), 4)
        self.assertEqual(self.graph.get_edge_weight(3, 1), 2)
    
    def test_neighbors(self):
        """Test getting neighbors of vertices."""
        self.graph.add_edge(1, 2, 3)
        self.graph.add_edge(1, 3, 4)
        self.graph.add_edge(2, 3, 1)
        
        neighbors_1 = self.graph.get_neighbors(1)
        self.assertEqual(len(neighbors_1), 2)
        self.assertIn((2, 3), neighbors_1)
        self.assertIn((3, 4), neighbors_1)
        
        neighbors_2 = self.graph.get_neighbors(2)
        self.assertEqual(len(neighbors_2), 1)
        self.assertIn((3, 1), neighbors_2)
    
    def test_copy_graph(self):
        """Test copying a graph."""
        self.graph.add_edge(1, 2, 5)
        self.graph.add_edge(2, 3, -2)
        
        copy_graph = self.graph.copy()
        
        self.assertEqual(copy_graph.get_vertex_count(), self.graph.get_vertex_count())
        self.assertEqual(copy_graph.get_edge_count(), self.graph.get_edge_count())
        self.assertEqual(copy_graph.get_edge_weight(1, 2), 5)
        self.assertEqual(copy_graph.get_edge_weight(2, 3), -2)
        
        # Modify original, copy should remain unchanged
        self.graph.add_edge(3, 4, 1)
        self.assertEqual(self.graph.get_edge_count(), 3)
        self.assertEqual(copy_graph.get_edge_count(), 2)


class TestBellmanFord(unittest.TestCase):
    """Test cases for the Bellman-Ford algorithm."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.graph = Graph()
    
    def test_single_vertex(self):
        """Test Bellman-Ford with a single vertex."""
        self.graph.add_edge(1, 1, 0)  # Self-loop
        bf = BellmanFord(self.graph)
        distances = bf.find_shortest_paths(1)
        
        self.assertIsNotNone(distances)
        self.assertEqual(distances[1], 0)
    
    def test_simple_path(self):
        """Test Bellman-Ford with a simple path."""
        self.graph.add_edge(1, 2, 3)
        self.graph.add_edge(2, 3, 4)
        
        bf = BellmanFord(self.graph)
        distances = bf.find_shortest_paths(1)
        
        self.assertIsNotNone(distances)
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 3)
        self.assertEqual(distances[3], 7)
    
    def test_negative_edges(self):
        """Test Bellman-Ford with negative edges but no negative cycles."""
        self.graph.add_edge(1, 2, -1)
        self.graph.add_edge(2, 3, 4)
        self.graph.add_edge(1, 3, 2)
        
        bf = BellmanFord(self.graph)
        distances = bf.find_shortest_paths(1)
        
        self.assertIsNotNone(distances)
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], -1)
        self.assertEqual(distances[3], 2)  # min(2, -1+4) = 2
    
    def test_negative_cycle_detection(self):
        """Test Bellman-Ford negative cycle detection."""
        # Create a negative cycle: 1 -> 2 -> 3 -> 1 with total weight -1
        self.graph.add_edge(1, 2, 1)
        self.graph.add_edge(2, 3, -4)
        self.graph.add_edge(3, 1, 2)
        
        bf = BellmanFord(self.graph)
        distances = bf.find_shortest_paths(1)
        
        self.assertIsNone(distances)  # Should detect negative cycle
    
    def test_unreachable_vertices(self):
        """Test Bellman-Ford with unreachable vertices."""
        self.graph.add_edge(1, 2, 1)
        self.graph.add_edge(3, 4, 1)  # Separate component
        
        bf = BellmanFord(self.graph)
        distances = bf.find_shortest_paths(1)
        
        self.assertIsNotNone(distances)
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 1)
        self.assertEqual(distances[3], float('inf'))
        self.assertEqual(distances[4], float('inf'))
    
    def test_get_path(self):
        """Test path reconstruction in Bellman-Ford."""
        self.graph.add_edge(1, 2, 1)
        self.graph.add_edge(2, 3, 2)
        self.graph.add_edge(1, 3, 5)
        
        bf = BellmanFord(self.graph)
        distances = bf.find_shortest_paths(1)
        path = bf.get_path(1, 3)
        
        self.assertIsNotNone(distances)
        self.assertEqual(path, [1, 2, 3])  # Should use shorter path
        self.assertEqual(distances[3], 3)


class TestDijkstra(unittest.TestCase):
    """Test cases for Dijkstra's algorithm."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.graph = Graph()
    
    def test_simple_path(self):
        """Test Dijkstra with a simple path."""
        self.graph.add_edge(1, 2, 3)
        self.graph.add_edge(2, 3, 4)
        self.graph.add_edge(1, 3, 10)
        
        dijkstra = Dijkstra(self.graph)
        distances = dijkstra.find_shortest_paths(1)
        
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 3)
        self.assertEqual(distances[3], 7)  # 3 + 4 < 10
    
    def test_complex_graph(self):
        """Test Dijkstra with a more complex graph."""
        edges = [
            (1, 2, 4), (1, 3, 2),
            (2, 3, 1), (2, 4, 5),
            (3, 4, 8), (3, 5, 10),
            (4, 5, 2)
        ]
        self.graph.add_edges(edges)
        
        dijkstra = Dijkstra(self.graph)
        distances = dijkstra.find_shortest_paths(1)
        
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 4)  # Direct edge 1->2: 4
        self.assertEqual(distances[3], 2)
        self.assertEqual(distances[4], 9)  # 1->2->4: 4+5 = 9
        self.assertEqual(distances[5], 11) # 1->2->4->5: 4+5+2 = 11
    
    def test_unreachable_vertices(self):
        """Test Dijkstra with unreachable vertices."""
        self.graph.add_edge(1, 2, 1)
        self.graph.add_edge(3, 4, 1)
        
        dijkstra = Dijkstra(self.graph)
        distances = dijkstra.find_shortest_paths(1)
        
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 1)
        self.assertEqual(distances[3], float('inf'))
        self.assertEqual(distances[4], float('inf'))
    
    def test_get_path(self):
        """Test path reconstruction in Dijkstra."""
        self.graph.add_edge(1, 2, 1)
        self.graph.add_edge(2, 3, 2)
        self.graph.add_edge(1, 3, 5)
        
        dijkstra = Dijkstra(self.graph)
        distances = dijkstra.find_shortest_paths(1)
        path = dijkstra.get_path(1, 3)
        
        self.assertEqual(path, [1, 2, 3])
        self.assertEqual(distances[3], 3)


class TestJohnsonsAlgorithm(unittest.TestCase):
    """Test cases for Johnson's Algorithm."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.graph = Graph()
    
    def test_empty_graph(self):
        """Test Johnson's algorithm with empty graph."""
        johnson = JohnsonsAlgorithm(self.graph)
        result = johnson.find_all_pairs_shortest_paths()
        
        self.assertEqual(result, {})
    
    def test_single_vertex(self):
        """Test Johnson's algorithm with single vertex."""
        # Need at least one edge to create a vertex
        self.graph.add_edge(1, 1, 0)
        johnson = JohnsonsAlgorithm(self.graph)
        result = johnson.find_all_pairs_shortest_paths()
        
        self.assertIsNotNone(result)
        self.assertEqual(result[1][1], 0)
    
    def test_simple_graph_positive_weights(self):
        """Test Johnson's algorithm with positive weights only."""
        edges = [
            (1, 2, 3),
            (2, 3, 4),
            (1, 3, 10)
        ]
        self.graph.add_edges(edges)
        
        johnson = JohnsonsAlgorithm(self.graph)
        result = johnson.find_all_pairs_shortest_paths()
        
        self.assertIsNotNone(result)
        
        # Check some key distances
        self.assertEqual(result[1][1], 0)
        self.assertEqual(result[1][2], 3)
        self.assertEqual(result[1][3], 7)  # 1->2->3: 3+4 = 7
        self.assertEqual(result[2][2], 0)
        self.assertEqual(result[2][3], 4)
        self.assertEqual(result[3][3], 0)
        
        # Unreachable paths should be infinity
        self.assertEqual(result[2][1], float('inf'))
        self.assertEqual(result[3][1], float('inf'))
        self.assertEqual(result[3][2], float('inf'))
    
    def test_graph_with_negative_weights(self):
        """Test Johnson's algorithm with negative weights (no negative cycles)."""
        edges = [
            (1, 2, -1),
            (1, 3, 4),
            (2, 3, 3),
            (2, 4, 2),
            (3, 4, -5),
            (4, 1, 6)
        ]
        self.graph.add_edges(edges)
        
        johnson = JohnsonsAlgorithm(self.graph)
        result = johnson.find_all_pairs_shortest_paths()
        
        self.assertIsNotNone(result)
        
        # Test some specific shortest paths
        self.assertEqual(result[1][1], 0)
        self.assertEqual(result[1][2], -1)
        self.assertEqual(result[1][4], -3)  # 1->3->4: 4+(-5) = -1, but 1->2->3->4: -1+3+(-5) = -3
        self.assertEqual(result[3][4], -5)
    
    def test_negative_cycle_detection(self):
        """Test Johnson's algorithm negative cycle detection."""
        # Create a negative cycle
        edges = [
            (1, 2, 1),
            (2, 3, -4),
            (3, 1, 2)  # Total cycle weight: 1 + (-4) + 2 = -1
        ]
        self.graph.add_edges(edges)
        
        johnson = JohnsonsAlgorithm(self.graph)
        result = johnson.find_all_pairs_shortest_paths()
        
        self.assertIsNone(result)  # Should detect negative cycle
        # Note: has_negative_cycle only returns True after find_all_pairs_shortest_paths is called and returns None
    
    def test_string_vertices(self):
        """Test Johnson's algorithm with string vertices."""
        edges = [
            ('A', 'B', 1),
            ('A', 'C', 4),
            ('B', 'C', -3),
            ('B', 'D', 2),
            ('C', 'D', 3),
            ('D', 'A', -1)
        ]
        self.graph.add_edges(edges)
        
        johnson = JohnsonsAlgorithm(self.graph)
        result = johnson.find_all_pairs_shortest_paths()
        
        self.assertIsNotNone(result)
        
        # Test some specific distances
        self.assertEqual(result['A']['A'], 0)
        self.assertEqual(result['A']['B'], 1)
        self.assertEqual(result['A']['C'], -2)  # A->B->C: 1+(-3) = -2
        self.assertEqual(result['B']['C'], -3)
        self.assertEqual(result['D']['A'], -1)
    
    def test_get_shortest_path_method(self):
        """Test the get_shortest_path convenience method."""
        edges = [(1, 2, 3), (2, 3, 4)]
        self.graph.add_edges(edges)
        
        johnson = JohnsonsAlgorithm(self.graph)
        result = johnson.find_all_pairs_shortest_paths()
        
        self.assertEqual(johnson.get_shortest_path(1, 3), 7)
        self.assertEqual(johnson.get_shortest_path(1, 1), 0)
        self.assertEqual(johnson.get_shortest_path(2, 1), float('inf'))
    
    def test_algorithm_suitability_check(self):
        """Test the static method for checking algorithm suitability."""
        # Empty graph
        empty_graph = Graph()
        suitable, reason = JohnsonsAlgorithm.is_suitable_for_johnson(empty_graph)
        self.assertFalse(suitable)
        self.assertIn("empty", reason.lower())
        
        # Graph with negative cycle
        neg_cycle_graph = Graph()
        neg_cycle_graph.add_edges([(1, 2, 1), (2, 3, -4), (3, 1, 2)])
        suitable, reason = JohnsonsAlgorithm.is_suitable_for_johnson(neg_cycle_graph)
        self.assertFalse(suitable)
        self.assertIn("negative cycle", reason.lower())
        
        # Good graph for Johnson's
        good_graph = Graph()
        good_graph.add_edges([(1, 2, -1), (2, 3, 4), (3, 4, 2)])
        suitable, reason = JohnsonsAlgorithm.is_suitable_for_johnson(good_graph)
        self.assertTrue(suitable)


class TestIntegration(unittest.TestCase):
    """Integration tests comparing Johnson's with individual algorithms."""
    
    def test_johnson_vs_dijkstra_positive_weights(self):
        """Compare Johnson's with Dijkstra on positive weight graph."""
        graph = Graph()
        edges = [(1, 2, 3), (2, 3, 4), (1, 3, 10), (3, 4, 1)]
        graph.add_edges(edges)
        
        # Johnson's algorithm
        johnson = JohnsonsAlgorithm(graph)
        johnson_result = johnson.find_all_pairs_shortest_paths()
        
        # Dijkstra from vertex 1
        dijkstra = Dijkstra(graph)
        dijkstra_distances = dijkstra.find_shortest_paths(1)
        
        # Compare results for vertex 1
        for vertex in graph.get_vertices():
            self.assertEqual(
                johnson_result[1][vertex], 
                dijkstra_distances[vertex],
                f"Mismatch for vertex {vertex}"
            )
    
    def test_performance_comparison(self):
        """Basic performance test to ensure algorithms complete."""
        # Create a moderately sized graph
        graph = Graph()
        
        # Create a grid-like graph
        for i in range(1, 6):
            for j in range(1, 6):
                if i < 5:
                    graph.add_edge(i*5 + j, (i+1)*5 + j, 1)
                if j < 5:
                    graph.add_edge(i*5 + j, i*5 + (j+1), 1)
        
        # Add some negative edges
        graph.add_edge(6, 11, -2)
        graph.add_edge(12, 17, -1)
        
        johnson = JohnsonsAlgorithm(graph)
        result = johnson.find_all_pairs_shortest_paths()
        
        self.assertIsNotNone(result)
        self.assertEqual(len(result), graph.get_vertex_count())


def run_tests():
    """Run all tests and display results."""
    # Create test suite
    test_classes = [
        TestGraph,
        TestBellmanFord, 
        TestDijkstra,
        TestJohnsonsAlgorithm,
        TestIntegration
    ]
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print(f"\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split('AssertionError:')[-1].strip()}")
    
    if result.errors:
        print(f"\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback.split('Exception:')[-1].strip()}")
    
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun) * 100
    print(f"\nSuccess rate: {success_rate:.1f}%")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
