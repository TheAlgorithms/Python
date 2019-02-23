from __future__ import print_function

def printDist(dist, V):
	print("\nThe shortest path matrix using Floyd Warshall algorithm\n")
	for i in range(V):
		for j in range(V):
			if dist[i][j] != float('inf') :
				print(int(dist[i][j]),end = "\t")
			else:
				print("INF",end="\t")
		print()



def FloydWarshall(graph, V):
	dist=[[float('inf') for i in range(V)] for j in range(V)]
	
	for i in range(V):
		for j in range(V):
			dist[i][j] = graph[i][j]

	for k in range(V):
		for i in range(V):
			for j in range(V):
				if dist[i][k]!=float('inf') and dist[k][j]!=float('inf') and dist[i][k]+dist[k][j] < dist[i][j]:
					dist[i][j] = dist[i][k] + dist[k][j]

	printDist(dist, V)	

			

#MAIN
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

graph = [[float('inf') for i in range(V)] for j in range(V)]

for i in range(V):
	graph[i][i] = 0.0

for i in range(E):
	print("\nEdge ",i+1)
	src = int(input("Enter source:"))
	dst = int(input("Enter destination:"))
	weight = float(input("Enter weight:"))
	graph[src][dst] = weight

FloydWarshall(graph, V)
