"""
Disjoint Set (Union-Find) Data Structure.
Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""

class Node:
    """
    Node class representing elements of a disjoint set.
    Each node has data, a rank, and a parent pointer.
    """

    def __init__(self, data: int) -> None:
        self.data = data  # The value of the node
        self.rank: int = 0  # Rank helps optimize union operations
        self.parent: Node = self  # Initially, each node is its own parent


def make_set(x: Node) -> None:
    """
    Initializes the node as a separate set.
    The node becomes its own parent with rank 0.
    """
    x.rank = 0
    x.parent = x  # Parent points to itself


def union_set(x: Node, y: Node) -> None:
    """
    Unites two sets containing nodes x and y.
    The root with the higher rank becomes the parent of the other.
    """
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:  # Only union if they are in different sets
        if root_x.rank > root_y.rank:
            root_y.parent = root_x
        elif root_x.rank < root_y.rank:
            root_x.parent = root_y
        else:
            root_y.parent = root_x
            root_x.rank += 1  # Increase the rank if both have the same rank


def find_set(x: Node) -> Node:
    """
    Finds the representative of the set containing x.
    Uses path compression to optimize future lookups.
    """
    if x != x.parent:
        x.parent = find_set(x.parent)  # Path compression step
    return x.parent


def find_python_set(node: Node) -> set:
    """
    Simulates finding a set in Python's built-in set collections.
    Example usage only for testing logic consistency.
    """
    sets = ({0, 1, 2}, {3, 4, 5})
    for s in sets:
        if node.data in s:
            return s
    raise ValueError(f"{node.data} is not in {sets}")


def test_disjoint_set() -> None:
    """
    Test function to verify the correctness of the disjoint set operations.

    >>> test_disjoint_set()
    """
    # Create nodes for elements 0 to 5
    vertices = [Node(i) for i in range(6)]
    for v in vertices:
        make_set(v)  # Initialize each node as its own set

    # Perform unions to create two disjoint sets: {0, 1, 2} and {3, 4, 5}
    union_set(vertices[0], vertices[1])
    union_set(vertices[1], vertices[2])
    union_set(vertices[3], vertices[4])
    union_set(vertices[4], vertices[5])

    # Verify the correctness of the unions
    for node0 in vertices:
        for node1 in vertices:
            if find_python_set(node0).isdisjoint(find_python_set(node1)):
                assert find_set(node0) != find_set(node1)
            else:
                assert find_set(node0) == find_set(node1)


if __name__ == "__main__":
    test_disjoint_set()
