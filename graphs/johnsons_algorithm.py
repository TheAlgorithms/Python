"""
Johnson's Algorithm for All-Pairs Shortest Path
Implementation by: Zakaria Fakhri
Date: August 2025

Johnson's Algorithm is used to find the shortest paths between all pairs of vertices
in a weighted directed graph. It works well for sparse graphs and handles negative
edge weights (but not negative cycles).

Algorithm Steps:
1. Add a new vertex connected to all vertices with weight 0
2. Run Bellman-Ford from the new vertex to detect negative cycles and get potentials
3. Reweight all edges using the potentials to make them non-negative
4. Run Dijkstra from each vertex on the reweighted graph
5. Convert distances back using the original potentials

Time Complexity: O(V²log(V) + VE)
Space Complexity: O(V²)
"""

from collections import defaultdict
from typing import Dict, Any, Optional, List, Tuple
from .bellman_ford import BellmanFord
from .dijkstra import Dijkstra


class Graph:
    """
    A weighted directed graph implementation using adjacency list representation.
    """

    def __init__(self):
        """Initialize an empty graph."""
        self.adjacency_list = defaultdict(list)
        self.vertices = set()
        self._edge_count = 0

    def add_edge(self, source: Any, destination: Any, weight: float) -> None:
        """Add a weighted edge to the graph."""
        self.adjacency_list[source].append((destination, weight))
        self.vertices.add(source)
        self.vertices.add(destination)
        self._edge_count += 1

    def add_edges(self, edges: List[Tuple[Any, Any, float]]) -> None:
        """Add multiple edges to the graph."""
        for source, destination, weight in edges:
            self.add_edge(source, destination, weight)

    def get_neighbors(self, vertex: Any) -> List[Tuple[Any, float]]:
        """Get all neighbors of a vertex with their edge weights."""
        return self.adjacency_list.get(vertex, [])

    def get_vertices(self) -> set:
        """Get all vertices in the graph."""
        return self.vertices.copy()

    def get_vertex_count(self) -> int:
        """Get the number of vertices in the graph."""
        return len(self.vertices)

    def get_edge_count(self) -> int:
        """Get the number of edges in the graph."""
        return self._edge_count

    def has_vertex(self, vertex: Any) -> bool:
        """Check if a vertex exists in the graph."""
        return vertex in self.vertices

    def has_edge(self, source: Any, destination: Any) -> bool:
        """Check if an edge exists between two vertices."""
        for neighbor, _ in self.adjacency_list.get(source, []):
            if neighbor == destination:
                return True
        return False

    def get_edge_weight(self, source: Any, destination: Any) -> Optional[float]:
        """Get the weight of an edge between two vertices."""
        for neighbor, weight in self.adjacency_list.get(source, []):
            if neighbor == destination:
                return weight
        return None

    def is_empty(self) -> bool:
        """Check if the graph is empty (no vertices)."""
        return len(self.vertices) == 0

    def copy(self) -> "Graph":
        """Create a copy of the graph."""
        new_graph = Graph()
        for vertex in self.adjacency_list:
            for neighbor, weight in self.adjacency_list[vertex]:
                new_graph.add_edge(vertex, neighbor, weight)
        return new_graph

    def to_dict(self) -> Dict[Any, List[Tuple[Any, float]]]:
        """Convert the graph to a dictionary representation."""
        return dict(self.adjacency_list)


class JohnsonsAlgorithm:
    """
    Implementation of Johnson's Algorithm for All-Pairs Shortest Path problem.

    This class handles weighted directed graphs and finds shortest paths between
    all pairs of vertices efficiently, even with negative edge weights.
    """

    def __init__(self, graph: Graph):
        """
        Initialize Johnson's Algorithm with a graph.

        Args:
            graph: The weighted directed graph to process
        """
        self.original_graph = graph
        self.potentials = {}
        self.reweighted_graph = None
        self.all_pairs_distances = {}

    def find_all_pairs_shortest_paths(self) -> Optional[Dict[Any, Dict[Any, float]]]:
        """
        Find shortest paths between all pairs of vertices using Johnson's Algorithm.

        Returns:
            Dictionary of source -> {destination -> distance}, or None if negative cycle exists
        """
        if self.original_graph.is_empty():
            return {}

        # Step 1: Create graph with extra vertex
        graph_with_extra = self._create_graph_with_extra_vertex()
        extra_vertex = self._get_extra_vertex_name()

        # Step 2: Run Bellman-Ford from extra vertex to get potentials
        print("Running Bellman-Ford to compute potentials...")
        if not self._compute_potentials(graph_with_extra, extra_vertex):
            return None  # Negative cycle detected

        # Step 3: Reweight edges to make them non-negative
        print("Reweighting edges...")
        self._reweight_edges()

        # Step 4: Run Dijkstra from each vertex
        print("Running Dijkstra from each vertex...")
        self._compute_all_pairs_distances()

        # Step 5: Convert distances back to original weights
        self._convert_distances_to_original()

        return self.all_pairs_distances

    def _get_extra_vertex_name(self) -> str:
        """Generate a unique name for the extra vertex."""
        base_name = "extra_vertex_johnson"
        extra_vertex = base_name
        counter = 0

        while self.original_graph.has_vertex(extra_vertex):
            counter += 1
            extra_vertex = f"{base_name}_{counter}"

        return extra_vertex

    def _create_graph_with_extra_vertex(self) -> Graph:
        """Create a copy of the original graph with an extra vertex."""
        graph_with_extra = self.original_graph.copy()
        extra_vertex = self._get_extra_vertex_name()

        # Add edges from extra vertex to all original vertices with weight 0
        for vertex in self.original_graph.get_vertices():
            graph_with_extra.add_edge(extra_vertex, vertex, 0)

        return graph_with_extra

    def _compute_potentials(self, graph_with_extra: Graph, extra_vertex: str) -> bool:
        """Compute potentials using Bellman-Ford algorithm."""
        bellman_ford = BellmanFord(graph_with_extra)
        distances = bellman_ford.find_shortest_paths(extra_vertex)

        if distances is None:
            return False  # Negative cycle detected

        # Store potentials (exclude extra vertex)
        self.potentials = {v: distances[v] for v in self.original_graph.get_vertices()}
        return True

    def _reweight_edges(self) -> None:
        """Reweight all edges to make them non-negative using the computed potentials."""
        self.reweighted_graph = Graph()

        for vertex in self.original_graph.get_vertices():
            for neighbor, weight in self.original_graph.get_neighbors(vertex):
                # Reweight the edge
                new_weight = (
                    weight + self.potentials[vertex] - self.potentials[neighbor]
                )
                self.reweighted_graph.add_edge(vertex, neighbor, new_weight)

    def _compute_all_pairs_distances(self) -> None:
        """Run Dijkstra's algorithm from each vertex on the reweighted graph."""
        self.all_pairs_distances = {}

        for start_vertex in self.original_graph.get_vertices():
            dijkstra = Dijkstra(self.reweighted_graph)
            distances = dijkstra.find_shortest_paths(start_vertex)
            self.all_pairs_distances[start_vertex] = distances

    def _convert_distances_to_original(self) -> None:
        """Convert the distances back to original weights using potentials."""
        for start_vertex in self.all_pairs_distances:
            original_distances = {}

            for end_vertex in self.all_pairs_distances[start_vertex]:
                reweighted_distance = self.all_pairs_distances[start_vertex][end_vertex]

                if reweighted_distance != float("inf"):
                    # Convert back to original distance
                    original_distance = (
                        reweighted_distance
                        - self.potentials[start_vertex]
                        + self.potentials[end_vertex]
                    )
                    original_distances[end_vertex] = original_distance
                else:
                    original_distances[end_vertex] = float("inf")

            self.all_pairs_distances[start_vertex] = original_distances

    def get_shortest_path(self, source: Any, destination: Any) -> Optional[float]:
        """Get the shortest distance between two specific vertices."""
        if source in self.all_pairs_distances:
            return self.all_pairs_distances[source].get(destination)
        return None

    def has_negative_cycle(self) -> bool:
        """Check if the original graph contains a negative cycle."""
        return self.all_pairs_distances is None

    def get_potentials(self) -> Dict[Any, float]:
        """Get the computed potentials for all vertices."""
        return self.potentials.copy()

    def get_reweighted_graph(self) -> Optional[Graph]:
        """Get the reweighted graph with non-negative edge weights."""
        return self.reweighted_graph

    def print_all_pairs_distances(
        self, distances: Optional[Dict[Any, Dict[Any, float]]] = None
    ) -> None:
        """Print the all-pairs shortest path distances in a readable format."""
        if distances is None:
            distances = self.all_pairs_distances

        if distances is None:
            print("No solution due to negative cycle!")
            return

        print("\n" + "=" * 60)
        print("ALL-PAIRS SHORTEST PATH DISTANCES (Johnson's Algorithm)")
        print("=" * 60)

        # Print header
        vertices_list = sorted(list(self.original_graph.get_vertices()), key=str)
        print(f"{'From\\To':<8}", end="")
        for vertex in vertices_list:
            print(f"{str(vertex):<8}", end="")
        print()
        print("-" * (8 + len(vertices_list) * 8))

        # Print distances
        for source in vertices_list:
            print(f"{str(source):<8}", end="")
            for destination in vertices_list:
                if source in distances and destination in distances[source]:
                    dist = distances[source][destination]
                    if dist == float("inf"):
                        print(f"{'∞':<8}", end="")
                    else:
                        print(f"{dist:<8}", end="")
                else:
                    print(f"{'N/A':<8}", end="")
            print()

    @staticmethod
    def is_suitable_for_johnson(graph: Graph) -> tuple:
        """Check if Johnson's algorithm is suitable for the given graph."""
        if graph.is_empty():
            return False, "Graph is empty"

        # Check for negative cycles using a simple Bellman-Ford test
        temp_graph = graph.copy()
        extra_vertex = "temp_extra"
        for vertex in graph.get_vertices():
            temp_graph.add_edge(extra_vertex, vertex, 0)

        bellman_ford = BellmanFord(temp_graph)
        result = bellman_ford.find_shortest_paths(extra_vertex)

        if result is None:
            return False, "Graph contains negative cycles"

        # Johnson's is particularly good for sparse graphs
        vertex_count = graph.get_vertex_count()
        edge_count = graph.get_edge_count()

        if edge_count < vertex_count * vertex_count / 4:
            return True, "Suitable: Sparse graph with no negative cycles"
        else:
            return True, "Suitable but consider Floyd-Warshall for dense graphs"
