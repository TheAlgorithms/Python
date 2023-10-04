#!/usr/bin/python

""" Author: OMKAR PATHAK """


class Graph:
    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertices
    def print_graph(self) -> None:
        print(self.vertex)
        for i in self.vertex:
            print(i, " -> ", " -> ".join([str(j) for j in self.vertex[i]]))

    # for adding the edge between two vertices
    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        # check if vertex is already present,
        if from_vertex in self.vertex:
            self.vertex[from_vertex].append(to_vertex)
        else:
            # else make a new vertex
            self.vertex[from_vertex] = [to_vertex]

    def dfs(self) -> None:
        # visited array for storing already visited nodes
        visited = [False] * len(self.vertex)

        # call the recursive helper function
        for i in range(len(self.vertex)):
            if not visited[i]:
                self.dfs_recursive(i, visited)

    def dfs_recursive(self, start_vertex: int, visited: list) -> None:
        # mark start vertex as visited
        visited[start_vertex] = True

        print(start_vertex, end=" ")

        # Recur for all the vertices that are adjacent to this node
        for i in self.vertex:
            if not visited[i]:
                self.dfs_recursive(i, visited)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.print_graph()
    print("DFS:")
    g.dfs()

    # OUTPUT:
    # 0  ->  1 -> 2
    # 1  ->  2
    # 2  ->  0 -> 3
    # 3  ->  3
    # DFS:
    #  0 1 2 3
