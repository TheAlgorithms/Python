from __future__ import annotations


class Graph:
    def __init__(self, vertices: int) -> None:
        """
        >>> graph = Graph(2)
        >>> graph.vertices
        2
        >>> len(graph.graph)
        2
        >>> len(graph.graph[0])
        2
        """
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def print_solution(self, distances_from_source: list[int]) -> None:
        """
        >>> graph = Graph(0)
        >>> graph.print_solution([])  # doctest: +NORMALIZE_WHITESPACE
        Vertex 	 Distance from Source
        """
        print("Vertex \t Distance from Source")
        for vertex in range(self.vertices):
            print(vertex, "\t\t", distances_from_source[vertex])

    def minimum_distance(
        self, distances_from_source: list[int], sptset: list[bool]
    ) -> int:
        """
        A utility function to find the vertex with minimum distance value, from the set
        of vertices not yet included in shortest path tree.

        >>> graph = Graph(3)
        >>> graph.minimum_distance([1, 2, 3], [False, False, True])
        0
        """

        # Initialize minimum distance for next node
        minimum = 1e7
        min_index = 0

        # Search not nearest vertex not in the shortest path tree
        for vertex in range(self.vertices):
            if distances_from_source[vertex] < minimum and sptset[vertex] is False:
                minimum = distances_from_source[vertex]
                min_index = vertex
        return min_index

    def dijkstra(self, source: int) -> None:
        """
        Function that implements Dijkstra's single source shortest path algorithm for a
        graph represented using adjacency matrix representation.

        >>> graph = Graph(4)
        >>> graph.dijkstra(1)  # doctest: +NORMALIZE_WHITESPACE
        Vertex  Distance from Source
        0 		 10000000.0
        1 		 0
        2 		 10000000.0
        3 		 10000000.0
        """

        distances = [1e7] * self.vertices  # distances from the source
        distances[source] = 0
        sptset = [False] * self.vertices

        for _ in range(self.vertices):
            u = self.minimum_distance(distances, sptset)
            sptset[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.vertices):
                if (
                    self.graph[u][v] > 0
                    and sptset[v] is False
                    and distances[v] > distances[u] + self.graph[u][v]
                ):
                    distances[v] = distances[u] + self.graph[u][v]

        self.print_solution(distances)


# Driver program
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

g.dijkstra(0)
