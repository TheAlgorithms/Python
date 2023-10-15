#!/usr/bin/env python3
"""
Author: Vikram Nithyanandam

Description:
The following implementation is a robust unweighted Graph data structure
implemented using an adjacency list. This vertices and edges of this graph can be
effectively initialized and modified while storing your chosen generic
value in each vertex.

Adjacency List: https://en.wikipedia.org/wiki/Adjacency_list

Potential Future Ideas:
- Add a flag to set edge weights on and set edge weights
- Make edge weights and vertex values customizable to store whatever the client wants
- Support multigraph functionality if the client wants it
"""
from __future__ import annotations

import random
import unittest
from pprint import pformat
from typing import Generic, TypeVar

import pytest

T = TypeVar("T")


class GraphAdjacencyList(Generic[T]):
    def __init__(
        self, vertices: list[T], edges: list[list[T]], directed: bool = True
    ) -> None:
        """
        Parameters:
         - vertices: (list[T]) The list of vertex names the client wants to
        pass in. Default is empty.
        - edges: (list[list[T]]) The list of edges the client wants to
        pass in. Each edge is a 2-element list. Default is empty.
        - directed: (bool) Indicates if graph is directed or undirected.
        Default is True.
        """
        self.adj_list: dict[T, list[T]] = {}  # dictionary of lists of T
        self.directed = directed

        # Falsey checks
        edges = edges or []
        vertices = vertices or []

        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            if len(edge) != 2:
                msg = f"Invalid input: {edge} is the wrong length."
                raise ValueError(msg)
            self.add_edge(edge[0], edge[1])

    def add_vertex(self, vertex: T) -> None:
        """
        Adds a vertex to the graph. If the given vertex already exists,
        a ValueError will be thrown.
        """
        if self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} is already in the graph."
            raise ValueError(msg)
        self.adj_list[vertex] = []

    def add_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        Creates an edge from source vertex to destination vertex. If any
        given vertex doesn't exist or the edge already exists, a ValueError
        will be thrown.
        """
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} or "
                f"{destination_vertex} does not exist"
            )
            raise ValueError(msg)
        if self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Incorrect input: The edge already exists between "
                f"{source_vertex} and {destination_vertex}"
            )
            raise ValueError(msg)

        # add the destination vertex to the list associated with the source vertex
        # and vice versa if not directed
        self.adj_list[source_vertex].append(destination_vertex)
        if not self.directed:
            self.adj_list[destination_vertex].append(source_vertex)

    def remove_vertex(self, vertex: T) -> None:
        """
        Removes the given vertex from the graph and deletes all incoming and
        outgoing edges from the given vertex as well. If the given vertex
        does not exist, a ValueError will be thrown.
        """
        if not self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} does not exist in this graph."
            raise ValueError(msg)

        if not self.directed:
            # If not directed, find all neighboring vertices and delete all references
            # of edges connecting to the given vertex
            for neighbor in self.adj_list[vertex]:
                self.adj_list[neighbor].remove(vertex)
        else:
            # If directed, search all neighbors of all vertices and delete all
            # references of edges connecting to the given vertex
            for edge_list in self.adj_list.values():
                if vertex in edge_list:
                    edge_list.remove(vertex)

        # Finally, delete the given vertex and all of its outgoing edge references
        self.adj_list.pop(vertex)

    def remove_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        Removes the edge between the two vertices. If any given vertex
        doesn't exist or the edge does not exist, a ValueError will be thrown.
        """
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} or "
                f"{destination_vertex} does not exist"
            )
            raise ValueError(msg)
        if not self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Incorrect input: The edge does NOT exist between "
                f"{source_vertex} and {destination_vertex}"
            )
            raise ValueError(msg)

        # remove the destination vertex from the list associated with the source
        # vertex and vice versa if not directed
        self.adj_list[source_vertex].remove(destination_vertex)
        if not self.directed:
            self.adj_list[destination_vertex].remove(source_vertex)

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
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} "
                f"or {destination_vertex} does not exist."
            )
            raise ValueError(msg)

        return destination_vertex in self.adj_list[source_vertex]

    def clear_graph(self) -> None:
        """
        Clears all vertices and edges.
        """
        self.adj_list = {}

    def __repr__(self) -> str:
        return pformat(self.adj_list)


class TestGraphAdjacencyList(unittest.TestCase):
    def __assert_graph_edge_exists_check(
        self,
        undirected_graph: GraphAdjacencyList,
        directed_graph: GraphAdjacencyList,
        edge: list[int],
    ) -> None:
        assert undirected_graph.contains_edge(edge[0], edge[1])
        assert undirected_graph.contains_edge(edge[1], edge[0])
        assert directed_graph.contains_edge(edge[0], edge[1])

    def __assert_graph_edge_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyList,
        directed_graph: GraphAdjacencyList,
        edge: list[int],
    ) -> None:
        assert not undirected_graph.contains_edge(edge[0], edge[1])
        assert not undirected_graph.contains_edge(edge[1], edge[0])
        assert not directed_graph.contains_edge(edge[0], edge[1])

    def __assert_graph_vertex_exists_check(
        self,
        undirected_graph: GraphAdjacencyList,
        directed_graph: GraphAdjacencyList,
        vertex: int,
    ) -> None:
        assert undirected_graph.contains_vertex(vertex)
        assert directed_graph.contains_vertex(vertex)

    def __assert_graph_vertex_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyList,
        directed_graph: GraphAdjacencyList,
        vertex: int,
    ) -> None:
        assert not undirected_graph.contains_vertex(vertex)
        assert not directed_graph.contains_vertex(vertex)

    def __generate_random_edges(
        self, vertices: list[int], edge_pick_count: int
    ) -> list[list[int]]:
        assert edge_pick_count <= len(vertices)

        random_source_vertices: list[int] = random.sample(
            vertices[0 : int(len(vertices) / 2)], edge_pick_count
        )
        random_destination_vertices: list[int] = random.sample(
            vertices[int(len(vertices) / 2) :], edge_pick_count
        )
        random_edges: list[list[int]] = []

        for source in random_source_vertices:
            for dest in random_destination_vertices:
                random_edges.append([source, dest])

        return random_edges

    def __generate_graphs(
        self, vertex_count: int, min_val: int, max_val: int, edge_pick_count: int
    ) -> tuple[GraphAdjacencyList, GraphAdjacencyList, list[int], list[list[int]]]:
        if max_val - min_val + 1 < vertex_count:
            raise ValueError(
                "Will result in duplicate vertices. Either increase range "
                "between min_val and max_val or decrease vertex count."
            )

        # generate graph input
        random_vertices: list[int] = random.sample(
            range(min_val, max_val + 1), vertex_count
        )
        random_edges: list[list[int]] = self.__generate_random_edges(
            random_vertices, edge_pick_count
        )

        # build graphs
        undirected_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=random_edges, directed=False
        )
        directed_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=random_edges, directed=True
        )

        return undirected_graph, directed_graph, random_vertices, random_edges

    def test_init_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # test graph initialization with vertices and edges
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

        for edge in random_edges:
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )
        assert not undirected_graph.directed
        assert directed_graph.directed

    def test_contains_vertex(self) -> None:
        random_vertices: list[int] = random.sample(range(101), 20)

        # Build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=[], directed=True
        )

        # Test contains_vertex
        for num in range(101):
            assert (num in random_vertices) == undirected_graph.contains_vertex(num)
            assert (num in random_vertices) == directed_graph.contains_vertex(num)

    def test_add_vertices(self) -> None:
        random_vertices: list[int] = random.sample(range(101), 20)

        # build empty graphs
        undirected_graph: GraphAdjacencyList = GraphAdjacencyList(
            vertices=[], edges=[], directed=False
        )
        directed_graph: GraphAdjacencyList = GraphAdjacencyList(
            vertices=[], edges=[], directed=True
        )

        # run add_vertex
        for num in random_vertices:
            undirected_graph.add_vertex(num)

        for num in random_vertices:
            directed_graph.add_vertex(num)

        # test add_vertex worked
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

    def test_remove_vertices(self) -> None:
        random_vertices: list[int] = random.sample(range(101), 20)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=[], directed=True
        )

        # test remove_vertex worked
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

            undirected_graph.remove_vertex(num)
            directed_graph.remove_vertex(num)

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, num
            )

    def test_add_and_remove_vertices_repeatedly(self) -> None:
        random_vertices1: list[int] = random.sample(range(51), 20)
        random_vertices2: list[int] = random.sample(range(51, 101), 20)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyList(
            vertices=random_vertices1, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyList(
            vertices=random_vertices1, edges=[], directed=True
        )

        # test adding and removing vertices
        for i, _ in enumerate(random_vertices1):
            undirected_graph.add_vertex(random_vertices2[i])
            directed_graph.add_vertex(random_vertices2[i])

            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, random_vertices2[i]
            )

            undirected_graph.remove_vertex(random_vertices1[i])
            directed_graph.remove_vertex(random_vertices1[i])

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, random_vertices1[i]
            )

        # remove all vertices
        for i, _ in enumerate(random_vertices1):
            undirected_graph.remove_vertex(random_vertices2[i])
            directed_graph.remove_vertex(random_vertices2[i])

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, random_vertices2[i]
            )

    def test_contains_edge(self) -> None:
        # generate graphs and graph input
        vertex_count = 20
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(vertex_count, 0, 100, 4)

        # generate all possible edges for testing
        all_possible_edges: list[list[int]] = []
        for i in range(vertex_count - 1):
            for j in range(i + 1, vertex_count):
                all_possible_edges.append([random_vertices[i], random_vertices[j]])
                all_possible_edges.append([random_vertices[j], random_vertices[i]])

        # test contains_edge function
        for edge in all_possible_edges:
            if edge in random_edges:
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, edge
                )
            elif [edge[1], edge[0]] in random_edges:
                # since this edge exists for undirected but the reverse
                # may not exist for directed
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, [edge[1], edge[0]]
                )
            else:
                self.__assert_graph_edge_does_not_exist_check(
                    undirected_graph, directed_graph, edge
                )

    def test_add_edge(self) -> None:
        # generate graph input
        random_vertices: list[int] = random.sample(range(101), 15)
        random_edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=[], directed=True
        )

        # run and test add_edge
        for edge in random_edges:
            undirected_graph.add_edge(edge[0], edge[1])
            directed_graph.add_edge(edge[0], edge[1])
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )

    def test_remove_edge(self) -> None:
        # generate graph input and graphs
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # run and test remove_edge
        for edge in random_edges:
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )
            undirected_graph.remove_edge(edge[0], edge[1])
            directed_graph.remove_edge(edge[0], edge[1])
            self.__assert_graph_edge_does_not_exist_check(
                undirected_graph, directed_graph, edge
            )

    def test_add_and_remove_edges_repeatedly(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # make some more edge options!
        more_random_edges: list[list[int]] = []

        while len(more_random_edges) != len(random_edges):
            edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)
            for edge in edges:
                if len(more_random_edges) == len(random_edges):
                    break
                elif edge not in more_random_edges and edge not in random_edges:
                    more_random_edges.append(edge)

        for i, _ in enumerate(random_edges):
            undirected_graph.add_edge(more_random_edges[i][0], more_random_edges[i][1])
            directed_graph.add_edge(more_random_edges[i][0], more_random_edges[i][1])

            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, more_random_edges[i]
            )

            undirected_graph.remove_edge(random_edges[i][0], random_edges[i][1])
            directed_graph.remove_edge(random_edges[i][0], random_edges[i][1])

            self.__assert_graph_edge_does_not_exist_check(
                undirected_graph, directed_graph, random_edges[i]
            )

    def test_add_vertex_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with pytest.raises(ValueError):
                undirected_graph.add_vertex(vertex)
            with pytest.raises(ValueError):
                directed_graph.add_vertex(vertex)

    def test_remove_vertex_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for i in range(101):
            if i not in random_vertices:
                with pytest.raises(ValueError):
                    undirected_graph.remove_vertex(i)
                with pytest.raises(ValueError):
                    directed_graph.remove_vertex(i)

    def test_add_edge_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for edge in random_edges:
            with pytest.raises(ValueError):
                undirected_graph.add_edge(edge[0], edge[1])
            with pytest.raises(ValueError):
                directed_graph.add_edge(edge[0], edge[1])

    def test_remove_edge_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        more_random_edges: list[list[int]] = []

        while len(more_random_edges) != len(random_edges):
            edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)
            for edge in edges:
                if len(more_random_edges) == len(random_edges):
                    break
                elif edge not in more_random_edges and edge not in random_edges:
                    more_random_edges.append(edge)

        for edge in more_random_edges:
            with pytest.raises(ValueError):
                undirected_graph.remove_edge(edge[0], edge[1])
            with pytest.raises(ValueError):
                directed_graph.remove_edge(edge[0], edge[1])

    def test_contains_edge_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with pytest.raises(ValueError):
                undirected_graph.contains_edge(vertex, 102)
            with pytest.raises(ValueError):
                directed_graph.contains_edge(vertex, 102)

        with pytest.raises(ValueError):
            undirected_graph.contains_edge(103, 102)
        with pytest.raises(ValueError):
            directed_graph.contains_edge(103, 102)


if __name__ == "__main__":
    unittest.main()
