"""Queue represented by a pseudo stack (represented by a list with pop and append)"""


class Queue:
    def __init__(self):
        self.stack = []
        self.length = 0

    def __str__(self):
        """
        >>> q = Queue()
        >>> q.put(3)
        >>> q.put(5)
        >>> q.put(7)
        >>> print(q)
        <3, 5, 7>

        >>> q = Queue()
        >>> print(q)
        <>
        """
        printed = "<" + str(self.stack)[1:-1] + ">"
        return printed

    """Enqueues {@code item}
    @param item
        item to enqueue"""

    def put(self, item):
        """
        >>> q = Queue()
        >>> q.put(3)
        >>> assert q.stack == [3]
        >>> assert q.length == 1
        """
        self.stack.append(item)
        self.length = self.length + 1

    """Dequeues {@code item}
    @requirement: |self.length| > 0
    @return dequeued
        item that was dequeued"""

    def get(self):
        """
        Testing get() and inner call to rotate()

        >>> q = Queue()
        >>> q.put(3)
        >>> q.put(5)
        >>> q.put(7)
        >>> n = q.get()
        >>> assert n == 3
        >>> assert q.stack == [5,7]

        >>> q2 = Queue()
        >>> q2.put(3)
        >>> n = q2.get()
        >>> n = q2.get()
        Traceback (most recent call last):
        ...
        IndexError: The queue is empty

        >>> q3 = Queue()
        >>> n = q3.get()
        Traceback (most recent call last):
        ...
        IndexError: The queue is empty

        >>> q4 = Queue()
        >>> q4.put(3)
        >>> n = q4.get()
        >>> assert n == 3
        """

        self.rotate(1)
        dequeued = self.stack[self.length - 1]
        self.stack = self.stack[:-1]
        self.rotate(self.length - 1)
        self.length = self.length - 1
        return dequeued

    """Rotates the queue {@code rotation} times
    @param rotation
    @requirement: |self.length| > 0
        number of times to rotate queue"""

    def rotate(self, rotation):
        """
        >>> q = Queue()
        >>> q.put(3)
        >>> q.put(5)
        >>> q.put(7)
        >>> q.rotate(2)
        >>> assert q.stack == [7,3,5]
        """

        for i in range(rotation):
            if self.length == 0:
                raise IndexError("The queue is empty")
            temp = self.stack[0]
            self.stack = self.stack[1:]
            self.put(temp)
            self.length = self.length - 1

    """Reports item at the front of self
    @return item at front of self.stack"""

    def front(self):
        """
        >>> q = Queue()
        >>> q.put(3)
        >>> n = q.front()
        >>> assert n == 3

        >>> q2 = Queue()
        >>> n = q2.front()
        Traceback (most recent call last):
        ...
        IndexError: The queue is empty
        """
        front = self.get()
        self.put(front)
        self.rotate(self.length - 1)
        return front

    """Returns the length of this.stack"""

    def size(self):
        """
        >>> q = Queue()
        >>> q.size()
        0
        """
        return self.length


if __name__ == "__main__":
    import doctest

    doctest.testmod()
