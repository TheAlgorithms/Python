import heapq
import sys

#First implementation of johnson algorithm
#Steps followed to implement this algorithm is given in the below link:
#https://brilliant.org/wiki/johnsons-algorithm/
class JohnsonGraph:
    def __init__(self):
        self.edges = []
        self.graph = {}

    # add vertices for a graph
    def add_vertices(self, u):
        self.graph[u] = []

    # assign weights for each edges formed of the directed graph
    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
        self.graph[u].append((v, w))

    # perform a dijkstra algorithm on a directed graph
    def dijkstra(self, s):
        distances = {vertex: sys.maxsize-1 for vertex in self.graph}
        pq = [(0,s)]
        
        distances[s] = 0
        while pq:
            weight, v = heapq.heappop(pq)

            if weight > distances[v]:
                continue

            for node, w in self.graph[v]:
                if distances[v] + w < distances[node]:
                    distances[node] = distances[v] + w
                    heapq.heappush(pq, (distances[node], node))
        return distances

    #carry out the bellman ford algorithm for a node and estimate its distance vector
    def bellman_ford(self, s): 
        distances = {vertex: sys.maxsize-1 for vertex in self.graph}
        distances[s] = 0

        for u in self.graph:
            for u, v, w in self.edges:
                if distances[u] != sys.maxsize - 1 and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        return distances
 
    #perform the johnson algorithm to handle the negative weights that 
    # could not be handled by either the dijkstra
    #or the bellman ford algorithm efficiently
    def johnson_algo(self):
        self.add_vertices("#")
        for v in self.graph:
            if v != "#":
                self.add_edge("#", v, 0)

        n = self.bellman_ford("#")

        for i in range(len(self.edges)):
            u, v, weight = self.edges[i]
            self.edges[i] = (u, v, weight + n[u] - n[v])

        self.graph.pop("#")
        self.edges = [(u, v, w) for u, v, w in self.edges if u != "#"]

        for u in self.graph:
            self.graph[u] = [(v, weight) for x, v, weight in self.edges if x == u]

        distances = []
        for u in self.graph:
            new_dist = self.dijkstra(u)
            for v in self.graph:
                if new_dist[v] < sys.maxsize - 1:
                    new_dist[v] += n[v] - n[u]
            distances.append(new_dist)
        return distances


g = JohnsonGraph()
# this a complete connected graph
g.add_vertices("A")
g.add_vertices("B")
g.add_vertices("C")
g.add_vertices("D")
g.add_vertices("E")

g.add_edge("A", "B", 1)
g.add_edge("A", "C", 3)
g.add_edge("B", "D", 4)
g.add_edge("D", "E", 2)
g.add_edge("E", "C", -2)


optimal_paths = g.johnson_algo()
print("Print all optimal paths of a graph using Johnson Algorithm")
for i, row in enumerate(optimal_paths):
    print(f"{i}: {row}")
