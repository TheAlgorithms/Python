from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    """
    A node in a circular doubly linked list.
    """

    data: Any
    next_node: Node | None = None
    prev_node: Node | None = None


@dataclass
class CircularDoublyLinkedList:
    """
    A circular doubly linked list implementation.
    In a circular doubly linked list:
    - Each node has references to both next and previous nodes
    - The last node's next points to the first node
    - The first node's previous points to the last node
    """

    head: Node | None = None  # Reference to the head (first node)
    tail: Node | None = None  # Reference to the tail (last node)

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate through all nodes in the Circular Doubly Linked List yielding their
        data.
        Yields:
            The data of each node in the linked list.
        """
        if self.head is None:
            return

        node = self.head
        while True:
            yield node.data
            assert node.next_node is not None
            node = node.next_node
            if node == self.head:
                break

    def __len__(self) -> int:
        """
        Get the length (number of nodes) in the Circular Doubly Linked List.
        """
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        """
        Generate a string representation of the Circular Doubly Linked List.
        Returns:
            A string of the format "1<->2<->.....<->N".
        """
        return "<->".join(str(item) for item in iter(self))

    def insert_tail(self, data: Any) -> None:
        """
        Insert a node with the given data at the end of the Circular Doubly Linked List.
        """
        self.insert_nth(len(self), data)

    def insert_head(self, data: Any) -> None:
        """
        Insert a node with the given data at the beginning of the Circular Doubly
        Linked List.
        """
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data: Any) -> None:
        """
        Insert the data of the node at the nth position in the Circular Doubly
        Linked List.
        Args:
            index: The index at which the data should be inserted.
            data: The data to be inserted.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index > len(self):
            raise IndexError("list index out of range.")

        new_node: Node = Node(data)

        if self.head is None:
            # First node - points to itself in both directions
            new_node.next_node = new_node
            new_node.prev_node = new_node
            self.head = self.tail = new_node
        elif index == 0:
            # Insert at the head
            assert self.tail is not None
            new_node.next_node = self.head
            new_node.prev_node = self.tail
            self.head.prev_node = new_node
            self.tail.next_node = new_node
            self.head = new_node
        elif index == len(self):
            # Insert at the tail
            assert self.tail is not None
            new_node.next_node = self.head
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.head.prev_node = new_node
            self.tail = new_node
        else:
            # Find the position to insert
            temp: Node | None = self.head
            for _ in range(index):
                assert temp is not None
                temp = temp.next_node

            assert temp is not None
            # Insert before temp
            prev_node = temp.prev_node
            assert prev_node is not None

            new_node.next_node = temp
            new_node.prev_node = prev_node
            temp.prev_node = new_node
            prev_node.next_node = new_node

    def delete_front(self) -> Any:
        """
        Delete and return the data of the node at the front of the Circular Doubly
        Linked List.
        Raises:
            IndexError: If the list is empty.
        """
        return self.delete_nth(0)

    def delete_tail(self) -> Any:
        """
        Delete and return the data of the node at the end of the Circular Doubly
        Linked List.
        Returns:
            Any: The data of the deleted node.
        Raises:
            IndexError: If the list is empty.
        """
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int = 0) -> Any:
        """
        Delete and return the data of the node at the nth position in Circular
        Doubly Linked List.
        Args:
            index (int): The index of the node to be deleted. Defaults to 0.
        Returns:
            Any: The data of the deleted node.
        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < len(self):
            raise IndexError("list index out of range.")

        assert self.head is not None
        assert self.tail is not None

        if self.head == self.tail:
            # Only one node
            delete_node = self.head
            self.head = self.tail = None
        elif index == 0:
            # Delete head node
            delete_node = self.head
            self.head = self.head.next_node
            assert self.head is not None
            self.head.prev_node = self.tail
            self.tail.next_node = self.head
        else:
            # Find the node to delete
            delete_node = self.head
            for _ in range(index):
                assert delete_node is not None
                assert delete_node.next_node is not None
                delete_node = delete_node.next_node

            assert delete_node is not None
            prev_node = delete_node.prev_node
            next_node = delete_node.next_node

            assert prev_node is not None
            assert next_node is not None

            prev_node.next_node = next_node
            next_node.prev_node = prev_node

            if delete_node == self.tail:
                self.tail = prev_node

        return delete_node.data

    def is_empty(self) -> bool:
        """
        Check if the Circular Doubly Linked List is empty.
        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head is None

    def traverse_forward(self) -> list[Any]:
        """
        Traverse the list in forward direction and return all elements.
        Returns:
            list: A list containing all elements in forward order.
        """
        return list(self)

    def traverse_backward(self) -> list[Any]:
        """
        Traverse the list in backward direction and return all elements.
        Returns:
            list: A list containing all elements in backward order.
        """
        if self.tail is None:
            return []

        result = []
        node = self.tail
        while True:
            result.append(node.data)
            assert node.prev_node is not None
            node = node.prev_node
            if node == self.tail:
                break
        return result


def test_circular_doubly_linked_list() -> None:
    """
    Test cases for the CircularDoublyLinkedList class.
    >>> test_circular_doubly_linked_list()
    """
    circular_doubly_linked_list = CircularDoublyLinkedList()
    assert len(circular_doubly_linked_list) == 0
    assert circular_doubly_linked_list.is_empty() is True
    assert str(circular_doubly_linked_list) == ""

    # Test error cases on empty list
    try:
        circular_doubly_linked_list.delete_front()
        raise AssertionError  # This should not happen
    except IndexError:
        assert True  # This should happen

    try:
        circular_doubly_linked_list.delete_tail()
        raise AssertionError  # This should not happen
    except IndexError:
        assert True  # This should happen

    try:
        circular_doubly_linked_list.delete_nth(-1)
        raise AssertionError
    except IndexError:
        assert True

    try:
        circular_doubly_linked_list.delete_nth(0)
        raise AssertionError
    except IndexError:
        assert True

    # Test insertions
    assert circular_doubly_linked_list.is_empty() is True
    for i in range(5):
        assert len(circular_doubly_linked_list) == i
        circular_doubly_linked_list.insert_nth(i, i + 1)
    assert str(circular_doubly_linked_list) == "<->".join(str(i) for i in range(1, 6))

    # Test tail and head insertions
    circular_doubly_linked_list.insert_tail(6)
    assert str(circular_doubly_linked_list) == "<->".join(str(i) for i in range(1, 7))
    circular_doubly_linked_list.insert_head(0)
    assert str(circular_doubly_linked_list) == "<->".join(str(i) for i in range(7))

    # Test deletions
    assert circular_doubly_linked_list.delete_front() == 0
    assert circular_doubly_linked_list.delete_tail() == 6
    assert str(circular_doubly_linked_list) == "<->".join(str(i) for i in range(1, 6))
    assert circular_doubly_linked_list.delete_nth(2) == 3

    # Test re-insertion
    circular_doubly_linked_list.insert_nth(2, 3)
    assert str(circular_doubly_linked_list) == "<->".join(str(i) for i in range(1, 6))

    assert circular_doubly_linked_list.is_empty() is False

    # Test bidirectional traversal
    forward = circular_doubly_linked_list.traverse_forward()
    backward = circular_doubly_linked_list.traverse_backward()
    assert forward == [1, 2, 3, 4, 5]
    assert backward == [5, 4, 3, 2, 1]

    # Test circular property
    if circular_doubly_linked_list.head and circular_doubly_linked_list.tail:
        assert (
            circular_doubly_linked_list.head.prev_node
            == circular_doubly_linked_list.tail
        )
        assert (
            circular_doubly_linked_list.tail.next_node
            == circular_doubly_linked_list.head
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_circular_doubly_linked_list()
    print("All tests passed!")
