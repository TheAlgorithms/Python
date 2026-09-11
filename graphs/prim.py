"""Prim's Algorithm.

Determines the minimum spanning tree(MST) of a graph using the Prim's Algorithm.

Details: https://en.wikipedia.org/wiki/Prim%27s_algorithm
"""

import heapq as hq
import math
from collections.abc import Iterator


class Vertex:
    """Class Vertex."""

    def __init__(self, id_):
        """
        Arguments:
            id - input an id to identify the vertex
        Attributes:
            neighbors - a list of the vertices it is linked to
            edges     - a dict to store the edges's weight
        """
        self.id = str(id_)
        self.key = None
        self.pi = None
        self.neighbors = []
        self.edges = {}  # {vertex:distance}

    def __lt__(self, other):
        """Comparison rule to < operator."""
        return self.key < other.key

    def __repr__(self):
        """Return the vertex id."""
        return self.id

    def add_neighbor(self, vertex):
        """Add a pointer to a vertex at neighbor's list."""
        self.neighbors.append(vertex)

    def add_edge(self, vertex, weight):
        """Destination vertex and weight."""
        self.edges[vertex.id] = weight


def connect(graph, a, b, edge):
    # add the neighbors:
    graph[a - 1].add_neighbor(graph[b - 1])
    graph[b - 1].add_neighbor(graph[a - 1])
    # add the edges:
    graph[a - 1].add_edge(graph[b - 1], edge)
    graph[b - 1].add_edge(graph[a - 1], edge)


def prim(graph: list, root: Vertex) -> list:
    """Prim's Algorithm.

    Runtime:
        O(mn) with `m` edges and `n` vertices

    Return:
        List with the edges of a Minimum Spanning Tree

    Usage:
        prim(graph, graph[0])
    """
    a = []
    for u in graph:
        u.key = math.inf
        u.pi = None
    root.key = 0
    q = graph[:]
    while q:
        u = min(q)
        q.remove(u)
        for v in u.neighbors:
            if (v in q) and (u.edges[v.id] < v.key):
                v.pi = u
                v.key = u.edges[v.id]
    for i in range(1, len(graph)):
        a.append((int(graph[i].id) + 1, int(graph[i].pi.id) + 1))
    return a


def prim_heap(graph: list, root: Vertex) -> Iterator[tuple]:
    """Prim's Algorithm with min heap.

    Runtime:
        O((m + n)log n) with `m` edges and `n` vertices

    Yield:
        Edges of a Minimum Spanning Tree

    Usage:
        prim(graph, graph[0])
    """
    for u in graph:
        u.key = math.inf
        u.pi = None
    root.key = 0

    h = list(graph)
    hq.heapify(h)

    while h:
        u = hq.heappop(h)
        for v in u.neighbors:
            if (v in h) and (u.edges[v.id] < v.key):
                v.pi = u
                v.key = u.edges[v.id]
                hq.heapify(h)

    for i in range(1, len(graph)):
        yield (int(graph[i].id) + 1, int(graph[i].pi.id) + 1)


def test_vector() -> None:
    """
    # Creates a list to store x vertices.
    >>> x = 5
    >>> G = [Vertex(n) for n in range(x)]

    >>> connect(G, 1, 2, 15)
    >>> connect(G, 1, 3, 12)
    >>> connect(G, 2, 4, 13)
    >>> connect(G, 2, 5, 5)
    >>> connect(G, 3, 2, 6)
    >>> connect(G, 3, 4, 6)
    >>> connect(G, 0, 0, 0)  # Generate the minimum spanning tree:
    >>> G_heap = G[:]
    >>> MST = prim(G, G[0])
    >>> MST_heap = prim_heap(G, G[0])
    >>> for i in MST:
    ...     print(i)
    (2, 3)
    (3, 1)
    (4, 3)
    (5, 2)
    >>> for i in MST_heap:
    ...     print(i)
    (2, 3)
    (3, 1)
    (4, 3)
    (5, 2)
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
