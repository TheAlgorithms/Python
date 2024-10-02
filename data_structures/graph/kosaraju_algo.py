from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Default dictionary to store the graph
    
    def add_edge(self, u, v):
        """Function to add an edge from vertex u to vertex v."""
        self.graph[u].append(v)
    
    def _dfs(self, v, visited, stack=None):
        """
        A recursive function to perform DFS from vertex v.
        If stack is provided, it pushes the vertices in the order of their finish time.
        """
        visited[v] = True
        # Recur for all vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        
        # Push the vertex to stack if it's not None (used in first DFS pass)
        if stack is not None:
            stack.append(v)
    
    def _transpose(self):
        """
        Function to transpose (reverse) the graph.
        Returns the transposed graph.
        """
        transposed = Graph(self.V)
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transposed.add_edge(neighbor, vertex)
        return transposed
    
    def kosaraju_scc(self):
        """
        Function to find and print all Strongly Connected Components (SCCs) using Kosaraju's Algorithm.
        Returns a list of SCCs, where each SCC is a list of vertices.
        """
        # Step 1: Perform DFS to get the finishing times of vertices
        stack = []
        visited = [False] * self.V
        
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)
        
        # Step 2: Transpose the graph
        transposed_graph = self._transpose()
        
        # Step 3: Process vertices in the order defined by the stack
        visited = [False] * self.V
        sccs = []  # List to store SCCs
        
        while stack:
            v = stack.pop()
            if not visited[v]:
                # Collect all vertices in the current SCC
                scc_stack = []
                transposed_graph._dfs(v, visited, scc_stack)
                sccs.append(scc_stack)
        
        return sccs

# Example usage
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    
    print("Strongly Connected Components:")
    sccs = g.kosaraju_scc()
    for i, scc in enumerate(sccs, 1):
        print(f"SCC {i}: {scc}")
