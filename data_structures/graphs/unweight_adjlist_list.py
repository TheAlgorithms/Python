"""
This is an implementation of unweighted graph in the form of adjacency list using lists in python.
"""
from typing import Any


class Edge:                                 #A class to store graph edge.
    def __init__(self,src,dest) -> None:
        self.src = src
        self.dest = dest

class Graph:
    def __init__(self,edges,N) -> None:
        self.adj = [[] for _ in range(N)] #allocating space for adjacency list

        #add edges to the graph
        for current in edges:
            self.adj[current.src].append(current.dest)

    def printGraph(self) -> None:
        for src in range(len(self.adj)):
            print(f'{src} -> ',end=" ")
            print(*self.adj[src],sep=" ")


def test_graph() -> None:
    """
    >>> test_graph()
    """
    edges=[Edge(0,1) , Edge(1,2) , Edge(2,0) , Edge(2,1) ,
    Edge(3,2) ,Edge(4,5) ,Edge(5,4)]

    N=6

    graph= Graph(edges, N)
    graph.printGraph()

if __name__ == "__main__":
    test_graph()