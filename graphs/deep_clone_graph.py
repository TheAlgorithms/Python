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


def clone_graph(node: Node | None) -> Node | None:
    """
    This function returns a clone of a connected undirected graph.
    >>> clone_graph(Node(1))
    Node(1)
    >>> clone_graph(Node(1, [Node(2)]))
    Node(1, [Node(2)])
    >>> clone_graph(None)
    None
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
