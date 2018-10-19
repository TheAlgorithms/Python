from __future__ import print_function

def printDist(dist, V):
	print("\nVertex Distance")
	for i in range(V):
		if dist[i] != float('inf') :
			print(i,"\t",int(dist[i]),end = "\t")
		else:
			print(i,"\t","INF",end="\t")
		print()

def minDist(mdist, vset, V):
	minVal = float('inf')
	minInd = -1
	for i in range(V):
		if (not vset[i]) and mdist[i] < minVal :
			minInd = i
			minVal = mdist[i]
	return minInd

def Dijkstra(graph, V, src):
	mdist=[float('inf') for i in range(V)]
	vset = [False for i in range(V)]
	mdist[src] = 0.0;
	
	for i in range(V-1):
		u = minDist(mdist, vset, V)
		vset[u] = True
		
		for v in range(V):
			if (not vset[v]) and graph[u][v]!=float('inf') and mdist[u] + graph[u][v] < mdist[v]:
				mdist[v] = mdist[u] + graph[u][v] 

	

	printDist(mdist, V)	

			

#MAIN
V = int(raw_input("Enter number of vertices: "))
E = int(raw_input("Enter number of edges: "))

graph = [[float('inf') for i in range(V)] for j in range(V)]

for i in range(V):
	graph[i][i] = 0.0

for i in range(E):
	print("\nEdge ",i+1)
	src = int(raw_input("Enter source:"))
	dst = int(raw_input("Enter destination:"))
	weight = float(raw_input("Enter weight:"))
	graph[src][dst] = weight

gsrc = int(raw_input("\nEnter shortest path source:"))
Dijkstra(graph, V, gsrc)
