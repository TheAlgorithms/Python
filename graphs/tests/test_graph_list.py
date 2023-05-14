import sys
import random
from typing import Tuple
import unittest

sys.path.append("..")
from graph_list import GraphAdjacencyList


class TestGraphList(unittest.TestCase):
    def __assert_graph_edge_exists_check(
        self,
        undirected_graph: GraphAdjacencyList,
        directed_graph: GraphAdjacencyList,
        edge: list[int],
    ):
        self.assertTrue(undirected_graph.contains_edge(edge[0], edge[1]))
        self.assertTrue(undirected_graph.contains_edge(edge[1], edge[0]))
        self.assertTrue(directed_graph.contains_edge(edge[0], edge[1]))

    def __assert_graph_edge_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyList,
        directed_graph: GraphAdjacencyList,
        edge: list[int],
    ):
        self.assertFalse(undirected_graph.contains_edge(edge[0], edge[1]))
        self.assertFalse(undirected_graph.contains_edge(edge[1], edge[0]))
        self.assertFalse(directed_graph.contains_edge(edge[0], edge[1]))

    def __assert_graph_vertex_exists_check(
        self,
        undirected_graph: GraphAdjacencyList,
        directed_graph: GraphAdjacencyList,
        vertex: int,
    ):
        self.assertTrue(undirected_graph.contains_vertex(vertex))
        self.assertTrue(directed_graph.contains_vertex(vertex))

    def __assert_graph_vertex_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyList,
        directed_graph: GraphAdjacencyList,
        vertex: int,
    ):
        self.assertFalse(undirected_graph.contains_vertex(vertex))
        self.assertFalse(directed_graph.contains_vertex(vertex))

    def __generate_random_edges(
        self, vertices: list[int], edge_pick_count: int
    ) -> list[list[int]]:
        self.assertTrue(edge_pick_count <= len(vertices))

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
    ) -> Tuple[GraphAdjacencyList, GraphAdjacencyList, list[int], list[list[int]]]:
        if max_val - min_val + 1 < vertex_count:
            raise ValueError(
                "Will result in duplicate vertices, either increase range or decrease vertex count"
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

    def test_init_check(self):
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
        self.assertFalse(undirected_graph.directed)
        self.assertTrue(directed_graph.directed)

    def test_contains_vertex(self):
        random_vertices: list[int] = random.sample(range(101), 20)

        # Build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyList(vertices=random_vertices, directed=False)
        directed_graph = GraphAdjacencyList(vertices=random_vertices, directed=True)

        # Test contains_vertex
        for num in range(101):
            self.assertEqual(
                num in random_vertices, undirected_graph.contains_vertex(num)
            )
            self.assertEqual(
                num in random_vertices, directed_graph.contains_vertex(num)
            )

    def test_add_vertices(self):
        random_vertices: list[int] = random.sample(range(101), 20)

        # build empty graphs
        undirected_graph = GraphAdjacencyList(directed=False)
        directed_graph = GraphAdjacencyList(directed=True)

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

    def test_remove_vertices(self):
        random_vertices: list[int] = random.sample(range(101), 20)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyList(vertices=random_vertices, directed=False)
        directed_graph = GraphAdjacencyList(vertices=random_vertices, directed=True)

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

    def test_add_and_remove_vertices_repeatedly(self):
        random_vertices1: list[int] = random.sample(range(51), 20)
        random_vertices2: list[int] = random.sample(range(51, 101), 20)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyList(vertices=random_vertices1, directed=False)
        directed_graph = GraphAdjacencyList(vertices=random_vertices1, directed=True)

        # test adding and removing vertices
        for i in range(len(random_vertices1)):
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
        for i in range(len(random_vertices1)):
            undirected_graph.remove_vertex(random_vertices2[i])
            directed_graph.remove_vertex(random_vertices2[i])

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, random_vertices2[i]
            )

    def test_contains_edge(self):
        # generate graphs and graph input
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # generate all possible edges for testing
        all_possible_edges: list[list[int]] = []
        for i in range(len(random_vertices) - 1):
            for j in range(i + 1, len(random_vertices)):
                all_possible_edges.append([random_vertices[i], random_vertices[j]])
                all_possible_edges.append([random_vertices[j], random_vertices[i]])

        # test contains_edge function
        for edge in all_possible_edges:
            if edge in random_edges:
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, edge
                )
            elif [edge[1], edge[0]] in random_edges:
                # since this edge exists for undirected but the reverse may not exist for directed
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, [edge[1], edge[0]]
                )
            else:
                self.__assert_graph_edge_does_not_exist_check(
                    undirected_graph, directed_graph, edge
                )

    def test_add_edge(self):
        # generate graph input
        random_vertices: list[int] = random.sample(range(101), 15)
        random_edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyList(vertices=random_vertices, directed=False)
        directed_graph = GraphAdjacencyList(vertices=random_vertices, directed=True)

        # run and test add_edge
        for edge in random_edges:
            undirected_graph.add_edge(edge[0], edge[1])
            directed_graph.add_edge(edge[0], edge[1])
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )

    def test_remove_edge(self):
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

    def test_add_and_remove_edges_repeatedly(self):
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

        for i in range(len(random_edges)):
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

    def test_add_vertex_exception_check(self):
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with self.assertRaises(ValueError):
                undirected_graph.add_vertex(vertex)
            with self.assertRaises(ValueError):
                directed_graph.add_vertex(vertex)

    def test_remove_vertex_exception_check(self):
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for i in range(101):
            if i not in random_vertices:
                with self.assertRaises(ValueError):
                    undirected_graph.remove_vertex(i)
                with self.assertRaises(ValueError):
                    directed_graph.remove_vertex(i)

    def test_add_edge_exception_check(self):
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for edge in random_edges:
            with self.assertRaises(ValueError):
                undirected_graph.add_edge(edge[0], edge[1])
            with self.assertRaises(ValueError):
                directed_graph.add_edge(edge[0], edge[1])

    def test_remove_edge_exception_check(self):
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
            with self.assertRaises(ValueError):
                undirected_graph.remove_edge(edge[0], edge[1])
            with self.assertRaises(ValueError):
                directed_graph.remove_edge(edge[0], edge[1])

    def test_contains_edge_exception_check(self):
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with self.assertRaises(ValueError):
                undirected_graph.contains_edge(vertex, 102)
            with self.assertRaises(ValueError):
                directed_graph.contains_edge(vertex, 102)

        with self.assertRaises(ValueError):
            undirected_graph.contains_edge(103, 102)
        with self.assertRaises(ValueError):
            directed_graph.contains_edge(103, 102)


if __name__ == "__main__":
    unittest.main()
