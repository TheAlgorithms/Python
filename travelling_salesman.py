
from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):


	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	
	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:

		
		current_pathweight = 0

		# compute current path weight
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		# update minimum
		min_path = min(min_path, current_pathweight)
		
	return min_path


# Driver Code
if __name__ == "__main__":

	# matrix representation of graph
	graph = [[0, 15, 15, 30], [20, 0, 40, 25],
			[10, 25, 0, 40], [30, 25, 20, 0]]
	s = 0
	print(travellingSalesmanProblem(graph, s))
