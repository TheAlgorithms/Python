# Author: Vikram Nithyanandam

from __future__ import annotations

from pprint import pformat
from typing import Generic, TypeVar

T = TypeVar("T")


class GraphAdjacencyMatrix(Generic[T]):
    def __init__(
        self, vertices: list[T] = [], edges: list[list[T]] = [], directed: bool = True
    ):
        """
        Parameters:
        directed: (bool) Indicates if graph is directed or undirected. Default is True.
        vertices: (list[T]) The list of vertex names the client wants to pass in. Default is empty.
        """
        self.directed = directed
        self.vertex_to_index: dict[T, int] = {}
        self.adj_matrix: list[list[int]] = []

        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            if len(edge) != 2:
                raise ValueError(f"Invalid input: {edge} is the wrong length.")
            self.add_edge(edge[0], edge[1])

    def add_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        Creates an edge from source vertex to destination vertex. If any given vertex doesn't exist
        or the edge already exists, a ValueError will be thrown.
        """
        if (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
            and not self.contains_edge(source_vertex, destination_vertex)
        ):
            # Get the indices of the corresponding vertices and set their edge value to 1.
            u: int = self.vertex_to_index[source_vertex]
            v: int = self.vertex_to_index[destination_vertex]
            self.adj_matrix[u][v] = 1
            if not self.directed:
                self.adj_matrix[v][u] = 1
        else:
            raise ValueError(
                f"Incorrect input: Either {source_vertex} or {destination_vertex} do not exist OR \
                  there already exists an edge between them."
            )

    def remove_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        Removes the edge between the two vertices. If any given vertex doesn't exist or the edge
        does not exist, a ValueError will be thrown.
        """
        if (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
            and self.contains_edge(source_vertex, destination_vertex)
        ):
            # Get the indices of the corresponding vertices and setting their edge value to 0.
            u: int = self.vertex_to_index[source_vertex]
            v: int = self.vertex_to_index[destination_vertex]
            self.adj_matrix[u][v] = 0
            if not self.directed:
                self.adj_matrix[v][u] = 0
        else:
            raise ValueError(
                f"Incorrect input: Either {source_vertex} or {destination_vertex} do not exist \
                OR the requested edge does not exists between them."
            )

    def add_vertex(self, vertex: T) -> None:
        """
        Adds a vertex to the graph. If the given vertex already exists, a ValueError will
        be thrown.
        """
        if not self.contains_vertex(vertex):
            # build column for vertex
            for row in self.adj_matrix:
                row.append(0)

            # build row for vertex and update other data structures
            self.adj_matrix.append([0] * (len(self.adj_matrix) + 1))
            self.vertex_to_index[vertex] = len(self.adj_matrix) - 1
        else:
            raise ValueError(f"Incorrect input: {vertex} already exists in this graph.")

    def remove_vertex(self, vertex: T) -> None:
        """
        Removes the given vertex from the graph and deletes all incoming and outgoing edges from
        the given vertex as well. If the given vertex does not exist, a ValueError will be thrown.
        """
        if self.contains_vertex(vertex):
            # first slide up the rows by deleting the row corresponding to the vertex being deleted.
            start_index = self.vertex_to_index[vertex]
            self.adj_matrix.pop(start_index)

            # next, slide the columns to the left by deleting the values in the column corresponding
            # to the vertex being deleted
            for lst in self.adj_matrix:
                lst.pop(start_index)

            # final clean up
            self.vertex_to_index.pop(vertex)

            # decrement indices for vertices shifted by the deleted vertex in the adj matrix
            for vertex in self.vertex_to_index:
                if self.vertex_to_index[vertex] >= start_index:
                    self.vertex_to_index[vertex] = self.vertex_to_index[vertex] - 1
        else:
            raise ValueError(f"Incorrect input: {vertex} does not exist in this graph.")

    def contains_vertex(self, vertex: T) -> bool:
        """
        Returns True if the graph contains the vertex, False otherwise.
        """
        return vertex in self.vertex_to_index

    def contains_edge(self, source_vertex: T, destination_vertex: T) -> bool:
        """
        Returns True if the graph contains the edge from the source_vertex to the
        destination_vertex, False otherwise. If any given vertex doesn't exist, a
        ValueError will be thrown.
        """
        if self.contains_vertex(source_vertex) and self.contains_vertex(
            destination_vertex
        ):
            u = self.vertex_to_index[source_vertex]
            v = self.vertex_to_index[destination_vertex]
            return True if self.adj_matrix[u][v] == 1 else False
        else:
            raise ValueError(
                f"Incorrect input: Either {source_vertex} or {destination_vertex} does not exist."
            )

    def clear_graph(self) -> None:
        """
        Clears all vertices and edges.
        """
        self.vertices = []
        self.vertex_to_index: dict[T, int] = {}
        self.adj_matrix: list[list[int]] = []

    def __repr__(self) -> str:
        return pformat(self.adj_matrix) + "\n" + pformat(self.vertex_to_index)
