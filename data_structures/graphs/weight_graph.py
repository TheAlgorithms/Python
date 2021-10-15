"""
This is a representaton of a weighted graph using adjacency list.
"""

class Edge:                                 #A class to store graph edge.
    def __init__(self,src,dest,weight) -> None:
        self.src = src
        self.dest = dest
        self.weight = weight

class Node:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight


class Graph:
    def __init__(self,edges,N) -> None:
        self.adj=[[] for i in range(N)]                           #allocating space for adjacency list

        #add edges to the graph
        for e in edges:
            node=Node(e.dest,e.weight)
            self.adj[e.src].append(node)

    def printGraph(self) -> None:
        for src in range(len(self.adj)):
            print()
            for edge in self.adj[src]:
                print(f'({src} -> {edge.value}, {edge.weight})',end=" ")


def test_graph() -> None:
    """
    >>> test_graph()
    """
    edges=[Edge(0,1,6) , Edge(1,2,5) , Edge(2,0,3) , Edge(2,1,4) ,
    Edge(3,2,0) ,Edge(4,5,6) ,Edge(5,4,4)]

    N=6

    graph= Graph(edges, N)
    graph.printGraph()

if __name__ == "__main__":
    test_graph()