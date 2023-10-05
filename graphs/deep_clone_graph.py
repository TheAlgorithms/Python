"""
LeetCode 133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.
"""
from dataclasses import dataclass


@dataclass
class Node:
    value: int = 0
    neighbors: list["Node"] | None = None

    def __post_init__(self):
        self.neighbors = self.neighbors or []

    def __hash__(self):
        return id(self)


def clone_graph(node: Node | None) -> Node | None:
    """
    This function returns a clone of a connected undirected graph.
    >>> clone_graph(Node(1))
    Node(value=1, neighbors=[])
    >>> clone_graph(Node(1, [Node(2)]))
    Node(value=1, neighbors=[Node(value=2, neighbors=[])])
    >>> clone = clone_graph(None)
    >>> clone is None
    True
    """
    if not node:
        return None

    originals_to_clones = {}  # map nodes to clones

    stack = [node]

    while stack:
        original = stack.pop()

        if original in originals_to_clones:
            continue

        originals_to_clones[original] = Node(original.value)

        if not original.neighbors:
            continue

        for neighbor in original.neighbors:
            stack.append(neighbor)

    for original, clone in originals_to_clones.items():
        if not original.neighbors:
            continue

        for neighbor in original.neighbors:
            cloned_neighbor = originals_to_clones[neighbor]

            if not clone.neighbors:
                clone.neighbors = []

            clone.neighbors.append(cloned_neighbor)

    return originals_to_clones[node]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
