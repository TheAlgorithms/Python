# Kruskal's Algorithm in Python

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # List to store the graph edges (u, v, w)

    # Add edges to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Utility function to find the subset of an element 'i'
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Utility function to do union of two subsets
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        # Attach smaller rank tree under root of higher rank tree
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # The main function to implement Kruskal's algorithm
    def kruskal_mst(self):
        result = []  # This will store the resultant MST
        i, e = 0, 0  # Variables for sorted edges and result array

        # Sort all the edges in ascending order based on their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges in MST will be V-1
        while e < self.V - 1:

            # Pick the smallest edge and increment the index for the next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't cause a cycle, include it in the result
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print the contents of the resultant MST
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")

# Driver code
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()
