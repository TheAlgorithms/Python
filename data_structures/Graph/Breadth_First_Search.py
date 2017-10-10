class GRAPH:
    """docstring for GRAPH"""
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[0]*nodes for i in range (nodes)]
        self.visited = [0]*nodes


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
                    if visited[u] is False:
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
g.bfs(4)

print(self.graph)

    def add_edge(self, i, j):
        self.graph[i][j]=1
        self.graph[j][i]=1

    def bfs(self, s):
        queue = [s]
        self.visited[s] = 1
        while len(queue)!= 0:
            x = queue.pop(0)
            print(x)
            for i in range(0, self.nodes):
                if self.graph[x][i] == 1 and self.visited[i] == 0:
                    queue.append(i)     
                    self.visited[i] = 1

n = int(input("Enter the number of Nodes : "))
g = GRAPH(n)
e = int(input("Enter the no of edges : "))
print("Enter the edges (u v)")

for i in range(0, e):
    u ,v = map(int, raw_input().split())
    g.add_edge(u, v)

s = int(input("Enter the source node :"))
g.bfs(s)
