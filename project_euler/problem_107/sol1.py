"""
The following undirected network consists of seven vertices and twelve edges
with a total weight of 243.
￼
The same network can be represented by the matrix below.

    A   B   C   D   E   F   G
A   -   16  12  21  -   -   -
B   16  -   -   17  20  -   -
C   12  -   -   28  -   31  -
D   21  17  28  -   18  19  23
E   -   20  -   18  -   -   11
F   -   -   31  19  -   -   27
G   -   -   -   23  11  27  -

However, it is possible to optimise the network by removing some edges and still
ensure that all points on the network remain connected. The network which achieves
the maximum saving is shown below. It has a weight of 93, representing a saving of
243 - 93 = 150 from the original network.

Using network.txt (right click and 'Save Link/Target As...'), a 6K text file
containing a network with forty vertices, and given in matrix form, find the maximum
saving which can be achieved by removing redundant edges whilst ensuring that the
network remains connected.

Solution:
    We use Prim's algorithm to find a Minimum Spanning Tree.
    Reference: https://en.wikipedia.org/wiki/Prim%27s_algorithm
"""
from __future__ import annotations

import os
from collections.abc import Mapping

EdgeT = tuple[int, int]


class Graph:
    """
    A class representing an undirected weighted graph.
    """

    def __init__(self, vertices: set[int], edges: Mapping[EdgeT, int]) -> None:
        self.vertices: set[int] = vertices
        self.edges: dict[EdgeT, int] = {
            (min(edge), max(edge)): weight for edge, weight in edges.items()
        }

    def add_edge(self, edge: EdgeT, weight: int) -> None:
        """
        Add a new edge to the graph.
        >>> graph = Graph({1, 2}, {(2, 1): 4})
        >>> graph.add_edge((3, 1), 5)
        >>> sorted(graph.vertices)
        [1, 2, 3]
        >>> sorted([(v,k) for k,v in graph.edges.items()])
        [(4, (1, 2)), (5, (1, 3))]
        """
        self.vertices.add(edge[0])
        self.vertices.add(edge[1])
        self.edges[(min(edge), max(edge))] = weight

    def prims_algorithm(self) -> Graph:
        """
        Run Prim's algorithm to find the minimum spanning tree.
        Reference: https://en.wikipedia.org/wiki/Prim%27s_algorithm
        >>> graph = Graph({1,2,3,4},{(1,2):5, (1,3):10, (1,4):20, (2,4):30, (3,4):1})
        >>> mst = graph.prims_algorithm()
        >>> sorted(mst.vertices)
        [1, 2, 3, 4]
        >>> sorted(mst.edges)
        [(1, 2), (1, 3), (3, 4)]
        """
        subgraph: Graph = Graph({min(self.vertices)}, {})
        min_edge: EdgeT
        min_weight: int
        edge: EdgeT
        weight: int

        while len(subgraph.vertices) < len(self.vertices):
            min_weight = max(self.edges.values()) + 1
            for edge, weight in self.edges.items():
                if (edge[0] in subgraph.vertices) ^ (edge[1] in subgraph.vertices):
                    if weight < min_weight:
                        min_edge = edge
                        min_weight = weight

            subgraph.add_edge(min_edge, min_weight)

        return subgraph


def solution(filename: str = "p107_network.txt") -> int:
    """
    Find the maximum saving which can be achieved by removing redundant edges
    whilst ensuring that the network remains connected.
    >>> solution("test_network.txt")
    150
    """
    script_dir: str = os.path.abspath(os.path.dirname(__file__))
    network_file: str = os.path.join(script_dir, filename)
    edges: dict[EdgeT, int] = {}
    data: list[str]
    edge1: int
    edge2: int

    with open(network_file) as f:
        data = f.read().strip().split("\n")

    adjaceny_matrix = [line.split(",") for line in data]

    for edge1 in range(1, len(adjaceny_matrix)):
        for edge2 in range(edge1):
            if adjaceny_matrix[edge1][edge2] != "-":
                edges[(edge2, edge1)] = int(adjaceny_matrix[edge1][edge2])

    graph: Graph = Graph(set(range(len(adjaceny_matrix))), edges)

    subgraph: Graph = graph.prims_algorithm()

    initial_total: int = sum(graph.edges.values())
    optimal_total: int = sum(subgraph.edges.values())

    return initial_total - optimal_total


if __name__ == "__main__":
    print(f"{solution() = }")
