#!/usr/bin/python

# Author: OMKAR PATHAK, Nwachukwu Chidiebere

# We can use Python's dictionary for constructing the graph.

from pprint import pformat, pprint


class GraphAdjacencyList:
    """
    Adjacency List type Graph Data Structure that accounts for directed and undirected
    Graphs.
    """

    def __init__(self, directed=True):
        """
        Initialize graph object indicating whether it's directed or undirected. Default
        is directed.

        Parameters
        ----------
            directed (bool): Indicates if graph is directed or undirected. Default is
            directed (True)
        """
        self.adj_list = {}  # dictionary of lists
        self.directed = directed

    def add_edge(self, source_vertex: int, destination_vertex: int) -> None:
        """
        Connects vertices together. Creates and Edge from source vertex to destination
        vertex.
        Vertices will be created if not found in graph
        """

        # For undirected graphs
        if not self.directed:
            # if both source vertex and destination vertex are both present in the
            # adjacency list, add destination vertex to source vertex list of adjacent
            # vertices and add source vertex to destination vertex list of adjacent
            # vertices.
            if source_vertex in self.adj_list and destination_vertex in self.adj_list:
                self.adj_list[source_vertex].append(destination_vertex)
                self.adj_list[destination_vertex].append(source_vertex)
            # if only source vertex is present in adjacency list, add destination vertex
            # to source vertex list of adjacent vertices, then create a new vertex with
            # destination vertex as key and assign a list containing the source vertex
            # as it's first adjacent vertex.
            elif source_vertex in self.adj_list:
                self.adj_list[source_vertex].append(destination_vertex)
                self.adj_list[destination_vertex] = [source_vertex]
            # if only destination vertex is present in adjacency list, add source vertex
            # to destination vertex list of adjacent vertices, then create a new vertex
            # with source vertex as key and assign a list containing the source vertex
            # as it's first adjacent vertex.
            elif destination_vertex in self.adj_list:
                self.adj_list[destination_vertex].append(source_vertex)
                self.adj_list[source_vertex] = [destination_vertex]
            # if both source vertex and destination vertex are not present in adjacency
            # list, create a new vertex with source vertex as key and assign a list
            # containing the destination vertex as it's first adjacent vertex also
            # create a new vertex with destination vertex as key and assign a list
            # containing the source vertex as it's first adjacent vertex.
            else:
                self.adj_list[source_vertex] = [destination_vertex]
                self.adj_list[destination_vertex] = [source_vertex]

        # For directed Graphs
        else:
            # if both source vertex and destination vertex are present in adjacency
            # list, add destination vertex to source vertex list of adjacent vertices.
            if source_vertex in self.adj_list and destination_vertex in self.adj_list:
                self.adj_list[source_vertex].append(destination_vertex)
            # if only source vertex is present in adjacency list, add destination
            # vertex to source vertex list of adjacent vertices and create a new vertex
            # with destination vertex as key, which has no adjacent vertex
            elif source_vertex in self.adj_list:
                self.adj_list[source_vertex].append(destination_vertex)
                self.adj_list[destination_vertex] = []
            # if only destination vertex is present in adjacency list, create a new
            # vertex with source vertex as key and assign a list containing destination
            # vertex as first adjacent vertex
            elif destination_vertex in self.adj_list:
                self.adj_list[source_vertex] = [destination_vertex]
            # if both source vertex and destination vertex are not present in adjacency
            # list, create a new vertex with source vertex as key and a list containing
            # destination vertex as it's first adjacent vertex. Then create a new vertex
            # with destination vertex as key, which has no adjacent vertex
            else:
                self.adj_list[source_vertex] = [destination_vertex]
                self.adj_list[destination_vertex] = []

    def __str__(self) -> str:
        """
        Displays adjacency list using python's pretty print function
        """
        return pformat(self.adj_list)

    def __repr__(self) -> str:
        return pformat(self.adj_list)


if __name__ == "__main__":
    # directed graph
    al = GraphAdjacencyList()
    al.add_edge(0, 1)
    al.add_edge(1, 3)
    al.add_edge(1, 4)
    al.add_edge(1, 2)
    al.add_edge(3, 7)
    al.add_edge(3, 9)
    al.add_edge(4, 5)
    al.add_edge(4, 6)
    al.add_edge(2, 8)

    print(al)

    # OUTPUT:
    # {0: [1],
    #  1: [3, 4, 2],
    #  2: [8],
    #  3: [7, 9],
    #  4: [5, 6],
    #  5: [],
    #  6: [],
    #  7: [],
    #  8: [],
    #  9: []}

    # Undirected graph
    al2 = GraphAdjacencyList(False)
    al2.add_edge(0, 1)
    al2.add_edge(1, 3)
    al2.add_edge(1, 4)
    al2.add_edge(1, 2)
    al2.add_edge(3, 7)
    al2.add_edge(3, 9)
    al2.add_edge(4, 5)
    al2.add_edge(4, 6)
    al2.add_edge(2, 8)

    print(al2)

    # OUTPUT:
    # {0: [1],
    #  1: [0, 3, 4, 2],
    #  2: [1, 8],
    #  3: [1, 7, 9],
    #  4: [1, 5, 6],
    #  5: [4],
    #  6: [4],
    #  7: [3],
    #  8: [2],
    #  9: [3]}
