#!/usr/bin/python

""" Author: OMKAR PATHAK """


class Graph:
    def __init__(self):
        self.vertices = {}

    def printGraph(self):
        """prints adjacency list representation of graaph"""
        for i in self.vertices.keys():
            print(i, " : ", " -> ".join([str(j) for j in self.vertices[i]]))

    def addEdge(self, fromVertex, toVertex):
        """adding the edge between two vertices"""
        if fromVertex in self.vertices.keys():
            self.vertices[fromVertex].append(toVertex)
        else:
            self.vertices[fromVertex] = [toVertex]

    def BFS(self, startVertex):
        # initialize set for storing already visited vertices
        visited = set()

        # create a first in first out queue to store all the vertices for BFS
        queue = []

        # mark the source node as visited and enqueue it
        visited.add(startVertex)
        queue.append(startVertex)

        while queue:
            vertex = queue.pop(0)

            # loop through all adjacent vertex and enqueue it if not yet visited
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in visited:
                    queue.append(adjacent_vertex)
                    visited.add(adjacent_vertex)
        return visited


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()
    # 0  :  1 -> 2
    # 1  :  2
    # 2  :  0 -> 3
    # 3  :  3

    assert sorted(g.BFS(2)) == [0, 1, 2, 3]
