#!/usr/bin/python

""" Author: OMKAR PATHAK """
from __future__ import annotations

from queue import Queue


class Graph:
    def __init__(self) -> None:
        self.vertices: dict[int, list[int]] = {}

    def print_graph(self) -> None:
        """
        prints adjacency list representation of graaph
        >>> g = Graph()
        >>> g.print_graph()
        >>> g.add_edge(0, 1)
        >>> g.print_graph()
        0  :  1
        """
        for i in self.vertices:
            print(i, " : ", " -> ".join([str(j) for j in self.vertices[i]]))

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        adding the edge between two vertices
        >>> g = Graph()
        >>> g.print_graph()
        >>> g.add_edge(0, 1)
        >>> g.print_graph()
        0  :  1
        """
        if from_vertex in self.vertices:
            self.vertices[from_vertex].append(to_vertex)
        else:
            self.vertices[from_vertex] = [to_vertex]

    def bfs(self, start_vertex: int) -> set[int]:
        """
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 3)
        >>> sorted(g.bfs(2))
        [0, 1, 2, 3]
        """
        # initialize set for storing already visited vertices
        visited = set()

        # create a first in first out queue to store all the vertices for BFS
        queue: Queue = Queue()

        # mark the source node as visited and enqueue it
        visited.add(start_vertex)
        queue.put(start_vertex)

        while not queue.empty():
            vertex = queue.get()

            # loop through all adjacent vertex and enqueue it if not yet visited
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in visited:
                    queue.put(adjacent_vertex)
                    visited.add(adjacent_vertex)
        return visited


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.print_graph()
    # 0  :  1 -> 2
    # 1  :  2
    # 2  :  0 -> 3
    # 3  :  3

    assert sorted(g.bfs(2)) == [0, 1, 2, 3]

    """
https://en.wikipedia.org/wiki/Breadth-first_search
pseudo-code:
breadth_first_search(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
let Q = queue data structure, initialized with s
while Q is non-empty:
    remove the first node of Q, call it v
    for each edge(v, w):  // for w in graph[v]
        if w unexplored:
            mark w as explored
            add w to Q (at the end)
"""
#from __future__ import annotations

from collections import deque
from queue import Queue
from timeit import timeit

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def breadth_first_search(graph: dict, start: str) -> list[str]:
    """
    Implementation of breadth first search using queue.Queue.

    >>> ''.join(breadth_first_search(G, 'A'))
    'ABCDEF'
    """
    explored = {start}
    result = [start]
    queue: Queue = Queue()
    queue.put(start)
    while not queue.empty():
        v = queue.get()
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                result.append(w)
                queue.put(w)
    return result


def breadth_first_search_with_deque(graph: dict, start: str) -> list[str]:
    """
    Implementation of breadth first search using collection.queue.

    >>> ''.join(breadth_first_search_with_deque(G, 'A'))
    'ABCDEF'
    """
    visited = {start}
    result = [start]
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for child in graph[v]:
            if child not in visited:
                visited.add(child)
                result.append(child)
                queue.append(child)
    return result


def benchmark_function(name: str) -> None:
    setup = f"from __main__ import G, {name}"
    number = 10000
    res = timeit(f"{name}(G, 'A')", setup=setup, number=number)
    print(f"{name:<35} finished {number} runs in {res:.5f} seconds")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    benchmark_function("breadth_first_search")
    benchmark_function("breadth_first_search_with_deque")
    # breadth_first_search                finished 10000 runs in 0.20999 seconds
    # breadth_first_search_with_deque     finished 10000 runs in 0.01421 seconds
