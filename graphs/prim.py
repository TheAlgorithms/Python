"""
Prim's Algorithm.

Determines the minimum spanning tree(MST) of a graph using the Prim's Algorithm

Create a list to store x the vertices.
G = [vertex(n) for n in range(x)]

For each vertex in G, add the neighbors:
G[x].add_neighbor(G[y])
G[y].add_neighbor(G[x])

For each vertex in G, add the edges:
G[x].add_edge(G[y], w)
G[y].add_edge(G[x], w)

To solve, run:
MST = prim(G, G[0])
"""

import math


class Vertex:
    """Class Vertex."""

    def __init__(self, id):
        """
        Arguments:
            id - input an id to identify the vertex
        Attributes:
            neighbors - a list of the vertices it is linked to
            edges     - a dict to store the edges's weight
        """
        self.id = str(id)
        self.key = None
        self.pi = None
        self.neighbors = []
        self.edges = {}  # [vertex:distance]

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


def prim(graph, root):
    """
    Prim's Algorithm.
    Return a list with the edges of a Minimum Spanning Tree
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
        a.append([graph[i].id, graph[i].pi.id])
    return a
