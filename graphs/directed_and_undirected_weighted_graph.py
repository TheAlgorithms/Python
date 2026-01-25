from collections import deque
from math import floor
from random import random
from time import time

# the default weight is 1 if not assigned but all the implementation is weighted


class DirectedGraph:
    def __init__(self):
        self.graph = {}

    # adding vertices and edges
    # adding the weight is optional
    # handles repetition
    def add_pair(self, u, v, w=1):
        """
        Adds a directed edge u->v with weight w.
        >>> dg = DirectedGraph()
        >>> dg.add_pair(-1,2)
        >>> dg.add_pair(1,3,5)
        >>> dg.add_pair(1,3,5)
        >>> dg.add_pair(1,3,6)
        >>> dg.all_nodes()
        [-1, 2, 1, 3]
        >>> dg.graph[1]
        [[5, 3], [6, 3]]
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
        Returns list of all nodes in the graph.
        >>> dg = DirectedGraph()
        >>> dg.all_nodes()
        []
        >>> dg.add_pair(1,1)
        >>> dg.all_nodes()
        [1]
        >>> dg.add_pair(2,3,3)
        >>> dg.all_nodes()
        [1, 2, 3]
        """
        return list(self.graph)

    # handles if the input does not exist
    def remove_pair(self, u, v):
        """
        Removes all edges u->v if it exists.
        >>> dg = DirectedGraph()
        >>> dg.remove_pair(1,2) # silently exits
        >>> dg.add_pair(0,5,2)
        >>> dg.graph[0]
        [[2, 5]]
        >>> dg.remove_pair(5,0)
        >>> dg.graph[0]
        [[2, 5]]
        >>> dg.remove_pair(0,5)
        >>> dg.graph[0]
        []
        """
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)

    # if no destination is meant the default value is -1
    def dfs(self, s=-2, d=-1):
        """
        Performs depth first search from s to find d.
        Returns the path s->d as a list.
        Returns dfs from s if d is not found
        >>> dg = DirectedGraph()
        >>> dg.dfs()
        []
        >>> dg.add_pair(1,1)
        >>> dg.dfs(1,1)
        [1]
        >>> dg = DirectedGraph()
        >>> dg.add_pair(0,1)
        >>> dg.add_pair(0,2)
        >>> dg.add_pair(1,3)
        >>> dg.add_pair(1,4)
        >>> dg.add_pair(1,5)
        >>> dg.add_pair(2,5)
        >>> dg.add_pair(5,6)
        >>> dg.dfs(0,6)
        [0, 2, 5, 6]
        >>> dg.dfs(1,6)
        [1, 5, 6]
        >>> dg.dfs()
        [0, 2, 5, 6, 1, 4, 3]
        >>> dg.dfs(1,0)
        [1, 5, 6, 4, 3]
        """
        stack = []
        visited = []
        if s == -2:
            if self.graph.get(s, None):
                pass  # -2 is a node
            elif len(self.graph) > 0:
                s = next(iter(self.graph))
            else:
                return []  # Graph empty
        stack.append(s)

        # Run dfs
        while len(stack) > 0:
            s = stack.pop()
            visited.append(s)
            # If reached d, return
            if s == d:
                break

            # add not visited child nodes to stack
            for _, ss in self.graph[s]:
                if visited.count(ss) < 1:
                    stack.append(ss)
        return visited

    # c is the count of nodes you want and if you leave it or pass -1 to the function
    # the count will be random from 10 to 10000
    def fill_graph_randomly(self, c=-1):
        if c == -1:
            c = floor(random() * 10000) + 10
        for i in range(c):
            # every vertex has max 100 edges
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                if n != i:
                    self.add_pair(i, n, 1)

    def bfs(self, s=-2):
        """
        Performs breadth first search from s
        Returns list.
        >>> dg = DirectedGraph()
        >>> dg.bfs()
        []
        >>> dg.add_pair(1,1)
        >>> dg.bfs(1)
        [1]
        >>> dg = DirectedGraph()
        >>> dg.add_pair(0,1)
        >>> dg.add_pair(0,2)
        >>> dg.add_pair(1,3)
        >>> dg.add_pair(1,4)
        >>> dg.add_pair(1,5)
        >>> dg.add_pair(2,5)
        >>> dg.add_pair(5,6)
        >>> dg.bfs(0)
        [0, 1, 2, 3, 4, 5, 6]
        >>> dg.bfs(1)
        [1, 3, 4, 5, 6]
        >>> dg.bfs()
        [0, 1, 2, 3, 4, 5, 6]
        """
        d = deque()
        visited = []
        if s == -2:
            if self.graph.get(s, None):
                pass  # -2 is a node
            elif len(self.graph) > 0:
                s = next(iter(self.graph))
            else:
                return []  # Graph empty
        d.append(s)
        visited.append(s)
        # Run bfs
        while d:
            s = d.popleft()
            if len(self.graph[s]) != 0:
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        d.append(node[1])
                        visited.append(node[1])
        return visited

    def in_degree(self, u):
        count = 0
        for x in self.graph:
            for y in self.graph[x]:
                if y[1] == u:
                    count += 1
        return count

    def out_degree(self, u):
        return len(self.graph[u])

    def topological_sort(self, s=-2):
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        ss = s
        sorted_nodes = []

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            # check if all the children are visited
            if s == ss:
                sorted_nodes.append(stack.pop())
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                return sorted_nodes

    def cycle_nodes(self):
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                        and not on_the_way_back
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

            # check if all the children are visited
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                return list(anticipating_nodes)

    def has_cycle(self):
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                        and not on_the_way_back
                    ):
                        len_stack_minus_one = len(stack) - 1
                        while len_stack_minus_one >= 0:
                            if stack[len_stack_minus_one] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            else:
                                return True
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            # check if all the children are visited
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                return False

    def dfs_time(self, s=-2, e=-1):
        begin = time()
        self.dfs(s, e)
        end = time()
        return end - begin

    def bfs_time(self, s=-2):
        begin = time()
        self.bfs(s)
        end = time()
        return end - begin


class Graph:
    def __init__(self):
        self.graph = {}

    # adding vertices and edges
    # adding the weight is optional
    # handles repetition
    def add_pair(self, u, v, w=1):
        # check if the u exists
        if self.graph.get(u):
            # if there already is a edge
            if self.graph[u].count([w, v]) == 0:
                self.graph[u].append([w, v])
        else:
            # if u does not exist
            self.graph[u] = [[w, v]]
        # add the other way
        if self.graph.get(v):
            # if there already is a edge
            if self.graph[v].count([w, u]) == 0:
                self.graph[v].append([w, u])
        else:
            # if u does not exist
            self.graph[v] = [[w, u]]

    # handles if the input does not exist
    def remove_pair(self, u, v):
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)
        # the other way round
        if self.graph.get(v):
            for _ in self.graph[v]:
                if _[1] == u:
                    self.graph[v].remove(_)

    # if no destination is meant the default value is -1
    def dfs(self, s=-2, d=-1):
        """
        Performs depth first search from s to find d.
        Returns the path s->d as a list.
        Returns dfs from s if d is not found
        >>> ug = Graph()
        >>> ug.dfs()
        []
        >>> ug.add_pair(1,1)
        >>> ug.dfs(1,1)
        [1]
        >>> ug = Graph()
        >>> ug.add_pair(0,1)
        >>> ug.add_pair(0,2)
        >>> ug.add_pair(1,3)
        >>> ug.add_pair(1,4)
        >>> ug.add_pair(1,5)
        >>> ug.add_pair(2,5)
        >>> ug.add_pair(5,6)
        >>> ug.dfs(0,6)
        [0, 2, 5, 6]
        >>> ug.dfs(1,6)
        [1, 5, 6]
        >>> ug.dfs()
        [0, 2, 5, 6, 1, 4, 3]
        >>> ug.dfs(1,0)
        [1, 5, 6, 2, 0]
        """
        stack = []
        visited = []
        if s == -2:
            if self.graph.get(s, None):
                pass  # -2 is a node
            elif len(self.graph) > 0:
                s = next(iter(self.graph))
            else:
                return []  # Graph empty
        stack.append(s)

        # Run dfs
        while len(stack) > 0:
            s = stack.pop()
            if visited.count(s) == 1:
                continue
            else:
                visited.append(s)
            # If reached d, return
            if s == d:
                break

            # add not visited child nodes to stack
            for _, ss in self.graph[s]:
                if visited.count(ss) < 1:
                    stack.append(ss)
        return visited

    # c is the count of nodes you want and if you leave it or pass -1 to the function
    # the count will be random from 10 to 10000
    def fill_graph_randomly(self, c=-1):
        if c == -1:
            c = floor(random() * 10000) + 10
        for i in range(c):
            # every vertex has max 100 edges
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                if n != i:
                    self.add_pair(i, n, 1)

    def bfs(self, s=-2):
        """
        Performs breadth first search from s
        Returns list.
        >>> ug = Graph()
        >>> ug.bfs()
        []
        >>> ug.add_pair(1,1)
        >>> ug.bfs(1)
        [1]
        >>> ug = Graph()
        >>> ug.add_pair(0,1)
        >>> ug.add_pair(0,2)
        >>> ug.add_pair(1,3)
        >>> ug.add_pair(1,4)
        >>> ug.add_pair(1,5)
        >>> ug.add_pair(2,5)
        >>> ug.add_pair(5,6)
        >>> ug.bfs(0)
        [0, 1, 2, 3, 4, 5, 6]
        >>> ug.bfs(1)
        [1, 0, 3, 4, 5, 2, 6]
        >>> ug.bfs()
        [0, 1, 2, 3, 4, 5, 6]
        """
        d = deque()
        visited = []
        if s == -2:
            if self.graph.get(s, None):
                pass  # -2 is a node
            elif len(self.graph) > 0:
                s = next(iter(self.graph))
            else:
                return []  # Graph empty
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

    def degree(self, u):
        return len(self.graph[u])

    def cycle_nodes(self):
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                        and not on_the_way_back
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

            # check if all the children are visited
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                return list(anticipating_nodes)

    def has_cycle(self):
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                        and not on_the_way_back
                    ):
                        len_stack_minus_one = len(stack) - 1
                        while len_stack_minus_one >= 0:
                            if stack[len_stack_minus_one] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            else:
                                return True
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            # check if all the children are visited
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                return False

    def all_nodes(self):
        return list(self.graph)

    def dfs_time(self, s=-2, e=-1):
        begin = time()
        self.dfs(s, e)
        end = time()
        return end - begin

    def bfs_time(self, s=-2):
        begin = time()
        self.bfs(s)
        end = time()
        return end - begin
