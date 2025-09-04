"""
Bellman-Ford Algorithm implementation for single-source shortest path.

The Bellman-Ford algorithm can handle negative edge weights and detect negative cycles.
It has O(VE) time complexity where V is the number of vertices and E is the number of edges.

Author: Zakariae Fakhri
Date: August 2025
"""

from typing import Dict, Any, Optional, List, Tuple
from collections import defaultdict


class Graph:
    """
    A lightweight graph class for algorithms that don't have access to the main Graph class.
    """

    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.vertices = set()

    def add_edge(self, source: Any, destination: Any, weight: float) -> None:
        self.adjacency_list[source].append((destination, weight))
        self.vertices.add(source)
        self.vertices.add(destination)

    def get_neighbors(self, vertex: Any) -> List[Tuple[Any, float]]:
        return self.adjacency_list.get(vertex, [])

    def get_vertices(self) -> set:
        return self.vertices.copy()

    def has_vertex(self, vertex: Any) -> bool:
        return vertex in self.vertices

    def get_vertex_count(self) -> int:
        return len(self.vertices)


class BellmanFord:
    """
    Bellman-Ford algorithm implementation for single-source shortest path.

    This algorithm can handle graphs with negative edge weights and can detect
    negative cycles. It's particularly useful as a preprocessing step in
    Johnson's algorithm.
    """

    def __init__(self, graph):
        """
        Initialize the Bellman-Ford algorithm with a graph.

        Args:
            graph: The weighted directed graph to process
        """
        self.graph = graph
        self.distances = {}
        self.predecessors = {}

    def find_shortest_paths(self, start_vertex: Any) -> Optional[Dict[Any, float]]:
        """
        Find shortest paths from start_vertex to all other vertices.

        Args:
            start_vertex: The source vertex to start from

        Returns:
            Dictionary of vertex -> shortest distance, or None if negative cycle exists
        """
        if not self.graph.has_vertex(start_vertex):
            raise ValueError(f"Start vertex {start_vertex} not found in graph")

        # Initialize distances
        self.distances = {vertex: float("inf") for vertex in self.graph.get_vertices()}
        self.distances[start_vertex] = 0
        self.predecessors = {vertex: None for vertex in self.graph.get_vertices()}

        # Relax edges V-1 times
        vertex_count = self.graph.get_vertex_count()

        for iteration in range(vertex_count - 1):
            updated = False

            for vertex in self.graph.get_vertices():
                if self.distances[vertex] != float("inf"):
                    for neighbor, weight in self.graph.get_neighbors(vertex):
                        new_distance = self.distances[vertex] + weight

                        if new_distance < self.distances[neighbor]:
                            self.distances[neighbor] = new_distance
                            self.predecessors[neighbor] = vertex
                            updated = True

            # Early termination if no updates in this iteration
            if not updated:
                break

        # Check for negative cycles
        if self._has_negative_cycle():
            return None

        return self.distances.copy()

    def _has_negative_cycle(self) -> bool:
        """
        Check if the graph contains a negative cycle.

        Returns:
            True if negative cycle exists, False otherwise
        """
        for vertex in self.graph.get_vertices():
            if self.distances[vertex] != float("inf"):
                for neighbor, weight in self.graph.get_neighbors(vertex):
                    if self.distances[vertex] + weight < self.distances[neighbor]:
                        return True
        return False

    def get_path(self, start_vertex: Any, end_vertex: Any) -> Optional[List[Any]]:
        """
        Get the shortest path from start_vertex to end_vertex.

        Args:
            start_vertex: Source vertex
            end_vertex: Destination vertex

        Returns:
            List of vertices representing the path, or None if no path exists
        """
        if not self.distances or end_vertex not in self.distances:
            return None

        if self.distances[end_vertex] == float("inf"):
            return None

        path = []
        current = end_vertex

        while current is not None:
            path.append(current)
            current = self.predecessors.get(current)

        path.reverse()

        # Verify the path starts with start_vertex
        if path[0] != start_vertex:
            return None

        return path

    def get_distance(self, vertex: Any) -> float:
        """
        Get the shortest distance to a specific vertex.

        Args:
            vertex: The target vertex

        Returns:
            Shortest distance to the vertex
        """
        return self.distances.get(vertex, float("inf"))

    @staticmethod
    def detect_negative_cycle(graph) -> bool:
        """
        Static method to detect if a graph contains a negative cycle.

        Args:
            graph: The graph to check

        Returns:
            True if negative cycle exists, False otherwise
        """
        vertices = graph.get_vertices()
        if not vertices:
            return False

        # Pick any vertex as start
        start_vertex = next(iter(vertices))
        bf = BellmanFord(graph)
        result = bf.find_shortest_paths(start_vertex)

        return result is None
