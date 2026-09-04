from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    item: Any
    next: Node | Any = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size = 0

    def __str__(self) -> str:
        """
        >>> linked_list = LinkedList()
        >>> linked_list.add(23)
        >>> linked_list.add(14)
        >>> linked_list.add(9)
        >>> print(linked_list)
        9 --> 14 --> 23
        """
        iterate = self.head
        item_str = ""
        item_list: list[str] = []
        while iterate:
            item_list.append(str(iterate.item))
            iterate = iterate.next

        item_str = " --> ".join(item_list)

        return item_str

    def __len__(self) -> int:
        """
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.add("a")
        >>> len(linked_list)
        1
        >>> linked_list.add("b")
        >>> len(linked_list)
        2
        """
        return self.size

    def add(self, item: Any, position: int = 0) -> None:
        """
        Add an item to the LinkedList at the specified position.
        Default position is 0 (the head).

        Args:
            item (Any): The item to add to the LinkedList.
            position (int, optional): The position at which to add the item.
                Defaults to 0.

        Raises:
            ValueError: If the position is negative or out of bounds.

        >>> linked_list = LinkedList()
        >>> linked_list.add(1)
        >>> linked_list.add(2)
        >>> linked_list.add(3)
        >>> linked_list.add(4, 2)
        >>> print(linked_list)
        3 --> 2 --> 4 --> 1

        # Test adding to a negative position
        >>> linked_list.add(5, -3)
        Traceback (most recent call last):
            ...
        ValueError: Position must be non-negative

        # Test adding to an out-of-bounds position
        >>> linked_list.add(5,7)
        Traceback (most recent call last):
            ...
        ValueError: Out of bounds
        >>> linked_list.add(5, 4)
        >>> print(linked_list)
        3 --> 2 --> 4 --> 1 --> 5
        """
        if position < 0:
            raise ValueError("Position must be non-negative")

        if position == 0 or self.head is None:
            new_node = Node(item, self.head)
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
                if current is None:
                    raise ValueError("Out of bounds")
            new_node = Node(item, current.next)
            current.next = new_node
        self.size += 1

    def kth_element_from_end(self, position: int) -> Any:
        """
        Find the kth node element from the end of the Linked List.
        This is not a zero-based index search.
        If position=1, it will return the last element in the list.

        >>> linked_list = LinkedList()
        >>> linked_list.add(1)
        >>> linked_list.add(2)
        >>> linked_list.add(3)
        >>> linked_list.add(4, 2)
        >>> linked_list.add(5, 4)
        >>> print(linked_list)
        3 --> 2 --> 4 --> 1 --> 5
        >>> linked_list.kth_element_from_end(2)
        1
        >>> linked_list.kth_element_from_end(5)
        3
        >>> linked_list.kth_element_from_end(3)
        4
        >>> linked_list.kth_element_from_end(10)
        >>> linked_list.kth_element_from_end(0)
        >>> linked_list.kth_element_from_end(-5)
        """
        if (self.head is None) or (position <= 0) or (position > self.size):
            return None

        slow_pointer = fast_pointer = self.head

        for _ in range(position):
            fast_pointer = fast_pointer.next

        while fast_pointer is not None and slow_pointer is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        return slow_pointer.item
