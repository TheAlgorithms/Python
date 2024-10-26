"""
Author  : Your Name
Date    : Your Date

Implement the class of Graphs with useful functions based on it.
"""

from collections import deque
from math import floor
from random import random
from time import time

class DirectedGraph:
    def __init__(self) -> None:
        """
        Initialize a directed graph.

        >>> g = DirectedGraph()
        >>> g.all_nodes()
        []
        """
        self.graph = {}

    def add_pair(self, u: int, v: int, w: int = 1) -> None:
        """
        Add a directed edge from u to v with weight w.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2, 3)
        >>> g.graph
        {1: [[3, 2]], 2: []}
        """
        if self.graph.get(u):
            if not any(edge[1] == v and edge[0] == w for edge in self.graph[u]):
                self.graph[u].append([w, v])
        else:
            self.graph[u] = [[w, v]]
        if v not in self.graph:
            self.graph[v] = []

    def all_nodes(self) -> list:
        """
        Return a list of all nodes in the graph.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.all_nodes()
        [1, 2]
        """
        return list(self.graph)

    def remove_pair(self, u: int, v: int) -> None:
        """
        Remove the directed edge from u to v.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.remove_pair(1, 2)
        >>> g.graph
        {1: [], 2: []}
        """
        if self.graph.get(u):
            self.graph[u] = [edge for edge in self.graph[u] if edge[1] != v]

    def dfs(self, s: int = -2, d: int = -1) -> list:
        """
        Perform depth-first search from node s to d.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.add_pair(2, 3)
        >>> g.dfs(1, 3)
        [1, 2, 3]
        """
        if s == d:
            return []
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        while stack:
            current = stack[-1]
            if current == d:
                return visited
            if current in self.graph:
                for edge in self.graph[current]:
                    if edge[1] not in visited:
                        stack.append(edge[1])
                        visited.append(edge[1])
                        break
                else:
                    stack.pop()
            else:
                stack.pop()
        return visited

    def bfs(self, s: int = -2) -> list:
        """
        Perform breadth-first search starting from node s.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.add_pair(2, 3)
        >>> g.bfs(1)
        [1, 2, 3]
        """
        d = deque()
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        d.append(s)
        visited.append(s)
        while d:
            current = d.popleft()
            if current in self.graph:
                for edge in self.graph[current]:
                    if edge[1] not in visited:
                        d.append(edge[1])
                        visited.append(edge[1])
        return visited

    def has_cycle(self) -> bool:
        """
        Check if the graph has a cycle.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.add_pair(2, 1)
        >>> g.has_cycle()
        True
        """
        visited = set()
        rec_stack = set()

        def cycle_util(v):
            visited.add(v)
            rec_stack.add(v)
            for edge in self.graph.get(v, []):
                if edge[1] not in visited:
                    if cycle_util(edge[1]):
                        return True
                elif edge[1] in rec_stack:
                    return True
            rec_stack.remove(v)
            return False

        for node in self.graph:
            if node not in visited:
                if cycle_util(node):
                    return True
        return False

    # Additional methods would go here with doctests...

class Graph:
    def __init__(self) -> None:
        """
        Initialize an undirected graph.

        >>> g = Graph()
        >>> g.all_nodes()
        []
        """
        self.graph = {}

    def add_pair(self, u: int, v: int, w: int = 1) -> None:
        """
        Add an undirected edge between u and v with weight w.

        >>> g = Graph()
        >>> g.add_pair(1, 2, 3)
        >>> g.graph
        {1: [[3, 2]], 2: [[3, 1]]}
        """
        if self.graph.get(u):
            if not any(edge[1] == v and edge[0] == w for edge in self.graph[u]):
                self.graph[u].append([w, v])
        else:
            self.graph[u] = [[w, v]]
        if self.graph.get(v):
            if not any(edge[1] == u and edge[0] == w for edge in self.graph[v]):
                self.graph[v].append([w, u])
        else:
            self.graph[v] = [[w, u]]

    def all_nodes(self) -> list:
        """
        Return a list of all nodes in the graph.

        >>> g = Graph()
        >>> g.add_pair(1, 2)
        >>> g.all_nodes()
        [1, 2]
        """
        return list(self.graph)

    # Additional methods would go here with doctests...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
