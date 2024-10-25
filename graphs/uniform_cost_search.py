#!/usr/bin/python

"""Author: MRINAL"""

from __future__ import annotations
from queue import PriorityQueue


class Graph:
    def __init__(self) -> None:
        # Graph represented as an adjacency list with edge weights
        self.vertices: dict[int, list[tuple[int, int]]] = {}

    def print_graph(self) -> None:
        """
        Prints adjacency list representation of the graph.
        >>> g = Graph()
        >>> g.add_edge(0, 1, 2)
        >>> g.add_edge(0, 2, 4)
        >>> g.print_graph()
        0  :  [(1, 2), (2, 4)]
        """
        for i in self.vertices:
            print(i, " : ", self.vertices[i])

    def add_edge(self, from_vertex: int, to_vertex: int, cost: int) -> None:
        """
        Adds an edge with a specified cost between two vertices.
        >>> g = Graph()
        >>> g.add_edge(0, 1, 2)
        >>> g.print_graph()
        0  :  [(1, 2)]
        """
        if from_vertex in self.vertices:
            self.vertices[from_vertex].append((to_vertex, cost))
        else:
            self.vertices[from_vertex] = [(to_vertex, cost)]

    def ucs(self, start_vertex: int, goal_vertex: int) -> tuple[int, list[int]]:
        """
        Uniform Cost Search to find the minimum cost path from start to goal.
        >>> g = Graph()
        >>> g.add_edge(0, 1, 2)
        >>> g.add_edge(0, 2, 4)
        >>> g.add_edge(1, 2, 1)
        >>> g.add_edge(1, 3, 7)
        >>> g.add_edge(2, 3, 3)
        >>> g.ucs(0, 3)
        (6, [0, 1, 2, 3])
        """
        # Priority queue to hold nodes to explore; initializes with (cost, start_vertex)
        pq = PriorityQueue()
        pq.put((0, start_vertex, [start_vertex]))

        # Dictionary to track the minimum cost to reach each vertex
        visited = {}

        while not pq.empty():
            cost, vertex, path = pq.get()

            # If the goal is reached, return the cost and path
            if vertex == goal_vertex:
                return cost, path

            # If the vertex is already visited with a lower cost, skip it
            if vertex in visited and visited[vertex] <= cost:
                continue

            # Mark the vertex with the cost for the first time or with a lower cost
            visited[vertex] = cost

            # Explore neighbors
            for neighbor, edge_cost in self.vertices.get(vertex, []):
                if neighbor not in visited or visited[neighbor] > cost + edge_cost:
                    pq.put((cost + edge_cost, neighbor, path + [neighbor]))

        return float('inf'), []  # If no path found


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

    g = Graph()
    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 7)
    g.add_edge(2, 3, 3)

    g.print_graph()
    # 0  :  [(1, 2), (2, 4)]
    # 1  :  [(2, 1), (3, 7)]
    # 2  :  [(3, 3)]

    result = g.ucs(0, 3)
    print("Minimum cost:", result[0])
    print("Path:", result[1])
    # Expected output:
    # Minimum cost: 6
    # Path: [0, 1, 2, 3]
