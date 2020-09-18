from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next_node = None

    def __iter__(self):
        node = self
        while node:
            yield node.data
            node = node.next_node

    @property
    def has_duplicate_data(self) -> bool:
        """
        >>> node1 = Node(1)
        >>> node1.next_node = Node(2)
        >>> node1.next_node.next_node = Node(3)
        >>> node1.next_node.next_node.next_node = Node(4)
        >>> node.has_duplicate_data
        False
        >>> node1.next_node.next_node.next_node = node1.next_node
        >>> node.has_duplicate_data
        True
        """
        return len(list(self)) != len(set(self))


if __name__ == "__main__":
    node1 = Node(1)
    node1.next_node = Node(2)
    node1.next_node.next_node = Node(3)
    node1.next_node.next_node.next_node = Node(4)
    node1.next_node.next_node.next_node = node1.next_node
    print(node1.has_duplicate_data)

    node2 = Node(5)
    node2.next_node = Node(6)
    node2.next_node.next_node = Node(5)
    node2.next_node.next_node.next_node = Node(6)
    print(node2.has_duplicate_data)

    node3 = Node(1)
    print(node3.has_duplicate_data)
