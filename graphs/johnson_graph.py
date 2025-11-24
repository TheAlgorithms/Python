import heapq
import sys


# First implementation of johnson algorithm
# Steps followed to implement this algorithm is given in the below link:
# https://brilliant.org/wiki/johnsons-algorithm/
class JohnsonGraph:
    def __init__(self) -> None:
        """
        Initializes an empty graph with no edges.
        >>> g = JohnsonGraph()
        >>> g.edges
        []
        >>> g.graph
        {}
        """
        self.edges: list[tuple[str, str, int]] = []
        self.graph: dict[str, list[tuple[str, int]]] = {}

    # add vertices for a graph
    def add_vertices(self, vertex: str) -> None:
        """
        Adds a vertex `vertex` to the graph with an empty adjacency list.
        >>> g = JohnsonGraph()
        >>> g.add_vertices("A")
        >>> g.graph
        {'A': []}
        """
        self.graph[vertex] = []

    # assign weights for each edges formed of the directed graph
    def add_edge(self, vertex_a: str, vertex_b: str, weight: int) -> None:
        """
        Adds a directed edge from vertex `vertex_a`
        to vertex `vertex_b` with weight `weight`.
        >>> g = JohnsonGraph()
        >>> g.add_vertices("A")
        >>> g.add_vertices("B")
        >>> g.add_edge("A", "B", 5)
        >>> g.edges
        [('A', 'B', 5)]
        >>> g.graph
        {'A': [('B', 5)], 'B': []}
        """
        self.edges.append((vertex_a, vertex_b, weight))
        self.graph[vertex_a].append((vertex_b, weight))

    # perform a dijkstra algorithm on a directed graph
    def dijkstra(self, start: str) -> dict:
        """
        Computes the shortest path from vertex `start`
        to all other vertices using Dijkstra's algorithm.
        >>> g = JohnsonGraph()
        >>> g.add_vertices("A")
        >>> g.add_vertices("B")
        >>> g.add_edge("A", "B", 1)
        >>> g.dijkstra("A")
        {'A': 0, 'B': 1}
        >>> g.add_vertices("C")
        >>> g.add_edge("B", "C", 2)
        >>> g.dijkstra("A")
        {'A': 0, 'B': 1, 'C': 3}
        """
        distances = {vertex: sys.maxsize - 1 for vertex in self.graph}
        pq = [(0, start)]
        distances[start] = 0
        while pq:
            weight, vertex = heapq.heappop(pq)

            if weight > distances[vertex]:
                continue

            for node, node_weight in self.graph[vertex]:
                if distances[vertex] + node_weight < distances[node]:
                    distances[node] = distances[vertex] + node_weight
                    heapq.heappush(pq, (distances[node], node))
        return distances

    # carry out the bellman ford algorithm for a node and estimate its distance vector
    def bellman_ford(self, start: str) -> dict:
        """
        Computes the shortest path from vertex `start` to
        all other vertices using the Bellman-Ford algorithm.
        >>> g = JohnsonGraph()
        >>> g.add_vertices("A")
        >>> g.add_vertices("B")
        >>> g.add_edge("A", "B", 1)
        >>> g.bellman_ford("A")
        {'A': 0, 'B': 1}
        >>> g.add_vertices("C")
        >>> g.add_edge("B", "C", 2)
        >>> g.bellman_ford("A")
        {'A': 0, 'B': 1, 'C': 3}
        """
        distances = {vertex: sys.maxsize - 1 for vertex in self.graph}
        distances[start] = 0

        for vertex_a in self.graph:
            for vertex_a, vertex_b, weight in self.edges:
                if (
                    distances[vertex_a] != sys.maxsize - 1
                    and distances[vertex_a] + weight < distances[vertex_b]
                ):
                    distances[vertex_b] = distances[vertex_a] + weight

        return distances

    # perform the johnson algorithm to handle the negative weights that
    # could not be handled by either the dijkstra
    # or the bellman ford algorithm efficiently
    def johnson_algo(self) -> list[dict]:
        """
        Computes the shortest paths between
        all pairs of vertices using Johnson's algorithm
        for a directed graph.
        >>> g = JohnsonGraph()
        >>> g.add_vertices("A")
        >>> g.add_vertices("B")
        >>> g.add_edge("A", "B", 1)
        >>> g.add_edge("B", "A", 2)
        >>> optimal_paths = g.johnson_algo()
        >>> optimal_paths
        [{'A': 0, 'B': 1}, {'A': 2, 'B': 0}]
        """
        self.add_vertices("#")
        for vertex in self.graph:
            if vertex != "#":
                self.add_edge("#", vertex, 0)

        hash_path = self.bellman_ford("#")

        for i in range(len(self.edges)):
            vertex_a, vertex_b, weight = self.edges[i]
            self.edges[i] = (
                vertex_a,
                vertex_b,
                weight + hash_path[vertex_a] - hash_path[vertex_b],
            )
            self.edges[i] = (
                vertex_a,
                vertex_b,
                weight + hash_path[vertex_a] - hash_path[vertex_b],
            )

        self.graph.pop("#")
        filtered_edges = []
        for vertex1, vertex2, node_weight in self.edges:
            filtered_edges.append((vertex1, vertex2, node_weight))
        self.edges = filtered_edges

        for vertex in self.graph:
            self.graph[vertex] = []
            for vertex1, vertex2, node_weight in self.edges:
                if vertex1 == vertex:
                    self.graph[vertex].append((vertex2, node_weight))

        distances = []
        for vertex1 in self.graph:
            new_dist = self.dijkstra(vertex1)
            for vertex2 in self.graph:
                if new_dist[vertex2] < sys.maxsize - 1:
                    new_dist[vertex2] += hash_path[vertex2] - hash_path[vertex1]
            for key in new_dist:
                if new_dist[key] == sys.maxsize - 1:
                    new_dist[key] = None
            distances.append(new_dist)
        return distances


g = JohnsonGraph()
# this a complete connected graph
g.add_vertices("A")
g.add_vertices("B")
g.add_vertices("C")
g.add_vertices("D")
g.add_vertices("E")

g.add_edge("A", "B", 1)
g.add_edge("A", "C", 3)
g.add_edge("B", "D", 4)
g.add_edge("D", "E", 2)
g.add_edge("E", "C", -2)


optimal_paths = g.johnson_algo()
print("Print all optimal paths of a graph using Johnson Algorithm")
for i, row in enumerate(optimal_paths):
    print(f"{i}: {row}")
