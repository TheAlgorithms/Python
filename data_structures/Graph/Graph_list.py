class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] for i in range(vertex)]

    def add_edge(self, u, v):
        self.graph[u - 1].append(v - 1)

    def show(self):
        for i in range(self.vertex):
            print('%d: '% (i + 1), end=' ')
            for j in self.graph[i]:
                print('%d-> '% (j + 1), end=' ')
            print(' ')



g = Graph(100)

g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,5)


g.show()

