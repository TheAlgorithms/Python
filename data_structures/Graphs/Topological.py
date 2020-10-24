# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self, vertices):
        self.V = vertices
        self.verticeslist = []

        # default dictionary to store graph
        self.digraph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.digraph[u].append(v)
        self.verticeslist.append(u)
        self.verticeslist.append(v)

    def adjacency(self):
        print(self.digraph)

    def topological_sort(self):
        # self.digraph is a dictionary:
        #   key: a node
        # value: a set of adjacent neighboring nodes

        # construct a dictionary mapping nodes to their
        # indegrees
        # indegrees = {node: 0 for node in self.digraph.keys()}
        # print("IN", indegrees)
        self.verticeslist = set(self.verticeslist)
        indegrees = {}
        for k in self.verticeslist:
            indegrees[k] = 0
        # print("IN", indegrees)
        # print("GRAPH", self.digraph)
        for node in self.digraph.keys():
            for neighbor in self.digraph[node]:
                indegrees[neighbor] = indegrees[neighbor] + 1
                print(indegrees[neighbor])

        # track nodes with no incoming edges
        nodes_with_no_incoming_edges = []
        for node in self.digraph:
            if indegrees[node] == 0:
                nodes_with_no_incoming_edges.append(node)

        # initially, no nodes in our ordering
        topological_ordering = []

        # as long as there are nodes with no incoming edges
        # that can be added to the ordering
        while len(nodes_with_no_incoming_edges) > 0:

            # add one of those nodes to the ordering
            node = nodes_with_no_incoming_edges.pop()
            topological_ordering.append(node)

            # decrement the indegree of that node's neighbors
            for neighbor in self.digraph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    nodes_with_no_incoming_edges.append(neighbor)

        # we've run out of nodes with no incoming edges
        # did we add all the nodes or find a cycle?
        if len(topological_ordering) == len(self.digraph):
            return topological_ordering  # got them all
        else:
            raise Exception("Graph has a cycle! No topological ordering exists.")

    # Time Complexity: O(V+E).
    # Auxiliary space: O(V).


# Driver code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print("Following is a Topological Sort of the given graph")
print("ORDER", g.topological_sort())
