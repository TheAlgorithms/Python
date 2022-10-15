#From a given vertex in a weighted connected graph,to find shortest paths to other vertices using 
#Dijkstra’s algorithm.

def dij(n,v,cost,dist):
 flag=[0 for x in range(1,n+2,1)]
 for i in range(1,n+1,1):
 flag[i]=0
 dist[i]=cost[v][i]
count=2
 while count<=n:
 mini=99
 for w in range(1,n+1,1):
 if (dist[w] < mini and not(flag[w])):
 mini=dist[w]
 u=w
 flag[u]=1
 count=count+1
 for w in range(1,n+1,1):
 if ((dist[u]+cost[u][w]<dist[w]) and not(flag[w])):
 dist[w]=dist[u]+cost[u][w]
n=int(input("Enter number of nodes:"))
cost=[[0 for j in range(1,n+2,1)] for i in range(1,n+2,1)]
print("Enter the adjacency matrix:")
for i in range(1,n+1,1):
 for j in range(1,n+1,1):
 temp=int(input())
 cost[i][j]=temp
 if cost[i][j]==0:
 cost[i][j]=999
v=int(input("Enter the source node:"))
dist=[0 for i in range(1,n+2,1)]
dij(n,v,cost,dist)
print("***********Shortest path*********")
for i in range(1,n+1,1):
 if(i!=v):
 print(v,"->",i,"cost=",dist[i])
