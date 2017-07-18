class GRAPH:
    """docstring for GRAPH"""
    def __init__(self, nodes):
        self.nodes=nodes
        self.graph=[[0]*nodes for i in range (nodes)]
        self.visited=[0]*nodes


    def show(self):
        print self.graph

    def add_edge(self, i, j):
        self.graph[i][j]=1
        self.graph[j][i]=1

    def bfs(self,s):
        queue=[s]
        while len(queue)!=0:
            x=queue.pop(0)
            print(x)
            self.visited[x]=1
            for i in range(0,self.nodes):
                if self.graph[x][i]==1 and self.visited[i]==0:
                    queue.append(i)     
                    self.visited[i]=1

n=int(input("Enter the number of Nodes : "))
g=GRAPH(n)
e=int(input("Enter the no of edges : "))
print("Enter the edges (u v)")
for i in range(0,e):
    u,v=map(int, raw_input().split())
    g.add_edge(u,v)
s=int(input("Enter the source node :"))
g.bfs(s)
