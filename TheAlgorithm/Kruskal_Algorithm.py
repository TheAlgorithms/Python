graph folder structure:
graph/
__init__.py
graph.py
kruskal.py

graph.py:
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

kruskal.py:
from .graph import Graph

class Kruskal:
    def __init__(self, graph):
        self.graph = graph

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []
        i, e = 0, 0
        self.graph.graph = sorted(self.graph.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.graph.V):
            parent.append(node)
            rank.append(0)

        while e < self.graph.V - 1:
            u, v, w = self.graph.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)

Usage:
from graph import Graph
from graph.kruskal import Kruskal

if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    k = Kruskal(g)
    k.KruskalMST()
