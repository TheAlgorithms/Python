from __future__ import annotations


class DisjointSetTreeNode:
    # Disjoint Set Node to store the parent and rank
    def __init__(self, key: int) -> None:
        self.key = key
        self.parent = self
        self.rank = 0


class DisjointSetTree:
    # Disjoint Set DataStructure
    def __init__(self):
        # map from node name to the node object
        self.map = {}

    def make_set(self, x: int) -> None:
        # create a new set with x as its member
        self.map[x] = DisjointSetTreeNode(x)

    def find_set(self, x: int) -> DisjointSetTreeNode:
        # find the set x belongs to (with path-compression)
        elem_ref = self.map[x]
        if elem_ref != elem_ref.parent:
            elem_ref.parent = self.find_set(elem_ref.parent.key)
        return elem_ref.parent

    def link(self, x: int, y: int) -> None:
        # helper function for union operation
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1

    def union(self, x: int, y: int) -> None:
        # merge 2 disjoint sets
        self.link(self.find_set(x), self.find_set(y))


class GraphUndirectedWeighted:
    def __init__(self):
        # connections: map from the node to the neighbouring nodes (with weights)
        self.connections = {}

    def add_node(self, node: int) -> None:
        # add a node ONLY if its not present in the graph
        if node not in self.connections:
            self.connections[node] = {}

    def add_edge(self, node1: int, node2: int, weight: int) -> None:
        # add an edge with the given weight
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1][node2] = weight
        self.connections[node2][node1] = weight

    def kruskal(self) -> GraphUndirectedWeighted:
        # Kruskal's Algorithm to generate a Minimum Spanning Tree (MST) of a graph
        """
        Details: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

        Example:

        >>> graph = GraphUndirectedWeighted()
        >>> graph.add_edge(1, 2, 1)
        >>> graph.add_edge(2, 3, 2)
        >>> graph.add_edge(3, 4, 1)
        >>> graph.add_edge(3, 5, 100) # Removed in MST
        >>> graph.add_edge(4, 5, 5)
        >>> assert 5 in graph.connections[3]
        >>> mst = graph.kruskal()
        >>> assert 5 not in mst.connections[3]
        """

        # getting the edges in ascending order of weights
        edges = []
        seen = set()
        for start in self.connections:
            for end in self.connections[start]:
                if (start, end) not in seen:
                    seen.add((end, start))
                    edges.append((start, end, self.connections[start][end]))
        edges.sort(key=lambda x: x[2])
        # creating the disjoint set
        disjoint_set = DisjointSetTree()
        [disjoint_set.make_set(node) for node in self.connections]
        # MST generation
        num_edges = 0
        index = 0
        graph = GraphUndirectedWeighted()
        while num_edges < len(self.connections) - 1:
            u, v, w = edges[index]
            index += 1
            parentu = disjoint_set.find_set(u)
            parentv = disjoint_set.find_set(v)
            if parentu != parentv:
                num_edges += 1
                graph.add_edge(u, v, w)
                disjoint_set.union(u, v)
        return graph


if __name__ == "__main__":
    import doctest

    doctest.testmod()
