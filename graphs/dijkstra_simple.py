#Dijkstra's algorithm 

'''
	** NOTE **
	The vertices/ indices are zero based indexing
'''
# Define a matrix with cost from index i->j as matrix(i,j)
matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

#Define a list, to store the graph in the form of (i,j, cost)
graph = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]!=0:
            graph.append([i,j,matrix[i][j]])


def dijkstra(src, dest, graph):

	n = len(matrix)
	dist = [100001]*n  #Set the MAX to a large number
	dist[src]=0
		
	for _ in range(n):
		curr = dist[::]
		for fro,to,cost in graph:
		    curr[to]= min(curr[to],dist[fro]+cost)
		dist = curr


	#print(curr[dest])
	return curr[dest]
	

src = 0 
dest = 3

print(dijkstra(src,dest,graph))
