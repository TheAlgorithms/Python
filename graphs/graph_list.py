#!/usr/bin/python

# Author: OMKAR PATHAK

# We can use Python's dictionary for constructing the graph.


class AdjacencyList:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        # check if vertex is already present
        if from_vertex in self.adj_list:
            self.adj_list[from_vertex].append(to_vertex)
        else:
            self.adj_list[from_vertex] = [to_vertex]

    def print_list(self) -> None:
        for i in self.adj_list:
            print((i, "->", " -> ".join([str(j) for j in self.adj_list[i]])))


if __name__ == "__main__":
    al = AdjacencyList()
    al.add_edge(0, 1)
    al.add_edge(0, 4)
    al.add_edge(4, 1)
    al.add_edge(4, 3)
    al.add_edge(1, 0)
    al.add_edge(1, 4)
    al.add_edge(1, 3)
    al.add_edge(1, 2)
    al.add_edge(2, 3)
    al.add_edge(3, 4)

    al.print_list()

    # OUTPUT:
    # 0 -> 1 -> 4
    # 1 -> 0 -> 4 -> 3 -> 2
    # 2 -> 3
    # 3 -> 4
    # 4 -> 1 -> 3
