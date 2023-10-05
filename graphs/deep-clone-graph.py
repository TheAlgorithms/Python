"""
LeetCode 133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.
"""


class Node:
    def __init__(self, value=0, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> None | None:
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

    def create_clones(node: Node) -> None:
        if node in originals_to_clones:
            return

        originals_to_clones[node] = Node(node.value)

        for neighbor in node.neighbors:
            create_clones(neighbor)

    create_clones(node)

    def connect_clones_to_cloned_neighbors() -> None:
        for original, clone in originals_to_clones.items():
            for neighbor in original.neighbors:
                cloned_neighbor = originals_to_clones[neighbor]
                clone.neighbors.append(cloned_neighbor)

    connect_clones_to_cloned_neighbors()

    return originals_to_clones[node]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
