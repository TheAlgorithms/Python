from collections import deque
from dataclasses import dataclass
from typing import Iterator, List

"""
Finding the shortest path in 0-1-graph in O(E + V) which is faster than dijkstra.
0-1-graph is the weighted graph with the weights equal to 0 or 1.
Link: https://codeforces.com/blog/entry/22276
"""


@dataclass
class Edge:
    """Weighted directed graph edge."""

    destination_vertex: int
    weight: int


class AdjacencyList:
    """Graph adjacency list."""

    def __init__(self, size: int):
        self._graph: List[List[Edge]] = [[] for _ in range(size)]
        self._size = size

    def __getitem__(self, vertex: int) -> Iterator[Edge]:
        """Get all the vertices adjacent to the given one."""
        return iter(self._graph[vertex])

    @property
    def size(self):
        return self._size

    def add_edge(self, from_vertex: int, to_vertex: int, weight: int):
        """
        >>> g = AdjacencyList(2)
        >>> g.add_edge(0, 1, 0)
        >>> g.add_edge(1, 0, 1)
        >>> list(g[0])
        [Edge(destination_vertex=1, weight=0)]
        >>> list(g[1])
        [Edge(destination_vertex=0, weight=1)]
        >>> g.add_edge(0, 1, 2)
        Traceback (most recent call last):
            ...
        ValueError: Edge weight must be either 0 or 1.
        >>> g.add_edge(0, 2, 1)
        Traceback (most recent call last):
            ...
        ValueError: Vertex indexes must be in [0; size).
        """
        if weight not in (0, 1):
            raise ValueError("Edge weight must be either 0 or 1.")

        if to_vertex < 0 or to_vertex >= self.size:
            raise ValueError("Vertex indexes must be in [0; size).")

        self._graph[from_vertex].append(Edge(to_vertex, weight))

    def get_shortest_path(self, start_vertex: int, finish_vertex: int) -> int:
        """
        Return the shortest distance from start_vertex to finish_vertex in 0-1-graph.
              1                  1         1
         0--------->3        6--------7>------->8
         |          ^        ^        ^         |1
         |          |        |        |0        v
        0|          |0      1|        9-------->10
         |          |        |        ^    1
         v          |        |        |0
         1--------->2<-------4------->5
              0         1        1
        >>> g = AdjacencyList(11)
        >>> g.add_edge(0, 1, 0)
        >>> g.add_edge(0, 3, 1)
        >>> g.add_edge(1, 2, 0)
        >>> g.add_edge(2, 3, 0)
        >>> g.add_edge(4, 2, 1)
        >>> g.add_edge(4, 5, 1)
        >>> g.add_edge(4, 6, 1)
        >>> g.add_edge(5, 9, 0)
        >>> g.add_edge(6, 7, 1)
        >>> g.add_edge(7, 8, 1)
        >>> g.add_edge(8, 10, 1)
        >>> g.add_edge(9, 7, 0)
        >>> g.add_edge(9, 10, 1)
        >>> g.add_edge(1, 2, 2)
        Traceback (most recent call last):
            ...
        ValueError: Edge weight must be either 0 or 1.
        >>> g.get_shortest_path(0, 3)
        0
        >>> g.get_shortest_path(0, 4)
        Traceback (most recent call last):
            ...
        ValueError: No path from start_vertex to finish_vertex.
        >>> g.get_shortest_path(4, 10)
        2
        >>> g.get_shortest_path(4, 8)
        2
        >>> g.get_shortest_path(0, 1)
        0
        >>> g.get_shortest_path(1, 0)
        Traceback (most recent call last):
            ...
        ValueError: No path from start_vertex to finish_vertex.
        """
        queue = deque([start_vertex])
        distances = [None for i in range(self.size)]
        distances[start_vertex] = 0

        while queue:
            current_vertex = queue.popleft()
            current_distance = distances[current_vertex]

            for edge in self[current_vertex]:
                new_distance = current_distance + edge.weight
                if (
                    distances[edge.destination_vertex] is not None
                    and new_distance >= distances[edge.destination_vertex]
                ):
                    continue
                distances[edge.destination_vertex] = new_distance
                if edge.weight == 0:
                    queue.appendleft(edge.destination_vertex)
                else:
                    queue.append(edge.destination_vertex)

        if distances[finish_vertex] is None:
            raise ValueError("No path from start_vertex to finish_vertex.")

        return distances[finish_vertex]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
