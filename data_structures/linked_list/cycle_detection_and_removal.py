from __future__ import annotations

from typing import Any
import doctest


class ContainsLoopError(Exception):
    pass


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next_node: Node | None = None

    def __iter__(self):
        node = self
        visited = []
        while node:
            if node in visited:
                raise ContainsLoopError
            visited.append(node)
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
        """
        try:
            list(self)
            return False
        except ContainsLoopError:
            return True

    def remove_loop(self) -> None:
        """
        Removes the loop in the linked list if one exists.

        >>> root_node = Node(1)
        >>> root_node.next_node = Node(2)
        >>> root_node.next_node.next_node = Node(3)
        >>> root_node.next_node.next_node.next_node = Node(4)
        >>> root_node.remove_loop()
        >>> root_node.has_loop
        False

        >>> root_node = Node(1)
        >>> root_node.next_node = Node(2)
        >>> root_node.next_node.next_node = Node(3)
        >>> root_node.next_node.next_node.next_node = Node(4)
        >>> root_node.next_node.next_node.next_node = root_node.next_node
        >>> root_node.remove_loop()
        >>> root_node.has_loop
        False

        >>> root_node = Node(5)
        >>> root_node.next_node = Node(6)
        >>> root_node.next_node.next_node = Node(5)
        >>> root_node.next_node.next_node.next_node = Node(6)
        >>> root_node.remove_loop()
        >>> root_node.has_loop
        False
        """
        if self.has_loop:
            slow_ptr = self
            fast_ptr = self
            while slow_ptr and fast_ptr and fast_ptr.next_node:
                slow_ptr = slow_ptr.next_node
                fast_ptr = fast_ptr.next_node.next_node
                if slow_ptr == fast_ptr:
                    break

            # Move one pointer to the head of the linked list
            slow_ptr = self
            while slow_ptr.next_node != fast_ptr.next_node:
                slow_ptr = slow_ptr.next_node
                fast_ptr = fast_ptr.next_node

            # Remove the loop
            fast_ptr.next_node = None


if __name__ == "__main__":
    doctest.testmod()
    root_node = Node(1)
    root_node.next_node = Node(2)
    root_node.next_node.next_node = Node(3)
    root_node.next_node.next_node.next_node = Node(4)
    print(root_node.has_loop)  # False
    root_node.next_node.next_node.next_node = root_node.next_node
    print(root_node.has_loop)  # True

    # Remove the loop
    root_node.remove_loop()
    print(root_node.has_loop)  # False

    root_node = Node(5)
    root_node.next_node = Node(6)
    root_node.next_node.next_node = Node(5)
    root_node.next_node.next_node.next_node = Node(6)
    print(root_node.has_loop)  # False

    # Remove the loop
    root_node.remove_loop()
    print(root_node.has_loop)  # False

    root_node = Node(1)
    print(root_node.has_loop)  # False
