# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  # List to store graph edges (u, v, w)

    # Function to add an edge to the graph (u -> v with weight w)
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Utility function to find set of an element i (uses path compression)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Function that does union of two sets of x and y (uses union by rank)
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        # Attach smaller rank tree under the root of the high-rank tree
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Main function to construct MST using Kruskal's algorithm
    def kruskal_mst(self):
        # This will store the resultant Minimum Spanning Tree (MST)
        result = []

        # Step 1: Sort all edges in non-decreasing order of their weight
        # If we are using a greedy algorithm, we need to sort the edges first
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # Allocate memory for creating V subsets (for the disjoint-set)
        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges in MST is V-1, so we will stop once we have V-1 edges
        e = 0  # Initialize result edges count
        i = 0  # Initialize the index for sorted edges

        # Loop until MST has V-1 edges
        while e < self.V - 1:
            # Step 2: Pick the smallest edge 
            #increment the index for the next iteration
            u, v, w = self.graph[i]
            i = i + 1

            # Step 3: Find sets of both vertices u and v 
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If adding this edge doesn't cause a cycle, include it in the result
            if x != y:
                result.append([u, v, w])
                e = e + 1  # Increment the count of edges in the MST
                self.union(parent, rank, x, y)

            # Else, discard the edge (it would create a cycle)

        # Print the constructed Minimum Spanning Tree
        print("Following are the edges in the constructed MST:")
        for u, v, w in result:
            print(f"{u} -- {v} == {w}")


# Example usage
if __name__ == "__main__":
    V = int(
        input("Enter the number of vertices: ")
    )  # Ask user for the number of vertices
    E = int(input("Enter the number of edges: "))  # Ask user for the number of edges

    g = Graph(V)  # Create a graph with V vertices

    # Ask user to input the edges in the format u v w
    print("Enter each edge in the format: vertex1 vertex2 weight")
    for _ in range(E):
        u, v, w = map(int, input().split())  # Take input for edge (u, v) with weight w
        g.add_edge(u, v, w)

    # Print the constructed MST
    g.kruskal_mst()
