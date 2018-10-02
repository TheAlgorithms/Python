"""
Prim's Algorithm.

Determines the minimum spanning tree(MST) of a graph using the Prim's Algorithm

Create a list to store x the vertices.
G = [vertex(n) for n in range(x)]

For each vertex in G, add the neighbors:
G[x].addNeighbor(G[y])
G[y].addNeighbor(G[x])

For each vertex in G, add the edges:
G[x].addEdge(G[y], w)
G[y].addEdge(G[x], w)

To solve run:
MST = prim(G, G[0])
"""

import math


class vertex():
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
        return (self.key < other.key)

    def __repr__(self):
        """Return the vertex id."""
        return self.id

    def addNeighbor(self, vertex):
        """Add a pointer to a vertex at neighbor's list."""
        self.neighbors.append(vertex)

    def addEdge(self, vertex, weight):
        """Destination vertex and weight."""
        self.edges[vertex.id] = weight


def prim(graph, root):
    """
    Prim's Algorithm.

    Return a list with the edges of a Minimum Spanning Tree

    prim(graph, graph[0])
    """
    A = []
    for u in graph:
        u.key = math.inf
        u.pi = None
    root.key = 0
    Q = graph[:]
    while Q:
        u = min(Q)
        Q.remove(u)
        for v in u.neighbors:
            if (v in Q) and (u.edges[v.id] < v.key):
                v.pi = u
                v.key = u.edges[v.id]
    for i in range(1, len(graph)):
        A.append([graph[i].id, graph[i].pi.id])
    return(A)
