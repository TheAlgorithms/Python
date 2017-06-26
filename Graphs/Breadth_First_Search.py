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
    def bfs(self,v):

        visited = [False]*self.vertex
        visited[v - 1] = True
        print('%d visited' % (v))

        queue = [v - 1]
        while len(queue) > 0:
            v = queue[0]
            for u in range(self.vertex):
                if self.graph[v][u] == 1:
                    if visited[u]== False:
                        visited[u] = True
                        queue.append(u)
                        print('%d visited' % (u +1))
            queue.pop(0)

g = Graph(10)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(3,6)
g.add_edge(3,7)
g.add_edge(4,8)
g.add_edge(5,9)
g.add_edge(6,10)
g.bfs(1)
