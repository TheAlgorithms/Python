# A class to represent the adjacency list of the node


class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
        self.verticeslist = []

    def add_edge(self, src, dest):
        self.verticeslist.append(src)
        self.verticeslist.append(dest)
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def adjacency_list(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
        # Saves space O(|V|+|E|) . In the worst case, there can be C(V, 2) number of edges in a graph thus consuming O(V^2) space. Adding a vertex is easier.

    def adjacency_matrix(self):
        self.verticeslist = set(self.verticeslist)
        print(self.verticeslist)
        print("ADJACENCY MATRIX for ")
        for i in self.verticeslist:
            d = []
            print("I", i)
            temp = self.graph[i]
            while temp:
                d.append(temp.vertex)
                temp = temp.next
            print(d)


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    # graph.adjacency_list()
    graph.adjacency_matrix()
