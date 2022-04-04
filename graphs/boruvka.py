"""Borůvka's algorithm.

    Determines the minimum spanning tree (MST) of a graph using the Borůvka's algorithm.
    Borůvka's algorithm is a greedy algorithm for finding a minimum spanning tree in a
    connected graph, or a minimum spanning forest if a graph that is not connected.

    The time complexity of this algorithm is O(ELogV), where E represents the number
    of edges, while V represents the number of nodes.
    O(number_of_edges Log number_of_nodes)

    The space complexity of this algorithm is O(V + E), since we have to keep a couple
    of lists whose sizes are equal to the number of nodes, as well as keep all the
    edges of a graph inside of the data structure itself.

    Borůvka's algorithm gives us pretty much the same result as other MST Algorithms -
    they all find the minimum spanning tree, and the time complexity is approximately
    the same.

    One advantage that Borůvka's algorithm has compared to the alternatives is that it
    doesn't need to presort the edges or maintain a priority queue in order to find the
    minimum spanning tree.
    Even though that doesn't help its complexity, since it still passes the edges logE
    times, it is a bit simpler to code.

    Details: https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm
"""
from __future__ import annotations

from typing import Any


class Graph:
    def __init__(self, num_of_nodes: int) -> None:
        """
        Arguments:
            num_of_nodes - the number of nodes in the graph
        Attributes:
            m_num_of_nodes - the number of nodes in the graph.
            m_edges - the list of edges.
            m_component - the dictionary which stores the index of the component which
            a node belongs to.
        """

        self.m_num_of_nodes = num_of_nodes
        self.m_edges: list[list[int]] = []
        self.m_component: dict[int, int] = {}

    def add_edge(self, u_node: int, v_node: int, weight: int) -> None:
        """Adds an edge in the format [first, second, edge weight] to graph."""

        self.m_edges.append([u_node, v_node, weight])

    def find_component(self, u_node: int) -> int:
        """Propagates a new component throughout a given component."""

        if self.m_component[u_node] == u_node:
            return u_node
        return self.find_component(self.m_component[u_node])

    def set_component(self, u_node: int) -> None:
        """Finds the component index of a given node"""

        if self.m_component[u_node] != u_node:
            for k in self.m_component:
                self.m_component[k] = self.find_component(k)

    def union(self, component_size: list[int], u_node: int, v_node: int) -> None:
        """Union finds the roots of components for two nodes, compares the components
        in terms of size, and attaches the smaller one to the larger one to form
        single component"""

        if component_size[u_node] <= component_size[v_node]:
            self.m_component[u_node] = v_node
            component_size[v_node] += component_size[u_node]
            self.set_component(u_node)

        elif component_size[u_node] >= component_size[v_node]:
            self.m_component[v_node] = self.find_component(u_node)
            component_size[u_node] += component_size[v_node]
            self.set_component(v_node)

    def boruvka(self) -> None:
        """Performs Borůvka's algorithm to find MST."""

        # Initialize additional lists required to algorithm.
        component_size = []
        mst_weight = 0

        minimum_weight_edge: list[Any] = [-1] * self.m_num_of_nodes

        # A list of components (initialized to all of the nodes)
        for node in range(self.m_num_of_nodes):
            self.m_component.update({node: node})
            component_size.append(1)

        num_of_components = self.m_num_of_nodes

        while num_of_components > 1:
            for edge in self.m_edges:
                u, v, w = edge

                u_component = self.m_component[u]
                v_component = self.m_component[v]

                if u_component != v_component:
                    """If the current minimum weight edge of component u doesn't
                    exist (is -1), or if it's greater than the edge we're
                    observing right now, we will assign the value of the edge
                    we're observing to it.

                    If the current minimum weight edge of component v doesn't
                    exist (is -1), or if it's greater than the edge we're
                    observing right now, we will assign the value of the edge
                    we're observing to it"""

                    for component in (u_component, v_component):
                        if (
                            minimum_weight_edge[component] == -1
                            or minimum_weight_edge[component][2] > w
                        ):
                            minimum_weight_edge[component] = [u, v, w]

            for edge in minimum_weight_edge:
                if isinstance(edge, list):
                    u, v, w = edge

                    u_component = self.m_component[u]
                    v_component = self.m_component[v]

                    if u_component != v_component:
                        mst_weight += w
                        self.union(component_size, u_component, v_component)
                        print(f"Added edge [{u} - {v}]\nAdded weight: {w}\n")
                        num_of_components -= 1

            minimum_weight_edge = [-1] * self.m_num_of_nodes
        print(f"The total weight of the minimal spanning tree is: {mst_weight}")


def test_vector() -> None:
    """
    >>> g = Graph(8)
    >>> for u_v_w in ((0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4),
    ...    (3, 4, 8), (4, 5, 10), (4, 6, 6), (4, 7, 5), (5, 7, 15), (6, 7, 4)):
    ...        g.add_edge(*u_v_w)
    >>> g.boruvka()
    Added edge [0 - 3]
    Added weight: 5
    <BLANKLINE>
    Added edge [0 - 1]
    Added weight: 10
    <BLANKLINE>
    Added edge [2 - 3]
    Added weight: 4
    <BLANKLINE>
    Added edge [4 - 7]
    Added weight: 5
    <BLANKLINE>
    Added edge [4 - 5]
    Added weight: 10
    <BLANKLINE>
    Added edge [6 - 7]
    Added weight: 4
    <BLANKLINE>
    Added edge [3 - 4]
    Added weight: 8
    <BLANKLINE>
    The total weight of the minimal spanning tree is: 46
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
