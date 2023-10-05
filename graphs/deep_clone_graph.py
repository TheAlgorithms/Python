"""
LeetCode 133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.
"""


class Node:
    def __init__(self, value: int = 0, neighbors: list | None = None) -> None:
        self.value = value
        self.neighbors = neighbors or []

    def __repr__(self):
        return f"Node({self.value}, {self.neighbors})"


def clone_graph(node: Node | None) -> Node | None:
    """
    This function returns a clone of a connected undirected graph.
    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> node3 = Node(3)
    >>> node4 = Node(4)
    >>> node1.neighbors = [node2, node4]
    >>> node2.neighbors = [node1, node3]
    >>> node3.neighbors = [node2, node4]
    >>> node4.neighbors = [node1, node3]
    >>> clone1 = clone_graph(node1)
    >>> clone1.value
    1
    >>> clone2 = clone1.neighbors[0]
    >>> clone2.value
    2
    >>> clone4 = clone1.neighbors[1]
    >>> clone4.value
    4
    >>> clone3 = clone2.neighbors[1]
    >>> clone3.value
    3
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

        for neighbor in original.neighbors:
            stack.append(neighbor)

    for original, clone in originals_to_clones.items():
        for neighbor in original.neighbors:
            cloned_neighbor = originals_to_clones[neighbor]
            clone.neighbors.append(cloned_neighbor)

    return originals_to_clones[node]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
