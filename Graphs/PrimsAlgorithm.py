import sys, heapq
from collections import defaultdict

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
adjlist = defaultdict(list)
for x in range(e):
    l = [int(x) for x in input().split()]
    adjlist[l[0]].append([ l[1], l[2] ])
    adjlist[l[1]].append([ l[0], l[2] ])

# Prims Algorithm
visited = [0 for i in range(n)]

# Neighbour of explored vertex
Nbr_TV  = [-1 for i in range(n)]
# Minimum Distance of explored vertex with partial tree formed in graph
Dist_TV = [sys.maxsize for i in range(n)]
heapq.heapify(Dist_TV) 

TreeEdges = []
visited[0] = 1
for x in adjlist[0]:
    Nbr_TV[ x[0] ] = 0
    Dist_TV[ x[0] ] = x[1]
    
for i in range(1,n):

    u = heapq.heappop(Dist_TV)
    visited[u] = 1
    TreeEdges.append([u, Nbr_TV[u]])
    
    for x in adjlist[u]:
        if visited[x[0]] == False and Dist_TV[x[0]] > x[1]:
            Dist_TV[x[0]] = x[1]
            Nbr_TV[x[0]] = u
    
print(TreeEdges)

    
    
    
    