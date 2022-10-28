"""
Python program for Dijkstra's single
source shortest path algorithm. The program is
for adjacency matrix representation of the graph

author : aakash_2001
"""
class Graph():

	def __init__(self, vertices:int) -> None:
	    """
	    Constructor function
	    param vertices : int
	    """
	    self.V = vertices
	    self.graph = [[0 for column in range(vertices)]
	    for row in range(vertices)]

	def print_solution(self, dist:int) -> None:
	    """
	    Function to print the Distance from Source
	    param dist : int
	    """
	    print("Vertex \t Distance from Source")
	    for node in range(self.V):
		    print(node, "\t\t", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def min_distance(self, dist:int, sptSet:bool) -> int:
	    """
	    Function to calculate min distance
	    param dist:int
	    param sptSet:bool
	    """

		# Initialize minimum distance for next node
	    min = 1e7

		# Search not nearest vertex not in the
		# shortest path tree
	    for v in range(self.V):
	        if dist[v] < min and sptSet[v] == False:
	            min = dist[v]
	            min_index = v

	    return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src:int ) -> None:
	    """
	    Actual working of dijkstra algo
	    param src : int
	    """

	    dist = [1e7] * self.V
	    dist[src] = 0
	    sptSet = [False] * self.V

	    for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
		    u = self.min_distance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shortest path tree
            sptSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
		    for v in range(self.V):
		        if (self.graph[u][v] > 0 and
		        sptSet[v] == False and
		        dist[v] > dist[u] + self.graph[u][v]):
		            dist[v] = dist[u] + self.graph[u][v]

	    self.print_solution(dist)

# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]

g.dijkstra(0)
