class CircularQueueLinkedList:
    def __init__(self):
        self.is_empty_queue = True
        self.elem = None

    def is_empty(self) -> bool:
        """
        >>> cq = CircularQueueLinkedList()
        >>> cq.is_empty()
        True
        >>> cq.enqueue('a')
        >>> cq.is_empty()
        False
        >>> cq.dequeue()
        'a'
        >>> cq.is_empty()
        True
        """
        return self.is_empty_queue

    def first(self):
        """
        >>> cq = CircularQueueLinkedList()
        >>> cq.first()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        >>> cq.enqueue('a')
        >>> cq.first()
        'a'
        >>> cq.dequeue()
        'a'
        >>> cq.first()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        """
        if self.elem is None:
            raise Exception("Empty Queue")

        return self.elem

    def enqueue(self, data):
        self.is_empty_queue = False
        self.elem = data

    def dequeue(self):
        """
        >>> cq = CircularQueueLinkedList()
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        >>> cq.enqueue('a')
        >>> cq.dequeue()
        'a'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        """
        if self.elem is None:
            raise Exception("Empty Queue")

        self.is_empty_queue = True
        elem = self.elem
        self.elem = None
        return elem


if __name__ == "__main__":
    import doctest

    doctest.testmod()
