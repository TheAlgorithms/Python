from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class ContainsLoopError(Exception):
    pass


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next_node: Node | None = None

    def __iter__(self) -> Iterator[Any]:
        node = self
        visited = set()
        while node:
            if node in visited:
                raise ContainsLoopError
            visited.add(node)
            yield node.data
            node = node.next_node

    @property
    def has_loop(self) -> bool:
        """
        A loop is when the exact same Node appears more than once in a linked list.
        Uses Floyd's tortoise-and-hare cycle detection, so only constant
        auxiliary space is used regardless of list length.
        https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare
        >>> root_node = Node(1)
        >>> root_node.next_node = Node(2)
        >>> root_node.next_node.next_node = Node(3)
        >>> root_node.next_node.next_node.next_node = Node(4)
        >>> root_node.has_loop
        False
        >>> root_node.next_node.next_node.next_node = root_node.next_node
        >>> root_node.has_loop
        True
        """
        slow = self
        fast = self
        while fast is not None and fast.next_node is not None:
            slow = slow.next_node if slow is not None else None
            fast = fast.next_node.next_node
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    root_node = Node(1)
    root_node.next_node = Node(2)
    root_node.next_node.next_node = Node(3)
    root_node.next_node.next_node.next_node = Node(4)
    print(root_node.has_loop)  # False
    root_node.next_node.next_node.next_node = root_node.next_node
    print(root_node.has_loop)  # True

    root_node = Node(5)
    root_node.next_node = Node(6)
    root_node.next_node.next_node = Node(5)
    root_node.next_node.next_node.next_node = Node(6)
    print(root_node.has_loop)  # False

    root_node = Node(1)
    print(root_node.has_loop)  # False

    # Self-loop: a node points to itself
    root_node = Node(1)
    root_node.next_node = root_node
    print(root_node.has_loop)  # True

    # Loop involving the final node
    root_node = Node(1)
    root_node.next_node = Node(2)
    root_node.next_node.next_node = Node(3)
    root_node.next_node.next_node.next_node = root_node.next_node.next_node
    print(root_node.has_loop)  # True

    # Duplicate data values in different nodes must not be mistaken for a loop
    root_node = Node(1)
    root_node.next_node = Node(1)
    print(root_node.has_loop)  # False
