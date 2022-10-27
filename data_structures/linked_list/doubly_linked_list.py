"""
https://en.wikipedia.org/wiki/Doubly_linked_list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_head('b')
        >>> linked_list.insert_at_head('a')
        >>> linked_list.insert_at_tail('c')
        >>> tuple(linked_list)
        ('a', 'b', 'c')
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_tail('a')
        >>> linked_list.insert_at_tail('b')
        >>> linked_list.insert_at_tail('c')
        >>> str(linked_list)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])

    def __len__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> for i in range(0, 5):
        ...     linked_list.insert_at_nth(i, i + 1)
        >>> len(linked_list) == 5
        True
        """
        return len(tuple(iter(self)))

    def insert_at_head(self, data):
        self.insert_at_nth(0, data)

    def insert_at_tail(self, data):
        self.insert_at_nth(len(self), data)

    def insert_at_nth(self, index: int, data):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_nth(-1, 666)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> linked_list.insert_at_nth(1, 666)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> linked_list.insert_at_nth(0, 2)
        >>> linked_list.insert_at_nth(0, 1)
        >>> linked_list.insert_at_nth(2, 4)
        >>> linked_list.insert_at_nth(2, 3)
        >>> str(linked_list)
        '1->2->3->4'
        >>> linked_list.insert_at_nth(5, 5)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        """
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif index == 0:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        elif index == len(self):
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            temp.previous.next = new_node
            new_node.previous = temp.previous
            new_node.next = temp
            temp.previous = new_node

    def delete_head(self):
        return self.delete_at_nth(0)

    def delete_tail(self):
        return self.delete_at_nth(len(self) - 1)

    def delete_at_nth(self, index: int):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.delete_at_nth(0)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> for i in range(0, 5):
        ...     linked_list.insert_at_nth(i, i + 1)
        >>> linked_list.delete_at_nth(0) == 1
        True
        >>> linked_list.delete_at_nth(3) == 5
        True
        >>> linked_list.delete_at_nth(1) == 3
        True
        >>> str(linked_list)
        '2->4'
        >>> linked_list.delete_at_nth(2)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        """
        if not 0 <= index <= len(self) - 1:
            raise IndexError("list index out of range")
        delete_node = self.head  # default first node
        if len(self) == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.previous = None
        elif index == len(self) - 1:
            delete_node = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            delete_node = temp
            temp.next.previous = temp.previous
            temp.previous.next = temp.next
        return delete_node.data

    def delete(self, data) -> str:
        current = self.head

        while current.data != data:  # Find the position to delete
            if current.next:
                current = current.next
            else:  # We have reached the end an no value matches
                return "No data matching given value"

        if current == self.head:
            self.delete_head()

        elif current == self.tail:
            self.delete_tail()

        else:  # Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next  # 1 --> 3
            current.next.previous = current.previous  # 1 <--> 3
        return data

    def is_empty(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.is_empty()
        True
        >>> linked_list.insert_at_tail(1)
        >>> linked_list.is_empty()
        False
        """
        return len(self) == 0


def test_doubly_linked_list() -> None:
    """
    >>> test_doubly_linked_list()
    """
    linked_list = DoublyLinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""

    try:
        linked_list.delete_head()
        raise AssertionError()  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    try:
        linked_list.delete_tail()
        raise AssertionError()  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_at_nth(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert_at_head(0)
    linked_list.insert_at_tail(11)
    assert str(linked_list) == "->".join(str(i) for i in range(0, 12))

    assert linked_list.delete_head() == 0
    assert linked_list.delete_at_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
