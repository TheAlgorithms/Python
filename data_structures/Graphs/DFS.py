# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def adjacency(self):
        print(self.graph)

    # DFS algorithm
    def dfs(self, start, visited=None):
        print("GRAPH", self.graph)
        if visited is None:
            visited = set()
        visited.add(start)

        print(str(start) + " ", end="")

        for next in set(self.graph[start]) - (visited):
            self.dfs(next, visited)
        return visited

    # The time complexity of the DFS algorithm is represented in the form of O(V + E), where V is the number of nodes and E is the number of edges.

    # The space complexity of the algorithm is O(V).


# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.adjacency()
print("Following is DFS from (starting from vertex 2)")
g.dfs(2)
