from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Node | None = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        nodes = [str(item) for item in self]
        return "->".join(nodes)

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
            if node == self.head:
                break

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def insert_tail(self, data: Any) -> None:
        self.insert_nth(len(self), data)

    def insert_head(self, data: Any) -> None:
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data: Any) -> None:
        if index < 0 or index > len(self):
            raise IndexError("list index out of range.")
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.tail = self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = self.tail.next = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            if index == len(self) - 1:
                self.tail = new_node

    def delete_front(self) -> Any:
        return self.delete_nth(0)

    def delete_tail(self) -> Any:
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int = 0) -> Any:
        if not 0 <= index < len(self):
            raise IndexError("list index out of range.")
        delete_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        elif index == 0:
            self.tail.next = self.tail.next.next
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
            if index == len(self) - 1:
                self.tail = temp
        return delete_node.data

    def is_empty(self) -> bool:
        return len(self) == 0


def test_circular_linked_list() -> None:
    circular_linked_list = CircularLinkedList()
    assert len(circular_linked_list) == 0
    assert circular_linked_list.is_empty() is True
    assert repr(circular_linked_list) == ""

    try:
        circular_linked_list.delete_front()
        raise AssertionError
    except IndexError:
        assert True

    try:
        circular_linked_list.delete_tail()
        raise AssertionError
    except IndexError:
        assert True

    try:
        circular_linked_list.delete_nth(-1)
        raise AssertionError
    except IndexError:
        assert True

    try:
        circular_linked_list.delete_nth(0)
        raise AssertionError
    except IndexError:
        assert True

    assert circular_linked_list.is_empty() is True
    for i in range(5):
        assert len(circular_linked_list) == i
        circular_linked_list.insert_nth(i, i + 1)
    assert repr(circular_linked_list) == "->".join(str(i) for i in range(1, 6))

    circular_linked_list.insert_tail(6)
    assert repr(circular_linked_list) == "->".join(str(i) for i in range(1, 7))
    circular_linked_list.insert_head(0)
    assert repr(circular_linked_list) == "->".join(str(i) for i in range(7))

    assert circular_linked_list.delete_front() == 0
    assert circular_linked_list.delete_tail() == 6
    assert repr(circular_linked_list) == "->".join(str(i) for i in range(1, 6))
    assert circular_linked_list.delete_nth(2) == 3

    circular_linked_list.insert_nth(2, 3)
    assert repr(circular_linked_list) == "->".join(str(i) for i in range(1, 6))

    assert circular_linked_list.is_empty() is False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
