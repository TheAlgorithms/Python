"""
Dijkstra's Algorithm implementation for single-source shortest path.

Dijkstra's algorithm finds shortest paths from a source vertex to all other vertices
in a weighted graph with non-negative edge weights. It has O(V log V + E) time complexity
when using a binary heap.

Author: Zakaria Fakhri
Date: August 2025
"""

import heapq
from typing import Dict, Any, List, Optional, Set, Tuple
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
    
    def get_edge_weight(self, source: Any, destination: Any) -> Optional[float]:
        for neighbor, weight in self.adjacency_list.get(source, []):
            if neighbor == destination:
                return weight
        return None


class Dijkstra:
    """
    Dijkstra's algorithm implementation for single-source shortest path.
    
    This algorithm works on graphs with non-negative edge weights and provides
    optimal shortest paths. It's used as a component in Johnson's algorithm
    after edge reweighting.
    """
    
    def __init__(self, graph):
        """
        Initialize Dijkstra's algorithm with a graph.
        
        Args:
            graph: The weighted directed graph with non-negative weights
        """
        self.graph = graph
        self.distances = {}
        self.predecessors = {}
        self.visited = set()
    
    def find_shortest_paths(self, start_vertex: Any) -> Dict[Any, float]:
        """
        Find shortest paths from start_vertex to all other vertices.
        
        Args:
            start_vertex: The source vertex to start from
            
        Returns:
            Dictionary of vertex -> shortest distance
            
        Raises:
            ValueError: If start_vertex is not in the graph
        """
        if not self.graph.has_vertex(start_vertex):
            raise ValueError(f"Start vertex {start_vertex} not found in graph")
        
        # Initialize distances and data structures
        self.distances = {vertex: float('inf') for vertex in self.graph.get_vertices()}
        self.distances[start_vertex] = 0
        self.predecessors = {vertex: None for vertex in self.graph.get_vertices()}
        self.visited = set()
        
        # Priority queue: (distance, vertex)
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Skip if already visited (handles duplicate entries in heap)
            if current_vertex in self.visited:
                continue
            
            # Mark current vertex as visited
            self.visited.add(current_vertex)
            
            # Process all neighbors
            for neighbor, weight in self.graph.get_neighbors(current_vertex):
                if neighbor not in self.visited:
                    new_distance = current_distance + weight
                    
                    # Relaxation step
                    if new_distance < self.distances[neighbor]:
                        self.distances[neighbor] = new_distance
                        self.predecessors[neighbor] = current_vertex
                        heapq.heappush(priority_queue, (new_distance, neighbor))
        
        return self.distances.copy()
    
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
        
        if self.distances[end_vertex] == float('inf'):
            return None
        
        path = []
        current = end_vertex
        
        while current is not None:
            path.append(current)
            current = self.predecessors.get(current)
        
        path.reverse()
        
        # Verify the path starts with start_vertex
        if path and path[0] != start_vertex:
            return None
        
        return path if path else None
    
    def get_distance(self, vertex: Any) -> float:
        """
        Get the shortest distance to a specific vertex.
        
        Args:
            vertex: The target vertex
            
        Returns:
            Shortest distance to the vertex
        """
        return self.distances.get(vertex, float('inf'))
    
    def get_path_cost(self, path: List[Any]) -> float:
        """
        Calculate the total cost of a given path.
        
        Args:
            path: List of vertices representing a path
            
        Returns:
            Total cost of the path, or infinity if path is invalid
        """
        if not path or len(path) < 2:
            return 0.0
        
        total_cost = 0.0
        
        for i in range(len(path) - 1):
            current_vertex = path[i]
            next_vertex = path[i + 1]
            
            # Find the edge weight
            edge_weight = self.graph.get_edge_weight(current_vertex, next_vertex)
            if edge_weight is None:
                return float('inf')  # Invalid path
            
            total_cost += edge_weight
        
        return total_cost
    
    def is_reachable(self, start_vertex: Any, target_vertex: Any) -> bool:
        """
        Check if target_vertex is reachable from start_vertex.
        
        Args:
            start_vertex: Source vertex
            target_vertex: Target vertex
            
        Returns:
            True if target is reachable, False otherwise
        """
        if not self.distances:
            self.find_shortest_paths(start_vertex)
        
        return self.distances.get(target_vertex, float('inf')) != float('inf')
    
    @staticmethod
    def validate_non_negative_weights(graph) -> bool:
        """
        Validate that all edge weights in the graph are non-negative.
        
        Args:
            graph: The graph to validate
            
        Returns:
            True if all weights are non-negative, False otherwise
        """
        for vertex in graph.get_vertices():
            for neighbor, weight in graph.get_neighbors(vertex):
                if weight < 0:
                    return False
        return True
