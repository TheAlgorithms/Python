#!/usr/bin/python

""" Author: OMKAR PATHAK """
from __future__ import annotations

from queue import Queue


class Graph:
    def __init__(self, directed: bool =True) -> None:
        """
        To define a non-directed graph, simply
        set the directed argument to false
        """
        _Type = None
        if directed is False:
            _Type = Type[dict[int, list[Optional[int]]]]
        else:
            _Type = Type[dict[int, list[int]]]

        self.vertices:_Type  = {}
        self._directed = directed

    def operation_for_nondirected(self, possibly_mono_connected_vertex: int) -> None:
        """

        :param possibly_mono_connected_vertex: alias of the `to_vertex` in add_edge
        :return: None
        makes nondirected graphs consistent with the original setup
        >>> g = Graph(directed=False)
        >>> g.add_edge(0, 1)
        >>> g.print_graph()
        0  :  1
        """
        if self._directed is False:
            if possibly_mono_connected_vertex not in self.vertices:
                self.vertices[possibly_mono_connected_vertex] = []

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
            if not self.vertices[i]:
                continue
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
        from_v = self.vertices[from_vertex] = self.vertices.get(from_vertex, [])
        from_v.append(to_vertex)
        # what to do if the graph itself is non-directed
        self.operation_for_nondirected(to_vertex)

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
