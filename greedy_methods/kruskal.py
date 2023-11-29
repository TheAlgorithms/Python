"""
https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
"""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class Edge:
    """
    Represents an edge in a graph.

    Attributes:
        start  : The starting vertex of the edge.
        end    : The ending vertex of the edge.
        weight : The weight of the edge.
    """

    start: str
    end: str
    weight: int


class DisjointSet:
    """
    Implements a disjoint-set (union-find) data structure.

    This data structure is useful for tracking the partitioning of a set into disjoint,
    non-overlapping subsets. It offers efficient operations for union and finding the
    representative of a set.

    Attributes:
        parent (dict[str, str]): Maps each element to its parent element.
        rank (dict[str, int]): Maps each element to its rank in the tree.

    Methods:
        find(item): Finds the representative of the set containing 'item'.
        union(set1, set2): Merges the sets containing 'set1' and 'set2'.

    >>> disjoint_set = DisjointSet([])
    >>> disjoint_set.find("A")
    ''
    >>> disjoint_set = DisjointSet([1, 2, 3])
    >>> disjoint_set.find("D")  # "D" is not in the set
    Traceback (most recent call last):
        ...
    KeyError: "Item 'D' not found in the disjoint set"
    >>> disjoint_set = DisjointSet([1, 2, 3])
    >>> disjoint_set.find(1)
    1
    >>> disjoint_set.find(2)
    2
    >>> disjoint_set.find(3)
    3
    >>> disjoint_set.union(1, 2)
    >>> disjoint_set.find(2)
    1
    >>> ds = DisjointSet(["A", "B", "C"])
    >>> ds.find("A")
    'A'
    >>> ds.union("A", "B")
    >>> ds.find("B")
    'A'
    >>> ds.union("B", "C")
    >>> ds.find("C")
    'A'
    """

    def __init__(self, vertices: Iterable[str]) -> None:
        """Initializes the disjoint set with each vertex in its own set."""
        self.parent: dict[str, str] = {v: v for v in vertices}
        self.rank: dict[str, int] = {v: 0 for v in vertices}

    def find(self, item: str) -> str:
        """Finds the representative of the set containing 'item'."""
        if not self.parent:  # Check if the set is empty
            return ""
        if item not in self.parent:  # Check if the item is not in the set
            error_message = "Item '" + str(item) + "' not found in the disjoint set"
            raise KeyError(error_message)
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, set1: str, set2: str) -> None:
        """Merges the sets containing 'set1' and 'set2'."""
        root1, root2 = self.find(set1), self.find(set2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph: list[Edge]) -> list[Edge]:
    """
    Implements Kruskal's algorithm to find the minimum spanning tree of a graph.

    Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for
    a connected, weighted graph. It sorts the graph's edges by weight and selects them
    in ascending order, ensuring no cycles are formed.

    :param graph: a list of edges representing the graph.
    :return: a list of edges representing the minimum spanning tree of the graph.

    >>> graph = [
    ...     Edge("A", "B", 1), Edge("B", "C", 3), Edge("A", "C", 4),
    ...     Edge("A", "D", 2), Edge("D", "C", 5)
    ... ]
    >>> minimum_spanning_tree = kruskal(graph)
    >>> [(edge.start, edge.end, edge.weight) for edge in minimum_spanning_tree]
    [('A', 'B', 1), ('A', 'D', 2), ('B', 'C', 3)]
    """
    vertices: set[str] = {vertex for edge in graph for vertex in (edge.start, edge.end)}
    disjoint_set = DisjointSet(vertices)
    minimum_spanning_tree: list[Edge] = []

    for edge in sorted(graph, key=lambda edge: edge.weight):
        if disjoint_set.find(edge.start) != disjoint_set.find(edge.end):
            minimum_spanning_tree.append(edge)
            disjoint_set.union(edge.start, edge.end)

    return minimum_spanning_tree


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    graph = [
        Edge("A", "B", 1),
        Edge("B", "C", 3),
        Edge("A", "C", 4),
        Edge("A", "D", 2),
        Edge("D", "C", 5),
    ]
    minimum_spanning_tree = kruskal(graph)
    print(
        "Minimum Spanning Tree:",
        [(edge.start, edge.end, edge.weight) for edge in minimum_spanning_tree],
    )  # Minimum Spanning Tree: [('A', 'B', 1), ('A', 'D', 2), ('B', 'C', 3)]
