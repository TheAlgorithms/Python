"""
Linked Lists consists of Nodes.
Nodes contain data and also may link to other nodes:
    - Head Node: First node, the address of the
                 head node gives us access of the complete list
    - Last node: points to null
"""
from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, item: Any, next: Any) -> None:  # noqa: A002
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size = 0

    def add(self, item: Any) -> None:
        self.head = Node(item, self.head)
        self.size += 1

    def add_at_position(self, item: Any, position: int) -> bool:
        """
        Adds a new node with the given item at the specified position in the linked list

        Args:
            item (Any): The item to be added to the linked list.
            position (int): The position at which the item should be inserted.

        Returns:
            bool: True if the insertion was successful, False otherwise.

        >>> linked_list = LinkedList()
        >>> linked_list.add(1)
        >>> linked_list.add(2)
        >>> linked_list.add(3)
        >>> linked_list.add_at_position(10, 1)
        True

        """
        if position < 0:
            return False

        current = self.head
        counter = 0
        while current and counter < position:
            current = current.next
            counter += 1

        if current:  # Check if current is not None
            new_node = Node(item, current.next)
            current.next = new_node
            return True
        else:
            return False

    def remove(self) -> Any:
        # Switched 'self.is_empty()' to 'self.head is None'
        # because mypy was considering the possibility that 'self.head'
        # can be None in below else part and giving error
        if self.head is None:
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item

    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        """
        >>> linked_list = LinkedList()
        >>> linked_list.add(23)
        >>> linked_list.add(14)
        >>> linked_list.add(9)
        >>> print(linked_list)
        9 --> 14 --> 23
        """
        if self.is_empty():
            return ""
        else:
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
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        1
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        0
        """
        return self.size
