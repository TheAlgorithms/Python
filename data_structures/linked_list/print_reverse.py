from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next_node: Node | None = None


class LinkedList:
    """A class to represent a Linked List.
    Use a tail pointer to speed up the append() operation.
    """

    def __init__(self) -> None:
        """Initialize a LinkedList with the head node set to None.
        >>> linked_list = LinkedList()
        >>> (linked_list.head, linked_list.tail)
        (None, None)
        """
        self.head: Node | None = None
        self.tail: Node | None = None  # Speeds up the append() operation

    def __iter__(self) -> Iterator[int]:
        """Iterate the LinkedList yielding each Node's data.
        >>> linked_list = LinkedList()
        >>> items = (1, 2, 3, 4, 5)
        >>> linked_list.extend(items)
        >>> tuple(linked_list) == items
        True
        """
        node = self.head
        while node:
            yield node.data
            node = node.next_node

    def __repr__(self) -> str:
        """Returns a string representation of the LinkedList.
        >>> linked_list = LinkedList()
        >>> str(linked_list)
        ''
        >>> linked_list.append(1)
        >>> str(linked_list)
        '1'
        >>> linked_list.extend([2, 3, 4, 5])
        >>> str(linked_list)
        '1 -> 2 -> 3 -> 4 -> 5'
        """
        return " -> ".join([str(data) for data in self])

    def append(self, data: int) -> None:
        """Appends a new node with the given data to the end of the LinkedList.
        >>> linked_list = LinkedList()
        >>> str(linked_list)
        ''
        >>> linked_list.append(1)
        >>> str(linked_list)
        '1'
        >>> linked_list.append(2)
        >>> str(linked_list)
        '1 -> 2'
        """
        if self.tail:
            self.tail.next_node = self.tail = Node(data)
        else:
            self.head = self.tail = Node(data)

    def extend(self, items: Iterable[int]) -> None:
        """Appends each item to the end of the LinkedList.
        >>> linked_list = LinkedList()
        >>> linked_list.extend([])
        >>> str(linked_list)
        ''
        >>> linked_list.extend([1, 2])
        >>> str(linked_list)
        '1 -> 2'
        >>> linked_list.extend([3,4])
        >>> str(linked_list)
        '1 -> 2 -> 3 -> 4'
        """
        for item in items:
            self.append(item)


def make_linked_list(elements_list: Iterable[int]) -> LinkedList:
    """Creates a Linked List from the elements of the given sequence
    (list/tuple) and returns the head of the Linked List.
    >>> make_linked_list([])
    Traceback (most recent call last):
        ...
    Exception: The Elements List is empty
    >>> make_linked_list([7])
    7
    >>> make_linked_list(['abc'])
    abc
    >>> make_linked_list([7, 25])
    7 -> 25
    """
    if not elements_list:
        raise Exception("The Elements List is empty")

    linked_list = LinkedList()
    linked_list.extend(elements_list)
    return linked_list


def in_reverse(linked_list: LinkedList) -> str:
    """Prints the elements of the given Linked List in reverse order
    >>> in_reverse(LinkedList())
    ''
    >>> in_reverse(make_linked_list([69, 88, 73]))
    '73 <- 88 <- 69'
    """
    return " <- ".join(str(line) for line in reversed(tuple(linked_list)))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    linked_list = make_linked_list((14, 52, 14, 12, 43))
    print(f"Linked List:  {linked_list}")
    print(f"Reverse List: {in_reverse(linked_list)}")
