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
        >>> root_node = Node(1)
        >>> root_node.next_node = Node(2)
        >>> root_node.next_node.next_node = Node(3)
        >>> root_node.next_node.next_node.next_node = Node(4)
        >>> root_node.has_loop
        False
        >>> root_node.next_node.next_node.next_node = root_node.next_node
        >>> root_node.has_loop
        True
        >>> single_node = Node(1)
        >>> single_node.next_node = single_node
        >>> single_node.has_loop
        True
        >>> loop_to_root = Node(1)
        >>> loop_to_root.next_node = Node(2)
        >>> loop_to_root.next_node.next_node = loop_to_root
        >>> loop_to_root.has_loop
        True
        >>> dup_node = Node(5)
        >>> dup_node.next_node = Node(5)
        >>> dup_node.has_loop
        False
        """
        slow: Node | None = self
        fast: Node | None = self
        while fast and fast.next_node and slow:
            slow = slow.next_node
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

    root_node.next_node = root_node
    print(root_node.has_loop)  # True
