""" A Queue using a linked list like structure """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedQueue:
    """
    >>> queue = LinkedQueue()
    >>> queue.is_empty()
    True
    >>> queue.enqueue(5)
    >>> queue.enqueue(9)
    >>> queue.enqueue('python')
    >>> queue.is_empty();
    False
    >>> queue.dequeue()
    5
    >>> queue.enqueue('algorithms')
    >>> queue.dequeue()
    9
    >>> queue.dequeue()
    'python'
    >>> queue.dequeue()
    'algorithms'
    >>> queue.is_empty()
    True
    >>> queue.dequeue()
    Traceback (most recent call last):
        ...
    IndexError: dequeue from empty queue
    """

    def __init__(self):
        self.front = self.rear = None

    def __iter__(self):
        node = self.front
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        """
        >>> queue = LinkedQueue()
        >>> for i in range(1, 6):
        ...     queue.enqueue(i)
        >>> len(queue)
        5
        >>> for i in range(1, 6):
        ...     assert len(queue) == 6 - i
        ...     _ = queue.dequeue()
        >>> len(queue)
        0
        """
        return len(tuple(iter(self)))

    def __str__(self):
        """
        >>> queue = LinkedQueue()
        >>> for i in range(1, 4):
        ...     queue.enqueue(i)
        >>> queue.enqueue("Python")
        >>> queue.enqueue(3.14)
        >>> queue.enqueue(True)
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
        ...     queue.enqueue(i)
        >>> queue.is_empty()
        False
        """
        return len(self) == 0

    def enqueue(self, item) -> None:
        """
        >>> queue = LinkedQueue()
        >>> queue.dequeue()
        Traceback (most recent call last):
        ...
        IndexError: dequeue from empty queue
        >>> for i in range(1, 6):
        ...     queue.enqueue(i)
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

    def dequeue(self):
        """
        >>> queue = LinkedQueue()
        >>> queue.dequeue()
        Traceback (most recent call last):
        ...
        IndexError: dequeue from empty queue
        >>> queue = LinkedQueue()
        >>> for i in range(1, 6):
        ...     queue.enqueue(i)
        >>> for i in range(1, 6):
        ...     assert queue.dequeue() == i
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
        ...     queue.enqueue(i)
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