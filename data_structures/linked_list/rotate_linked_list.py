from collections.abc import Iterator
from typing import Any

# Definition for singly-linked list.


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class RotateLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self) -> Iterator[Any]:
        node = self.head
        while self.head:
            yield node.data
            node = node.next
            if node == self.head:
                break

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def __repr__(self):
        return "->".join(str(item) for item in iter(self))

    def is_empty(self) -> bool:
        return len(self) == 0

    def Insert(self, newValue: int) -> None:
        newNode = Node(newValue)
        if self.head == None:
            self.head = newNode
            return

        current = self.head

        while current.next != None:
            current = current.next

        current.next = newNode

    def rotateRight(self, k: int) -> None:
        if k == 0:
            return self.head

        if self.head == None:
            return None

        current = Node()
        current = self.head

        length = 1

        while current.next != None:
            current = current.next
            length += 1

        current.next = self.head
        current = self.head

        for i in range(0, length - (k % length) - 1):
            current = current.next

        self.head = current.next
        current.next = None

        return self.head


def test_rotate_linked_list() -> None:
    """
    >>> test_rotate_linked_list()
    """
    rotate_linked_list = RotateLinkedList()
    assert len(rotate_linked_list) == 0
    assert rotate_linked_list.is_empty() is True
    assert str(rotate_linked_list) == ""

    rotate_linked_list.Insert(1)
    rotate_linked_list.Insert(2)
    rotate_linked_list.Insert(3)
    rotate_linked_list.Insert(4)
    rotate_linked_list.Insert(5)
    """
    >>> str(rotate_linked_list)
    1->2->3->4->5
    """

    rotate_linked_list.rotateRight(2)
    """
    >>> str(rotate_linked_list)
    3->4->5->1->2
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
