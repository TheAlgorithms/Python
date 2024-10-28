"""
Author  : Yashwanth Adimulam
Date    : 26th Oct 2024

Implement the class of Graphs with useful functions based on it.

Useful Links: https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-weighted-graph/
              https://www.tutorialspoint.com/applications-advantages-and-disadvantages-of-unweighted-graph
              https://www.baeldung.com/cs/weighted-vs-unweighted-graphs
              https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)
"""

from collections import deque
from math import floor
from random import random
from time import time


class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_pair(self, u, v, w=1):
        """
        Add a directed edge from u to v with weight w.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2, 3)
        >>> g.graph
        {1: [[3, 2]], 2: []}
        """
        if self.graph.get(u):
            if self.graph[u].count([w, v]) == 0:
                self.graph[u].append([w, v])
        else:
            self.graph[u] = [[w, v]]
        if not self.graph.get(v):
            self.graph[v] = []

    def all_nodes(self):
        """
        Return a list of all nodes in the graph.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.all_nodes()
        [1, 2]
        """
        return list(self.graph)

    def remove_pair(self, u, v):
        """
        Remove the directed edge from u to v.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.remove_pair(1, 2)
        >>> g.graph
        {1: [], 2: []}
        """
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)

    def dfs(self, s=-2, d=-1):
        """
        Perform depth-first search from node s to d.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.add_pair(2, 3)
        >>> g.dfs(1, 3)
        [1, 2, 3]
        >>> g.dfs(1, 2)
        [1, 2]
        """
        if s == d:
            return []
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        while True:
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        if node[1] == d:
                            visited.append(d)
                            return visited
                        else:
                            stack.append(node[1])
                            visited.append(node[1])
                            ss = node[1]
                            break

            if s == ss:
                stack.pop()
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss

            if len(stack) == 0:
                return visited

    def fill_graph_randomly(self, c=-1):
        """
        Fill the graph with random edges.

        >>> g = DirectedGraph()
        >>> g.fill_graph_randomly(5)
        >>> len(g.all_nodes()) > 0
        True
        """
        if c == -1:
            c = floor(random() * 10000) + 10
        for i in range(c):
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                if n != i:
                    self.add_pair(i, n, 1)

    def bfs(self, s=-2):
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
            s = d.popleft()
            if len(self.graph[s]) != 0:
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        d.append(node[1])
                        visited.append(node[1])
        return visited

    def in_degree(self, u):
        """
        Calculate in-degree of node u.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.in_degree(2)
        1
        """
        count = 0
        for x in self.graph:
            for y in self.graph[x]:
                if y[1] == u:
                    count += 1
        return count

    def out_degree(self, u):
        """
        Calculate out-degree of node u.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.out_degree(1)
        1
        """
        return len(self.graph[u])

    def topological_sort(self, s=-2):
        """
        Perform topological sort of the graph.
        """
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        sorted_nodes = []

        while True:
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            if s == ss:
                sorted_nodes.append(stack.pop())
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss

            if len(stack) == 0:
                return sorted_nodes

    def cycle_nodes(self):
        """
        Get nodes that are part of a cycle.
        """
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        anticipating_nodes = set()

        while True:
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                    ):
                        len_stack = len(stack) - 1
                        while len_stack >= 0:
                            if stack[len_stack] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            else:
                                anticipating_nodes.add(stack[len_stack])
                                len_stack -= 1
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            if s == ss:
                stack.pop()
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                parent = s
                s = ss

            if len(stack) == 0:
                return list(anticipating_nodes)

    def has_cycle(self):
        """
        Check if the graph has a cycle.
        """
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s

        while True:
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                    ):
                        return True
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            if s == ss:
                stack.pop()
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss

            if len(stack) == 0:
                return False

    def dfs_time(self, s=-2, e=-1):
        """
        Measure the time taken for DFS.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.dfs_time(1, 2) >= 0
        True
        """
        begin = time()
        self.dfs(s, e)
        end = time()
        return end - begin

    def bfs_time(self, s=-2):
        """
        Measure the time taken for BFS.

        >>> g = DirectedGraph()
        >>> g.add_pair(1, 2)
        >>> g.bfs_time(1) >= 0
        True
        """
        begin = time()
        self.bfs(s)
        end = time()
        return end - begin
