"""
Dinic's algorithm for the maximum-flow problem.

Dinic's algorithm repeatedly builds a *level graph* with a breadth-first search
(shortest augmenting paths, measured in edges) and then, in one pass, saturates
a *blocking flow* on that level graph using depth-first search.  Grouping the
augmenting paths by length this way gives a much better worst case than the
plain Ford-Fulkerson / Edmonds-Karp augmenting-path method:

* Dinic's algorithm:            O(V^2 * E)
* on unit-capacity networks:    O(E * sqrt(V))

Unlike the adjacency-matrix implementations in ``ford_fulkerson.py`` and
``minimum_cut.py`` in this directory, this version stores the graph as an
adjacency list of residual edges, so it also handles graphs with parallel edges
and is efficient on sparse graphs.

Reference: https://en.wikipedia.org/wiki/Dinic%27s_algorithm
"""

from collections import deque


class Dinic:
    """
    Maximum flow in a directed graph with non-negative integer capacities.

    Add edges with :meth:`add_edge`, then call :meth:`max_flow`.

    >>> g = Dinic(6)
    >>> capacities = {
    ...     (0, 1): 16, (0, 2): 13, (1, 2): 10, (1, 3): 12,
    ...     (2, 1): 4, (2, 4): 14, (3, 2): 9, (3, 5): 20,
    ...     (4, 3): 7, (4, 5): 4,
    ... }
    >>> for (u, v), cap in capacities.items():
    ...     g.add_edge(u, v, cap)
    >>> g.max_flow(0, 5)
    23

    A source with no outgoing edges (or a sink with no incoming edges) has zero
    maximum flow:

    >>> Dinic(3).max_flow(0, 2)
    0

    Parallel edges between the same pair of vertices are supported and their
    capacities add up:

    >>> h = Dinic(2)
    >>> h.add_edge(0, 1, 3)
    >>> h.add_edge(0, 1, 5)
    >>> h.max_flow(0, 1)
    8
    """

    def __init__(self, vertices: int) -> None:
        if vertices <= 0:
            raise ValueError("number of vertices must be positive")
        self.size = vertices
        # graph[vertex] holds indices into self.edges for edges leaving that vertex.
        self.graph: list[list[int]] = [[] for _ in range(vertices)]
        # Each edge is stored as [destination, residual_capacity].
        # Edge i and its reverse edge i ^ 1 are always created together.
        self.edges: list[list[int]] = []

    def add_edge(self, source: int, destination: int, capacity: int) -> None:
        """
        Add a directed edge ``source -> destination`` with the given capacity.

        >>> g = Dinic(2)
        >>> g.add_edge(0, 1, 5)
        >>> g.add_edge(0, 1, -1)
        Traceback (most recent call last):
            ...
        ValueError: capacity must be non-negative
        >>> g.add_edge(0, 2, 5)
        Traceback (most recent call last):
            ...
        ValueError: vertex out of range
        """
        if capacity < 0:
            raise ValueError("capacity must be non-negative")
        if not (0 <= source < self.size and 0 <= destination < self.size):
            raise ValueError("vertex out of range")
        self.graph[source].append(len(self.edges))
        self.edges.append([destination, capacity])
        self.graph[destination].append(len(self.edges))
        self.edges.append([source, 0])  # reverse edge starts saturated

    def _build_level_graph(self, source: int) -> list[int]:
        """Breadth-first search; return per-vertex levels (-1 if unreachable)."""
        level = [-1] * self.size
        level[source] = 0
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for edge_index in self.graph[vertex]:
                destination, residual = self.edges[edge_index]
                if residual > 0 and level[destination] == -1:
                    level[destination] = level[vertex] + 1
                    queue.append(destination)
        return level

    def _send_flow(
        self,
        vertex: int,
        pushed: int,
        sink: int,
        level: list[int],
        progress: list[int],
    ) -> int:
        """Depth-first search that pushes a blocking flow along the level graph."""
        if vertex == sink:
            return pushed
        while progress[vertex] < len(self.graph[vertex]):
            edge_index = self.graph[vertex][progress[vertex]]
            destination, residual = self.edges[edge_index]
            if residual > 0 and level[destination] == level[vertex] + 1:
                flow = self._send_flow(
                    destination, min(pushed, residual), sink, level, progress
                )
                if flow > 0:
                    self.edges[edge_index][1] -= flow
                    self.edges[edge_index ^ 1][1] += flow
                    return flow
            progress[vertex] += 1
        return 0

    def max_flow(self, source: int, sink: int) -> int:
        """
        Return the maximum flow from ``source`` to ``sink``.

        >>> g = Dinic(4)
        >>> for (u, v), cap in {(0, 1): 3, (0, 2): 2, (1, 2): 5,
        ...                     (1, 3): 2, (2, 3): 3}.items():
        ...     g.add_edge(u, v, cap)
        >>> g.max_flow(0, 3)
        5
        >>> g.max_flow(0, 0)
        Traceback (most recent call last):
            ...
        ValueError: source and sink must be different
        """
        if not (0 <= source < self.size and 0 <= sink < self.size):
            raise ValueError("vertex out of range")
        if source == sink:
            raise ValueError("source and sink must be different")
        infinity = sum(capacity for _, capacity in self.edges) + 1
        flow = 0
        level = self._build_level_graph(source)
        while level[sink] != -1:
            progress = [0] * self.size
            while True:
                pushed = self._send_flow(source, infinity, sink, level, progress)
                if pushed == 0:
                    break
                flow += pushed
            level = self._build_level_graph(source)
        return flow


if __name__ == "__main__":
    from doctest import testmod

    testmod()
