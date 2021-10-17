class CircularQueueLinkedList:
    def is_empty(self) -> bool:
        """
        >>> cq = CircularQueueLinkedList()
        >>> cq.is_empty()
        True
        """
        return True

    def first(self):
        """
        >>> cq = CircularQueueLinkedList()
        >>> cq.first()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        """
        raise Exception("Empty Queue")

    def enqueue(self, data):
        pass

    def dequeue(self):
        """
        >>> cq = CircularQueueLinkedList()
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        """

        raise Exception("Empty Queue")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
