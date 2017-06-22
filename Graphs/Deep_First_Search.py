class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] * vertex for i in range(vertex) ]
        self.visited = [False] * vertex

    def add_edge(self, u, v):
        self.graph[u - 1][v - 1] = 1
        self.graph[v - 1][u - 1] = 1
    def show(self):

        for i in self.graph:
            for j in i:
                print(j, end=' ')
            print(' ')


    def dfs(self, u):
        self.visited[u - 1] = True
        print('%d visited' % u)
        for i in range(1, self.vertex + 1):
            if self.graph[u - 1][i - 1] == 1 and self.visited[i - 1] == False:
                self.dfs(i)


g = Graph(5)
g.add_edge(1,4)
g.add_edge(4,2)
g.add_edge(4,5)
g.add_edge(2,5)
g.add_edge(5,3)
g.dfs(1)
