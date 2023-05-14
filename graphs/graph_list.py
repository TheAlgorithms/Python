#!/usr/bin/env python3

# Original Authors: OMKAR PATHAK, Nwachukwu Chidiebere
# Redesigned and reimplemented by Vikram Nithyanandam

# Use an adjacency list via Python dictionary to construct the graph.
from __future__ import annotations

from pprint import pformat
from typing import Generic, TypeVar

T = TypeVar("T")


class GraphAdjacencyList(Generic[T]):
    """
    Adjacency List type Graph Data Structure that accounts for directed and undirected
    Graphs. Initialize graph object indicating whether it's directed or undirected.
    """

    def __init__(
        self, vertices: list[T] = [], edges: list[list[T]] = [], directed: bool = True
    ) -> None:
        """
        Parameters:
        directed: (bool) Indicates if graph is directed or undirected. Default is True.
        """
        self.adj_list: dict[T, list[T]] = {}  # dictionary of lists of T
        self.directed = directed

        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            if len(edge) != 2:
                raise ValueError(f"Invalid input: {edge} is the wrong length.")
            self.add_edge(edge[0], edge[1])

    def add_vertex(self, vertex: T) -> GraphAdjacencyList[T]:
        """
        Adds a vertex to the graph. If the given vertex already exists, a ValueError will
        be thrown.
        """
        if not self.contains_vertex(vertex):
            self.adj_list[vertex] = []
        else:
            raise ValueError(f"Incorrect input: {vertex} is already in the graph.")

    def add_edge(
        self, source_vertex: T, destination_vertex: T
    ) -> GraphAdjacencyList[T]:
        """
        Creates an edge from source vertex to destination vertex. If any given vertex doesn't exist
        or the edge already exists, a ValueError will be thrown.
        """
        if (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
            and not self.contains_edge(source_vertex, destination_vertex)
        ):
            self.adj_list[source_vertex].append(destination_vertex)
            if not self.directed:
                self.adj_list[destination_vertex].append(source_vertex)
        else:
            raise ValueError(
                f"Incorrect input: Either {source_vertex} or {destination_vertex} does not exist \
                  OR the requested edge already exists between them."
            )
        return self

    def remove_vertex(self, vertex: T) -> GraphAdjacencyList[T]:
        """
        Removes the given vertex from the graph and deletes all incoming and outgoing edges from
        the given vertex as well. If the given vertex does not exist, a ValueError will be thrown.
        """
        if self.contains_vertex(vertex):
            if not self.directed:
                # If not directed, find all neighboring vertices and delete all references of
                # edges connecting to the given vertex
                for neighbor in self.adj_list[vertex]:
                    self.adj_list[neighbor].remove(vertex)
            else:
                # If directed, search all neighbors of all vertices and delete all references of
                # edges connecting to the given vertex
                for edge_list in self.adj_list.values():
                    if vertex in edge_list:
                        edge_list.remove(vertex)

            # Finally, delete the given vertex and all of its outgoing edge references
            self.adj_list.pop(vertex)
        else:
            raise ValueError(f"Incorrect input: {vertex} does not exist in this graph.")

    def remove_edge(
        self, source_vertex: T, destination_vertex: T
    ) -> GraphAdjacencyList[T]:
        """
        Removes the edge between the two vertices. If any given vertex doesn't exist
        or the edge does not exist, a ValueError will be thrown.
        """
        if (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
            and self.contains_edge(source_vertex, destination_vertex)
        ):
            self.adj_list[source_vertex].remove(destination_vertex)
            if not self.directed:
                self.adj_list[destination_vertex].remove(source_vertex)
        else:
            raise ValueError(
                f"Incorrect input: Either {source_vertex} or {destination_vertex} do not exist \
                OR the requested edge does not exists between them."
            )

    def contains_vertex(self, vertex: T) -> bool:
        """
        Returns True if the graph contains the vertex, False otherwise.
        """
        return vertex in self.adj_list

    def contains_edge(self, source_vertex: T, destination_vertex: T) -> bool:
        """
        Returns True if the graph contains the edge from the source_vertex to the
        destination_vertex, False otherwise. If any given vertex doesn't exist, a
        ValueError will be thrown.
        """
        if self.contains_vertex(source_vertex) and self.contains_vertex(
            destination_vertex
        ):
            return True if destination_vertex in self.adj_list[source_vertex] else False
        else:
            raise ValueError(
                f"Incorrect input: Either {source_vertex} or {destination_vertex} does not exist."
            )

    def clear_graph(self) -> None:
        self.adj_list: dict[T, list[T]] = {}

    def __repr__(self) -> str:
        return pformat(self.adj_list)
