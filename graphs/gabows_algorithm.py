"""
This is a pure Python implementation of
Gabow's algorithm for finding
strongly connected components (SCCs)
in a directed graph.

For doctests run:
    python -m doctest -v gabow_algorithm.py
or
    python3 -m doctest -v gabow_algorithm.py
For manual testing run:
    python gabow_algorithm.py
"""

from collections import defaultdict
from typing import List, Dict


class Graph:
    """
    Graph data structure to represent
    a directed graph and find SCCs
    using Gabow's algorithm.

    Attributes:
        vertices (int): Number of
        vertices in the graph.
        graph (Dict[int, List[int]]):
        Adjacency list of the graph.

    Methods:
        add_edge(u, v): Adds an edge
        from vertex u to vertex v.
        find_sccs(): Finds and returns
        all SCCs in the graph.

    Examples:
    >>> g = Graph(5)
    >>> g.add_edge(0, 2)
    >>> g.add_edge(2, 1)
    >>> g.add_edge(1, 0)
    >>> g.add_edge(0, 3)
    >>> g.add_edge(3, 4)
    >>> sorted(g.find_sccs())
    [[0, 1, 2], [3], [4]]
    """

    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.graph: Dict[int, List[int]] = defaultdict(list)
        self.index = 0
        self.stack_s = []  # Stack S
        self.stack_p = []  # Stack P
        self.visited = [False] * vertices
        self.result = []

    def add_edge(self, u: int, v: int) -> None:
        """
        Adds a directed edge from vertex u to vertex v.

        :param u: Starting vertex of the edge.
        :param v: Ending vertex of the edge.
        """
        self.graph[u].append(v)

    def _dfs(self, v: int) -> None:
        """
        Depth-first search helper function to
        process each vertex and identify SCCs.
        :param v: The current vertex to process in DFS.
        """
        self.visited[v] = True
        self.stack_s.append(v)
        self.stack_p.append(v)

        for neighbor in self.graph[v]:
            if not self.visited[neighbor]:
                self._dfs(neighbor)
            elif neighbor in self.stack_p:
                while self.stack_p and self.stack_p[-1] != neighbor:
                    self.stack_p.pop()
        if self.stack_p and self.stack_p[-1] == v:
            scc = []
            while True:
                node = self.stack_s.pop()
                scc.append(node)
                if node == v:
                    break
            self.stack_p.pop()
            self.result.append(scc)

    def find_sccs(self) -> List[List[int]]:
        """
        Finds all strongly connected components
        in the directed graph.
        :return: List of SCCs, where each SCC
        is represented as a list of vertices.
        """
        for v in range(self.vertices):
            if not self.visited[v]:
                self._dfs(v)
        return self.result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # Example usage for manual testing
    try:
        vertex_count = int(input("Enter the number of vertices: "))
        g = Graph(vertex_count)
        edge_count = int(input("Enter the number of edges: "))
        print("Enter each edge as a pair of vertices (u v):")
        for _ in range(edge_count):
            u, v = map(int, input().split())
            g.add_edge(u, v)
        sccs = g.find_sccs()
        print("Strongly Connected Components:", sccs)
    except ValueError:
        print("Invalid input. Please enter valid integers.")
