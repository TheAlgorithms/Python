class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] * vertex for i in range(vertex) ]

    def add_edge(self, u, v):
        self.graph[u - 1][v - 1] = 1
        self.graph[v - 1][u - 1] = 1

    def show(self):

        for i in self.graph:
            for j in i:
                print(j, end=' ')
            print(' ')




g = Graph(100)

g.add_edge(1,4)
g.add_edge(4,2)
g.add_edge(4,5)
g.add_edge(2,5)
g.add_edge(5,3)
g.show()

