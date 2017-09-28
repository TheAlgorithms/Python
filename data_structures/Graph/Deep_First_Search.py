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

    def dfs(self,s):
        self.visited[s]=1
        print(s)
        for i in range(0,self.nodes):
            if self.visited[i]==0 and self.graph[s][i]==1:
                self.dfs(i)
            

n=int(input("Enter the number of Nodes : "))
g=GRAPH(n)
e=int(input("Enter the no of edges : "))
print("Enter the edges (u v)")
for i in range(0,e):
    u,v=map(int, raw_input().split())
    g.add_edge(u,v)
s=int(input("Enter the source node :"))
g.dfs(s)
