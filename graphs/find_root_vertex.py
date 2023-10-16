"""
A root vertex of a directed graph is a vertex u with a directed path from u to v for every pair of vertices (u, v) in the graph.
In other words, all other vertices in the graph can be reached from the root vertex.
https://medium.com
"""
# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        # Resize the list to hold `n` elements
        self.adj = [[] for _ in range(n)]

        # Add an edge from source to destination
        for edge in edges:
            self.adj[edge[0]].append(edge[1])

# Function to perform DFS traversal on the graph
def DFS(graph, v, discovered):
    discovered[v] = True  # Mark the current node as discovered

    # Do for every edge (v, u)
    for u in graph.adj[v]:
        if not discovered[u]:  # `u` is not discovered
            DFS(graph, u, discovered)

# Function to find the root vertex of a graph
def findRootVertex(graph, n):
    # To keep track of all previously discovered vertices in DFS
    discovered = [False] * n

    # Find the last starting vertex `v` in DFS
    v = 0
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)
            v = i

    # Reset the discovered vertices
    discovered[:] = [False] * n

    # Perform DFS on the graph from the last starting vertex `v`
    DFS(graph, v, discovered)

    # Return -1 if all vertices are not reachable from vertex `v`
    for i in range(n):
        if not discovered[i]:
            return -1

    # We reach here only if `v` is a root vertex
    return v

if __name__ == '__main':
    # List of graph edges as per the above diagram
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 3), (4, 5), (5, 0)]

    # Total number of nodes in the graph (0 to 5)
    n = 6

    # Build a directed graph from the given edges
    graph = Graph(edges, n)

    # Find the root vertex in the graph
    root = findRootVertex(graph, n)

    if root != -1:
        print('The root vertex is', root)
    else:
        print('The root vertex does not exist
