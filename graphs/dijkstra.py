class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for row in range(vertices)]

    def printsolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def minimum_distance(self, distances, spt_set) -> int:

        minm = 1e7

        for v in range(self.V):
            if dist[v] < minm and sptSet[v] == False:
                minm = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [1e7] * self.V
        dist[src] = 0
        sptset = [False] * self.V

        for cout in range(self.V):

            u = self.mindistance(dist, sptset)
            sptset[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and sptset[v] == False
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printsolution(dist)


# Driver program
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

g.dijkstra(0)
