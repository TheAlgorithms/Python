class Graph:
    def __init__(self, graph, source_vertex):
        """graph is implemented as dictionary of adjancency lists"""
        self.graph = graph
        # mapping node to its parent in resulting breadth first tree
        self.parent = {}
        self.source_vertex = source_vertex

    def breath_first_search(self):
        """
        """
        visited = {self.source_vertex}
        self.parent[self.source_vertex] = None
        queue = [self.source_vertex]  # first in first out queue

        while queue:
            vertex = queue.pop(0)
            for adjancent_vertex in self.graph[vertex]:
                if adjancent_vertex not in visited:
                    visited.add(adjancent_vertex)
                    self.parent[adjancent_vertex] = vertex
                    queue.append(adjancent_vertex)

    def print_shortest_path(self, target_vertex):
        if target_vertex == self.source_vertex:
            print(self.source_vertex, end="")
        elif target_vertex not in self.parent or not self.parent[target_vertex]:
            print(f"No path from vertex:{self.source_vertex} to vertex:{target_vertex}")
        else:
            self.print_shortest_path(self.parent[target_vertex])
            print(f"->{target_vertex}", end="")


if __name__ == "__main__":
    graph = {
        "A": ["B", "C", "E"],
        "B": ["A", "D", "E"],
        "C": ["A", "F", "G"],
        "D": ["B"],
        "E": ["A", "B", "D"],
        "F": ["C"],
        "G": ["C"],
    }
    g = Graph(graph, "G")
    g.breath_first_search()
    g.print_shortest_path("D")
    print()
    g.print_shortest_path("G")
    print()
    g.print_shortest_path("Foo")
