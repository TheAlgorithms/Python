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
        if self.graph.get(u):
            if self.graph[u].count([w, v]) == 0:
                self.graph[u].append([w, v])
        else:
            self.graph[u] = [[w, v]]
        if not self.graph.get(v):
            self.graph[v] = []

    def all_nodes(self):
        return list(self.graph)

    # handles if the input does not exist
    def remove_pair(self, u, v):
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)

    # if no destination is meant the default value is -1
    def dfs(self, s=-2, d=-1):
        if s == d:
            return []
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        ss = s

        while True:
            # check if there is any non isolated nodes
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

            # check if all the children are visited
            if s == ss:
                stack.pop()
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
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
    def add_pair(self, u, v, w=1) -> None:
        """
        Adds an edge between u and v with an optional weight w to an undirected graph

        >>> g = Graph()
        >>> g.add_pair(1,2)
        >>> g.graph[1]
        [[1, 2]]
        >>> g.graph[2]
        [[1, 1]]
        >>> g.add_pair(1,2) # testing for duplicates
        >>> g.graph[1]
        [[1, 2]]
        >>> g.add_pair(2,1) # reverse order, should not add a duplicate
        >>> g.graph[2]
        [[1, 1]]
        >>> g.add_pair(1,3,5)
        >>> g.graph[1]
        [[1, 2], [5, 3]]
        >>> g.graph[3]
        [[5, 1]]
        >>> g.add_pair(4,4) # test for self loop
        >>> g.graph[4]
        [[1, 4]]
        >>> g.add_pair(1,2,3) # previously added nodes, different weight
        >>> g.graph[1]
        [[1, 2], [5, 3], [3, 2]]
        """
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
    def remove_pair(self, u, v) -> None:
        """
        Removes the edge between u and v in an undirected graph, if it exists

        >>> g = Graph()
        >>> g.add_pair(1,2)
        >>> g.add_pair(1,3,5)
        >>> g.graph[1]
        [[1, 2], [5, 3]]
        >>> g.remove_pair(1, 2)
        >>> g.graph[1]
        [[5, 3]]
        >>> g.graph[2]
        []
        >>> g.remove_pair(1,4) # node 4 does not exist
        >>> g.remove_pair(10, 11) # neither exists
        >>> g.add_pair(5,5)
        >>> g.graph[5]
        [[1, 5]]
        >>> g.remove_pair(5,5)
        >>> g.graph[5]
        []
        >>> g.add_pair(6,7,2)
        >>> g.add_pair(6,7,3)
        >>> g.graph[6]
        [[2, 7], [3, 7]]
        >>> g.remove_pair(6,7)
        >>> g.graph[6]
        [[3, 7]]
        """
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
    def dfs(self, s=-2, d=-1) -> list[int]:
        """
        Performs a depth-first search starting from node s.
        If destination d is given, stops when d is found

        >>> g = Graph()
        >>> g.add_pair(1,2)
        >>> g.add_pair(2,3)
        >>> g.dfs(1)
        [1, 2, 3]
        >>> g.dfs(1,3)
        [1, 2, 3]
        >>> g.dfs(1,4)  # 4 not in graph
        [1, 2, 3]
        >>> g.dfs(1,1)  # start equals dest
        []
        >>> g2 = Graph()
        >>> g2.add_pair(10,20)
        >>> g2.add_pair(20,30)
        >>> g2.dfs()  # default start
        [10, 20, 30]
        >>> g2.add_pair(30,40)
        >>> g2.add_pair(40, 50)
        >>> g2.dfs(d=40)  # checking if destination works properly
        [10, 20, 30, 40]
        """
        if s == d:
            return []
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        ss = s

        while True:
            # check if there is any non isolated nodes
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

            # check if all the children are visited
            if s == ss:
                stack.pop()
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
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

    def bfs(self, s=-2) -> list[int]:
        """
        Performs breadth-first search starting from node s.
        If s is not given, starts from the first node in the graph

        Returns:
            list of nodes found after performing breadth-first search

        >>> g = Graph()
        >>> g.add_pair(1,2)
        >>> g.add_pair(1,3)
        >>> g.add_pair(2,4)
        >>> g.add_pair(3,5)
        >>> g.bfs(1)
        [1, 2, 3, 4, 5]
        >>> g.bfs(2)
        [2, 1, 4, 3, 5]
        >>> g.bfs(4)  # leaf node test
        [4, 2, 1, 3, 5]
        >>> g.bfs(10)  # nonexistent node
        Traceback (most recent call last):
            ...
        KeyError: 10
        >>> g2 = Graph()
        >>> g2.add_pair(10,20)
        >>> g2.add_pair(20,30)
        >>> g2.bfs()
        [10, 20, 30]
        """
        d: deque = deque()
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

    def has_cycle(self) -> bool:
        """
        Detects whether the undirected graph contains a cycle.

        Note:
        - This function assumes the graph is connected and only traverses from the
          first node found in the graph.
        - It does not detect cycles that exist in disconnected components.
        - It also does not detect self-loops
        (e.g., an edge from a node to itself like 1-1).

        Returns:
            bool: True if a cycle is detected in the connected component starting
            from the first node; False otherwise.

        >>> g = Graph()
        >>> g.add_pair(1, 2)
        >>> g.add_pair(2, 3)
        >>> g.has_cycle()
        False
        >>> g2 = Graph()
        >>> g2.add_pair(1, 2)
        >>> g2.add_pair(2, 3)
        >>> g2.add_pair(3, 1)  # creates a cycle
        >>> g2.has_cycle()
        True
        >>> g3 = Graph()
        >>> g3.add_pair(1, 1)  # self-loop
        >>> g3.has_cycle()  # Self-loops are not detected by this method
        False
        >>> g4 = Graph()
        >>> g4.add_pair(1, 2)
        >>> g4.add_pair(3, 4)
        >>> g4.add_pair(4, 5)
        >>> g4.add_pair(5, 3)  # cycle in disconnected component
        >>> g4.has_cycle()  # Only checks the component reachable from the first node 1
        False
        """

        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents: list[int] = []
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
