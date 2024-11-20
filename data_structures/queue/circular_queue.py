# Implementation of Circular Queue (using Python lists)


class CircularQueue:
    """Circular FIFO queue with a fixed capacity"""

    def __init__(self, n: int):
        self.n = n
        self.array = [None] * self.n
        self.front = 0  # index of the first element
        self.rear = 0
        self.size = 0

    def __len__(self) -> int:
        """
        >>> cq = CircularQueue(5)
        >>> len(cq)
        0
        >>> cq.enqueue("A")  # doctest: +ELLIPSIS
        <data_structures.queue.circular_queue.CircularQueue object at ...
        >>> len(cq)
        1
        """
        return self.size

    def is_empty(self) -> bool:
        """
        Checks whether the queue is empty or not
        >>> cq = CircularQueue(5)
        >>> cq.is_empty()
        True
        >>> cq.enqueue("A").is_empty()
        False
        """
        return self.size == 0

    def first(self):
        """
        Returns the first element of the queue
        >>> cq = CircularQueue(5)
        >>> cq.first()
        False
        >>> cq.enqueue("A").first()
        'A'
        """
        return False if self.is_empty() else self.array[self.front]

    def enqueue(self, data):
        """
        This function inserts an element at the end of the queue using self.rear value
        as an index.
        >>> cq = CircularQueue(5)
        >>> cq.enqueue("A")  # doctest: +ELLIPSIS
        <data_structures.queue.circular_queue.CircularQueue object at ...
        >>> (cq.size, cq.first())
        (1, 'A')
        >>> cq.enqueue("B")  # doctest: +ELLIPSIS
        <data_structures.queue.circular_queue.CircularQueue object at ...
        >>> (cq.size, cq.first())
        (2, 'A')
        """
        if self.size >= self.n:
            raise Exception("QUEUE IS FULL")

        self.array[self.rear] = data
        self.rear = (self.rear + 1) % self.n
        self.size += 1
        return self

    def dequeue(self):
        """
        This function removes an element from the queue using on self.front value as an
        index and returns it
        >>> cq = CircularQueue(5)
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: UNDERFLOW
        >>> cq.enqueue("A").enqueue("B").dequeue()
        'A'
        >>> (cq.size, cq.first())
        (1, 'B')
        >>> cq.dequeue()
        'B'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: UNDERFLOW
        """
        if self.size == 0:
            raise Exception("UNDERFLOW")

        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return temp
