from stack import Stack, StackOverflowError


class Queue:
    """
    A queue is an abstract data type that works on the principle of
    First In, First Out (FIFO). Its principal operations include enqueue()
    and dequeue(). enqueue() add an element to the end of the queue while
    dequeue() removes and element from the front of the queue.
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
    """

    def __init__(self, limit: int = 10) -> None:
        self.stack1 = Stack(limit)
        self.stack2 = Stack(limit)
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack1)

    def __str__(self) -> str:
        return str(self.stack1)

    def enqueue(self, data: int) -> None:
        """Add an element to the end of queue."""
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        self.stack1.push(data)

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self) -> int:
        """Remove and element from the front of queue."""
        return self.stack1.pop()

    def front(self) -> int:
        """Return the value of the element in front of the queue."""
        return self.stack1.peek()

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return not bool(self.stack1)

    def is_full(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        """Return the size of the queue."""
        return self.stack1.size()

    def __contains__(self, data: int) -> int:
        """Check if item is in the queue."""
        return data in self.stack1


def test_queue() -> None:
    """
    >>> test_queue()
    """
    queue = Queue(10)
    assert queue.is_empty() is True
    assert queue.is_full() is False
    assert bool(queue) is False
    assert str(queue) == "[]"

    try:
        queue.dequeue()
        assert False  # This should not happen
    except IndexError:
        assert True  # This should happen

    try:
        queue.front()
        assert False  # This should not happen
    except IndexError:
        assert True  # This should happen

    for i in range(10):
        assert queue.size() == i
        queue.enqueue(i)

    assert queue.is_full() is True
    assert queue.is_empty() is False
    assert bool(queue) is True
    assert str(queue) == str(list(range(10))[::-1])
    assert queue.dequeue() == 0
    assert queue.front() == 1

    queue.enqueue(100)
    assert str(queue) == str([100, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    try:
        queue.enqueue(0)
        assert False  # This should not happen
    except StackOverflowError:
        assert True  # This should happen

    assert queue.is_empty() is False
    assert queue.size() == 10

    assert 50 not in queue
    assert 100 in queue


if __name__ == "__main__":
    import doctest

    doctest.testmod()
