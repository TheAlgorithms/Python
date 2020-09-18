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
        >>> root_node = Node(1)
        >>> root_node.next_node = Node(2)
        >>> root_node.next_node.next_node = Node(3)
        >>> root_node.next_node.next_node.next_node = Node(4)
        >>> root_node.has_duplicate_data
        False
        >>> root_node.next_node.next_node.next_node = root_node.next_node
        >>> root_node.has_duplicate_data
        True
        """
        return len(list(self)) != len(set(self))


if __name__ == "__main__":
    root_node = Node(1)
    root_node.next_node = Node(2)
    root_node.next_node.next_node = Node(3)
    root_node.next_node.next_node.next_node = Node(4)
    print(root_node.has_duplicate_data)  # False
    root_node.next_node.next_node.next_node = root_node.next_node
    print(root_node.has_duplicate_data)  # True

    root_node = Node(5)
    root_node.next_node = Node(6)
    root_node.next_node.next_node = Node(5)
    root_node.next_node.next_node.next_node = Node(6)
    print(root_node.has_duplicate_data)  # True

    root_node = Node(1)
    print(root_node.has_duplicate_data)  # False
