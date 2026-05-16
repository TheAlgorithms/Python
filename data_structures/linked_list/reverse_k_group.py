from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next_node: Node | None = None


class LinkedList:
    def __init__(self, ints: Iterable[int]) -> None:
        self.head: Node | None = None
        for i in ints:
            self.append(i)

    def __iter__(self) -> Iterator[int]:
        """
        >>> ints = []
        >>> list(LinkedList(ints)) == ints
        True
        >>> ints = tuple(range(5))
        >>> tuple(LinkedList(ints)) == ints
        True
        """
        node = self.head
        while node:
            yield node.data
            node = node.next_node

    def __len__(self) -> int:
        """
        >>> for i in range(3):
        ...     len(LinkedList(range(i))) == i
        True
        True
        True
        >>> len(LinkedList("abcdefgh"))
        8
        """
        return sum(1 for _ in self)

    def __str__(self) -> str:
        """
        >>> str(LinkedList([]))
        ''
        >>> str(LinkedList(range(5)))
        '0 -> 1 -> 2 -> 3 -> 4'
        """
        return " -> ".join([str(node) for node in self])

    def append(self, data: int) -> None:
        """
        >>> ll = LinkedList([1, 2])
        >>> tuple(ll)
        (1, 2)
        >>> ll.append(3)
        >>> tuple(ll)
        (1, 2, 3)
        >>> ll.append(4)
        >>> tuple(ll)
        (1, 2, 3, 4)
        >>> len(ll)
        4
        """
        if not self.head:
            self.head = Node(data)
            return
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = Node(data)

    def reverse_k_nodes(self, group_size: int) -> None:
        """
        reverse nodes within groups of size k
        >>> ll = LinkedList([1, 2, 3, 4, 5])
        >>> ll.reverse_k_nodes(2)
        >>> tuple(ll)
        (2, 1, 4, 3, 5)
        >>> str(ll)
        '2 -> 1 -> 4 -> 3 -> 5'
        """
        if self.head is None or self.head.next_node is None:
            return

        length = len(self)
        dummy_head = Node(0)
        dummy_head.next_node = self.head
        previous_node = dummy_head

        while length >= group_size:
            current_node = previous_node.next_node
            assert current_node
            next_node = current_node.next_node
            for _ in range(1, group_size):
                assert next_node, current_node
                current_node.next_node = next_node.next_node
                assert previous_node
                next_node.next_node = previous_node.next_node
                previous_node.next_node = next_node
                next_node = current_node.next_node
            previous_node = current_node
            length -= group_size
        self.head = dummy_head.next_node


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ll = LinkedList([1, 2, 3, 4, 5])
    print(f"Original Linked List: {ll}")
    k = 2
    ll.reverse_k_nodes(k)
    print(f"After reversing groups of size {k}: {ll}")
