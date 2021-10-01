import doctest
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

def dijkstra(src: int, dest: int) -> int:

	""" Return the minumum cost from src to dest using the given graph.
	
	>>> dijkstra(0,3)
	19
	>>> dijkstra(0,29)
	-1
	
	"""

	#Define a list, to store the graph in the form of (i,j, cost)
	graph = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
		    if matrix[i][j]!=0:
		        graph.append([i,j,matrix[i][j]])

	n = len(matrix)
	if src < 0 or dest <0 or src >=n or dest >=n :
		return -1
	dist = [100001]*n  #Set the MAX to a large number
	dist[src]=0
		
	for _ in range(n):
		curr = dist[::]
		for fro,to,cost in graph:
		    curr[to]= min(curr[to],dist[fro]+cost)
		dist = curr


	#print(curr[dest])
	return curr[dest]
	

if __name__=="__main__":
	import doctest
	doctest.testmod()

