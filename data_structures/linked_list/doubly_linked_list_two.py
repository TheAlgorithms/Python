"""
- A linked list is similar to an array, it holds values. However, links in a linked
    list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous
    pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - It can be traversed in both forward and backward direction.
     Delete operation is more efficient
"""

from dataclasses import dataclass
from typing import Self, TypeVar

DataType = TypeVar("DataType")


@dataclass
class Node[DataType]:
    data: DataType
    previous: Self | None = None
    next: Self | None = None

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            value = self.current.data
            self.current = self.current.next
            return value


@dataclass
class LinkedList:
    head: Node | None = None  # First node in list
    tail: Node | None = None  # Last node in list

    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.data)
            current = current.next
        return " ".join(str(node) for node in nodes)

    def __contains__(self, value: DataType):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def __iter__(self):
        return LinkedListIterator(self.head)

    def get_head_data(self):
        if self.head:
            return self.head.data
        return None

    def get_tail_data(self):
        if self.tail:
            return self.tail.data
        return None

    def set_head(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insert_before_node(self.head, node)

    def set_tail(self, node: Node) -> None:
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.insert_after_node(self.tail, node)

    def insert(self, value: DataType) -> None:
        node = Node(value)
        if self.head is None:
            self.set_head(node)
        else:
            self.set_tail(node)

    def insert_before_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.next = node
        node_to_insert.previous = node.previous

        if node.previous is None:
            self.head = node_to_insert
        else:
            node.previous.next = node_to_insert

        node.previous = node_to_insert

    def insert_after_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.previous = node
        node_to_insert.next = node.next

        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.previous = node_to_insert

        node.next = node_to_insert

    def insert_at_position(self, position: int, value: DataType) -> None:
        current_position = 1
        new_node = Node(value)
        node = self.head
        while node:
            if current_position == position:
                self.insert_before_node(node, new_node)
                return
            current_position += 1
            node = node.next
        self.set_tail(new_node)

    def get_node(self, item: DataType) -> Node:
        node = self.head
        while node:
            if node.data == item:
                return node
            node = node.next
        raise Exception("Node not found")

    def delete_value(self, value):
        if (node := self.get_node(value)) is not None:
            if node == self.head:
                self.head = self.head.next

            if node == self.tail:
                self.tail = self.tail.previous

            self.remove_node_pointers(node)

    @staticmethod
    def remove_node_pointers(node: Node) -> None:
        if node.next:
            node.next.previous = node.previous

        if node.previous:
            node.previous.next = node.next

        node.next = None
        node.previous = None

    def is_empty(self):
        return self.head is None


def create_linked_list() -> None:
    """
    >>> new_linked_list = LinkedList()
    >>> new_linked_list.get_head_data() is None
    True
    >>> new_linked_list.get_tail_data() is None
    True
    >>> new_linked_list.is_empty()
    True
    >>> new_linked_list.insert(10)
    >>> new_linked_list.get_head_data()
    10
    >>> new_linked_list.get_tail_data()
    10
    >>> new_linked_list.insert_at_position(position=3, value=20)
    >>> new_linked_list.get_head_data()
    10
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.set_head(Node(1000))
    >>> new_linked_list.get_head_data()
    1000
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.set_tail(Node(2000))
    >>> new_linked_list.get_head_data()
    1000
    >>> new_linked_list.get_tail_data()
    2000
    >>> for value in new_linked_list:
    ...    print(value)
    1000
    10
    20
    2000
    >>> new_linked_list.is_empty()
    False
    >>> for value in new_linked_list:
    ...    print(value)
    1000
    10
    20
    2000
    >>> 10 in new_linked_list
    True
    >>> new_linked_list.delete_value(value=10)
    >>> 10 in new_linked_list
    False
    >>> new_linked_list.delete_value(value=2000)
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.delete_value(value=1000)
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.get_head_data()
    20
    >>> for value in new_linked_list:
    ...    print(value)
    20
    >>> new_linked_list.delete_value(value=20)
    >>> for value in new_linked_list:
    ...    print(value)
    >>> for value in range(1,10):
    ...    new_linked_list.insert(value=value)
    >>> for value in new_linked_list:
    ...    print(value)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>> linked_list = LinkedList()
    >>> linked_list.insert_at_position(position=1, value=10)
    >>> str(linked_list)
    '10'
    >>> linked_list.insert_at_position(position=2, value=20)
    >>> str(linked_list)
    '10 20'
    >>> linked_list.insert_at_position(position=1, value=30)
    >>> str(linked_list)
    '30 10 20'
    >>> linked_list.insert_at_position(position=3, value=40)
    >>> str(linked_list)
    '30 10 40 20'
    >>> linked_list.insert_at_position(position=5, value=50)
    >>> str(linked_list)
    '30 10 40 20 50'
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
