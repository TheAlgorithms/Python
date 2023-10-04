class Graph:
    """
    Data structure to store graphs (based on adjacency lists)
    """

    def __init__(self):
        self.num_vertices = 0
        self.num_edges = 0
        self.adjacency = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph

        """
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}
            self.num_vertices += 1

    def add_edge(self, head, tail, weight):
        """
        Adds an edge to the graph

        """

        self.add_vertex(head)
        self.add_vertex(tail)

        if head == tail:
            return

        self.adjacency[head][tail] = weight
        self.adjacency[tail][head] = weight

    def distinct_weight(self):
        """
        For Boruvks's algorithm the weights should be distinct
        Converts the weights to be distinct

        """
        edges = self.get_edges()
        for edge in edges:
            head, tail, weight = edge
            edges.remove((tail, head, weight))
        for i in range(len(edges)):
            edges[i] = list(edges[i])

        edges.sort(key=lambda e: e[2])
        for i in range(len(edges) - 1):
            if edges[i][2] >= edges[i + 1][2]:
                edges[i + 1][2] = edges[i][2] + 1
        for edge in edges:
            head, tail, weight = edge
            self.adjacency[head][tail] = weight
            self.adjacency[tail][head] = weight

    def __str__(self):
        """
        Returns string representation of the graph
        """
        string = ""
        for tail in self.adjacency:
            for head in self.adjacency[tail]:
                weight = self.adjacency[head][tail]
                string += f"{head} -> {tail} == {weight}\n"
        return string.rstrip("\n")

    def get_edges(self):
        """
        Returna all edges in the graph
        """
        output = []
        for tail in self.adjacency:
            for head in self.adjacency[tail]:
                output.append((tail, head, self.adjacency[head][tail]))
        return output

    def get_vertices(self):
        """
        Returns all vertices in the graph
        """
        return self.adjacency.keys()

    @staticmethod
    def build(vertices=None, edges=None):
        """
        Builds a graph from the given set of vertices and edges

        """
        g = Graph()
        if vertices is None:
            vertices = []
        if edges is None:
            edge = []
        for vertex in vertices:
            g.add_vertex(vertex)
        for edge in edges:
            g.add_edge(*edge)
        return g

    class UnionFind:
        """
        Disjoint set Union and Find for Boruvka's algorithm
        """

        def __init__(self):
            self.parent = {}
            self.rank = {}

        def __len__(self):
            return len(self.parent)

        def make_set(self, item):
            if item in self.parent:
                return self.find(item)

            self.parent[item] = item
            self.rank[item] = 0
            return item

        def find(self, item):
            if item not in self.parent:
                return self.make_set(item)
            if item != self.parent[item]:
                self.parent[item] = self.find(self.parent[item])
            return self.parent[item]

        def union(self, item1, item2):
            root1 = self.find(item1)
            root2 = self.find(item2)

            if root1 == root2:
                return root1

            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                return root1

            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
                return root2

            if self.rank[root1] == self.rank[root2]:
                self.rank[root1] += 1
                self.parent[root2] = root1
                return root1
            return None

    @staticmethod
    def boruvka_mst(graph):
        """
        Implementation of Boruvka's algorithm
        >>> g = Graph()
        >>> g = Graph.build([0, 1, 2, 3], [[0, 1, 1], [0, 2, 1],[2, 3, 1]])
        >>> g.distinct_weight()
        >>> bg = Graph.boruvka_mst(g)
        >>> print(bg)
        1 -> 0 == 1
        2 -> 0 == 2
        0 -> 1 == 1
        0 -> 2 == 2
        3 -> 2 == 3
        2 -> 3 == 3
        """
        num_components = graph.num_vertices

        union_find = Graph.UnionFind()
        mst_edges = []
        while num_components > 1:
            cheap_edge = {}
            for vertex in graph.get_vertices():
                cheap_edge[vertex] = -1

            edges = graph.get_edges()
            for edge in edges:
                head, tail, weight = edge
                edges.remove((tail, head, weight))
            for edge in edges:
                head, tail, weight = edge
                set1 = union_find.find(head)
                set2 = union_find.find(tail)
                if set1 != set2:
                    if cheap_edge[set1] == -1 or cheap_edge[set1][2] > weight:
                        cheap_edge[set1] = [head, tail, weight]

                    if cheap_edge[set2] == -1 or cheap_edge[set2][2] > weight:
                        cheap_edge[set2] = [head, tail, weight]
            for vertex in cheap_edge:
                if cheap_edge[vertex] != -1:
                    head, tail, weight = cheap_edge[vertex]
                    if union_find.find(head) != union_find.find(tail):
                        union_find.union(head, tail)
                        mst_edges.append(cheap_edge[vertex])
                        num_components = num_components - 1
        mst = Graph.build(edges=mst_edges)
        return mst
