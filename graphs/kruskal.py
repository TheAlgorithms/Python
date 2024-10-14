# Class to represent a graph
class Graph:
    def __init__(self, vertices: int) -> None:
        """
        Initialize the graph with the given number of vertices.

        Parameters:
        vertices (int): The number of vertices in the graph.

        Returns:
        None
        """
        self.vertices = vertices
        self.graph = []  # List to store graph edges (u, v, w)

    # Function to add an edge to the graph (u -> v with weight w)
    def add_edge(self, from_vertex: int, to_vertex: int, weight: float) -> None:
        """
        Add an edge to the graph.

        Parameters:
        from_vertex (int): The starting vertex of the edge.
        to_vertex (int): The ending vertex of the edge.
        weight (float): The weight of the edge.

        Returns:
        None

        Doctest:
        >>> g = Graph(3)
        >>> g.add_edge(0, 1, 5.0)
        >>> g.add_edge(1, 2, 3.5)
        >>> g.graph
        [(0, 1, 5.0), (1, 2, 3.5)]
        """
        self.graph.append((from_vertex, to_vertex, weight))

    # Utility function to find set of an element index (uses path compression)
    def find(self, parent: list, vertex_index: int) -> int:
        """
        Find the set of an element (vertex) using path compression.

        Parameters:
        parent (list): The list representing the parent of each vertex.
        vertex_index (int): The index of the vertex whose set is to be found.

        Returns:
        int: The representative (root) of the set containing the vertex.

        Doctest:
        >>> parent = [-1, 0, 0, 1]
        >>> g = Graph(4)
        >>> g.find(parent, 3)
        0
        >>> g.find(parent, 1)
        0
        """
        if parent[vertex_index] == -1:
            return vertex_index
        # Path compression
        parent[vertex_index] = self.find(parent, parent[vertex_index])
        return parent[vertex_index]

    # Function that does union of two sets of x and y (uses union by rank)
    def union(self, parent: list, rank: list, set_a: int, set_b: int) -> None:
        """
        Union of two sets of set_a and set_b (uses union by rank).

        Parameters:
        parent (list): The list representing the parent of each vertex.
        rank (list): The list representing the rank of each vertex.
        set_a (int): The representative of the first set.
        set_b (int): The representative of the second set.

        Returns:
        None

        Doctest:
        >>> parent = [0, 0, -1, -1]
        >>> rank = [1, 0, 0, 0]
        >>> g = Graph(4)
        >>> g.union(parent, rank, 0, 1)
        >>> parent
        [0, 0, -1, -1]
        >>> g.union(parent, rank, 2, 3)
        >>> parent
        [0, 0, 2, 2]
        """
        root_a = self.find(parent, set_a)
        root_b = self.find(parent, set_b)

        if root_a != root_b:
            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

    # Main function to construct MST using Kruskal's algorithm
    def kruskal_mst(self) -> list:
        """
        Construct Minimum Spanning Tree (MST) using Kruskal's algorithm.

        Returns:
        list: A list of edges included in the MST.

        Doctest:
        >>> g = Graph(4)
        >>> g.add_edge(0, 1, 10)
        >>> g.add_edge(0, 2, 6)
        >>> g.add_edge(0, 3, 5)
        >>> g.add_edge(1, 3, 15)
        >>> g.add_edge(2, 3, 4)
        >>> mst_edges = g.kruskal_mst()
        >>> mst_edges
        [(0, 3, 5), (2, 3, 4), (0, 1, 10)]
        """
        # Sort the edges based on their weights
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [-1] * self.vertices
        rank = [0] * self.vertices
        mst_edges = []

        for edge in self.graph:
            u, v, w = edge
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            # If including this edge does not cause a cycle
            if root_u != root_v:
                mst_edges.append((u, v, w))
                self.union(parent, rank, root_u, root_v)

        return mst_edges


# Example usage
if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))  # Ask user for the number of vertices
    E = int(input("Enter the number of edges: "))     # Ask user for the number of edges

    g = Graph(V)  # Create a graph with V vertices

    # Ask user to input the edges in the format u v w
    print("Enter each edge in the format: vertex1 vertex2 weight")
    for _ in range(E):
        u, v, w = map(int, input().split())  # Take input for edge (u, v) with weight w
        g.add_edge(u, v, w)

    # Print the constructed MST
    mst_result = g.kruskal_mst()
    print("Minimum Spanning Tree (MST) edges:")
    for edge in mst_result:
        print(edge)
