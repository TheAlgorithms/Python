""" A Queue using a linked list like structure """
from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Node | None = None

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedQueue:
    """
    >>> queue = LinkedQueue()
    >>> queue.is_empty()
    True
    >>> queue.put(5)
    >>> queue.put(9)
    >>> queue.put('python')
    >>> queue.is_empty();
    False
    >>> queue.get()
    5
    >>> queue.put('algorithms')
    >>> queue.get()
    9
    >>> queue.get()
    'python'
    >>> queue.get()
    'algorithms'
    >>> queue.is_empty()
    True
    >>> queue.get()
    Traceback (most recent call last):
        ...
    IndexError: dequeue from empty queue
    """

    def __init__(self) -> None:
        self.front: Node | None = None
        self.rear: Node | None = None

    def __iter__(self) -> Iterator[Any]:
        node = self.front
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        """
        >>> queue = LinkedQueue()
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> len(queue)
        5
        >>> for i in range(1, 6):
        ...     assert len(queue) == 6 - i
        ...     _ = queue.get()
        >>> len(queue)
        0
        """
        return len(tuple(iter(self)))

    def __str__(self) -> str:
        """
        >>> queue = LinkedQueue()
        >>> for i in range(1, 4):
        ...     queue.put(i)
        >>> queue.put("Python")
        >>> queue.put(3.14)
        >>> queue.put(True)
        >>> str(queue)
        '1 <- 2 <- 3 <- Python <- 3.14 <- True'
        """
        return " <- ".join(str(item) for item in self)

    def is_empty(self) -> bool:
        """
        >>> queue = LinkedQueue()
        >>> queue.is_empty()
        True
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> queue.is_empty()
        False
        """
        return len(self) == 0

    def put(self, item: Any) -> None:
        """
        >>> queue = LinkedQueue()
        >>> queue.get()
        Traceback (most recent call last):
        ...
        IndexError: dequeue from empty queue
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> str(queue)
        '1 <- 2 <- 3 <- 4 <- 5'
        """
        node = Node(item)
        if self.is_empty():
            self.front = self.rear = node
        else:
            assert isinstance(self.rear, Node)
            self.rear.next = node
            self.rear = node

    def get(self) -> Any:
        """
        >>> queue = LinkedQueue()
        >>> queue.get()
        Traceback (most recent call last):
        ...
        IndexError: dequeue from empty queue
        >>> queue = LinkedQueue()
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> for i in range(1, 6):
        ...     assert queue.get() == i
        >>> len(queue)
        0
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        assert isinstance(self.front, Node)
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return node.data

    def clear(self) -> None:
        """
        >>> queue = LinkedQueue()
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> queue.clear()
        >>> len(queue)
        0
        >>> str(queue)
        ''
        """
        self.front = self.rear = None


if __name__ == "__main__":
    from doctest import testmod

    testmod()
