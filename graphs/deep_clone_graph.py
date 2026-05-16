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

    def __post_init__(self) -> None:
        """
        >>> Node(3).neighbors
        []
        """
        self.neighbors = self.neighbors or []

    def __hash__(self) -> int:
        """
        >>> hash(Node(3)) != 0
        True
        """
        return id(self)


def clone_graph(node: Node | None) -> Node | None:
    """
    This function returns a clone of a connected undirected graph.
    >>> clone_graph(Node(1))
    Node(value=1, neighbors=[])
    >>> clone_graph(Node(1, [Node(2)]))
    Node(value=1, neighbors=[Node(value=2, neighbors=[])])
    >>> clone_graph(None) is None
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

        stack.extend(original.neighbors or [])

    for original, clone in originals_to_clones.items():
        for neighbor in original.neighbors or []:
            cloned_neighbor = originals_to_clones[neighbor]

            if not clone.neighbors:
                clone.neighbors = []

            clone.neighbors.append(cloned_neighbor)

    return originals_to_clones[node]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
