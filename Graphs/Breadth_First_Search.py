class GRAPH:
    """docstring for GRAPH"""

    def __init__(self, nodes):
        self.nodes=nodes
        self.graph=[[0]*nodes for i in range (nodes)]
        self.visited=[0]*nodes
        self.vertex = nodes

    def bfs(self,v):

        visited = [False]*self.vertex
        visited[v] = True
        queue = [v]
        while len(queue) > 0:
            v = queue[0]
            print('%d,' %v,end='')
            queue.pop(0)
            for u in range(self.vertex):
                if self.graph[v][u] == 1:
                    if visited[u]== False:
                        visited[u] = True
                        queue.append(u)
                        
            

    def add_edge(self, i, j):
        self.graph[i][j]=1


n=int(input("Enter the number of Nodes : "))
g=GRAPH(n)
g.vertex = n
e=int(input("Enter the no of edges : "))
print("Enter the edges (u v)")
for i in range(0,e):
    u,v=map(int,input().split())
    g.add_edge(u,v)
s=int(input("Enter the source node : "))
print("BFS order:")
g.bfs(s)
print("")

