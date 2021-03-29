#!/usr/bin/env python3

# Author: OMKAR PATHAK, Nwachukwu Chidiebere

# Use a Python dictionary to construct the graph.

from pprint import pformat


class GraphAdjacencyList:
    """
    Adjacency List type Graph Data Structure that accounts for directed and undirected
    Graphs.  Initialize graph object indicating whether it's directed or undirected.

    Directed graph example:
    >>> d_graph = GraphAdjacencyList()
    >>> d_graph
    {}
    >>> d_graph.add_edge(0, 1)
    {0: [1], 1: []}
    >>> d_graph.add_edge(1, 2).add_edge(1, 4).add_edge(1, 5)
    {0: [1], 1: [2, 4, 5], 2: [], 4: [], 5: []}
    >>> d_graph.add_edge(2, 0).add_edge(2, 6).add_edge(2, 7)
    {0: [1], 1: [2, 4, 5], 2: [0, 6, 7], 4: [], 5: [], 6: [], 7: []}
    >>> print(d_graph)
    {0: [1], 1: [2, 4, 5], 2: [0, 6, 7], 4: [], 5: [], 6: [], 7: []}
    >>> print(repr(d_graph))
    {0: [1], 1: [2, 4, 5], 2: [0, 6, 7], 4: [], 5: [], 6: [], 7: []}

    Undirected graph example:
    >>> u_graph = GraphAdjacencyList(directed=False)
    >>> u_graph.add_edge(0, 1)
    {0: [1], 1: [0]}
    >>> u_graph.add_edge(1, 2).add_edge(1, 4).add_edge(1, 5)
    {0: [1], 1: [0, 2, 4, 5], 2: [1], 4: [1], 5: [1]}
    >>> u_graph.add_edge(2, 0).add_edge(2, 6).add_edge(2, 7)
    {0: [1, 2], 1: [0, 2, 4, 5], 2: [1, 0, 6, 7], 4: [1], 5: [1], 6: [2], 7: [2]}
    >>> u_graph.add_edge(4, 5)
    {0: [1, 2],
     1: [0, 2, 4, 5],
     2: [1, 0, 6, 7],
     4: [1, 5],
     5: [1, 4],
     6: [2],
     7: [2]}
    >>> print(u_graph)
    {0: [1, 2],
     1: [0, 2, 4, 5],
     2: [1, 0, 6, 7],
     4: [1, 5],
     5: [1, 4],
     6: [2],
     7: [2]}
    >>> print(repr(u_graph))
    {0: [1, 2],
     1: [0, 2, 4, 5],
     2: [1, 0, 6, 7],
     4: [1, 5],
     5: [1, 4],
     6: [2],
     7: [2]}
    """

    def __init__(self, directed: bool = True):
        """
        Parameters:
        directed: (bool) Indicates if graph is directed or undirected. Default is True.
        """

        self.adj_list = {}  # dictionary of lists
        self.directed = directed

    def add_edge(self, source_vertex: int, destination_vertex: int) -> object:
        """
        Connects vertices together. Creates and Edge from source vertex to destination
        vertex.
        Vertices will be created if not found in graph
        """

        if not self.directed:  # For undirected graphs
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
        else:  # For directed graphs
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

        return self

    def __repr__(self) -> str:
        return pformat(self.adj_list)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
