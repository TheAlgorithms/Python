#!/usr/bin/python

""" Author: OMKAR PATHAK """


class Graph:
    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertices
    def printGraph(self):
        print(self.vertex)
        for i in self.vertex.keys():
            print(i, " -> ", " -> ".join([str(j) for j in self.vertex[i]]))

    # for adding the edge between two vertices
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]

    def DFS(self):
        # visited array for storing already visited nodes
        visited = [False] * len(self.vertex)

        # call the recursive helper function
        for i in range(len(self.vertex)):
            if visited[i] is False:
                self.DFSRec(i, visited)

    def DFSRec(self, startVertex, visited):
        # mark start vertex as visited
        visited[startVertex] = True

        print(startVertex, end=" ")

        # Recur for all the vertices that are adjacent to this node
        for i in self.vertex.keys():
            if visited[i] is False:
                self.DFSRec(i, visited)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()
    print("DFS:")
    g.DFS()

    # OUTPUT:
    # 0  ->  1 -> 2
    # 1  ->  2
    # 2  ->  0 -> 3
    # 3  ->  3
    # DFS:
    #  0 1 2 3
