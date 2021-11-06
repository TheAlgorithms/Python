"""Queue represented by a Python list"""

from typing import TypeVar, NoReturn, Union

T = TypeVar("T")


class Queue:
    """
    >>> queue = Queue()
    >>> queue.peek()
    Traceback (most recent call last):
    ...
    IndexError: The queue is empty
    >>> queue.size == 0
    True
    >>> queue.is_empty()
    True
    >>> queue.enqueue(2)
    >>> queue.peek()
    2
    >>> for i in range(3, 10):
    ...     queue.enqueue(i)
    >>> queue.dequeue()
    2
    >>> queue.dequeue()
    3
    >>> queue.rotate(2)
    >>> queue.dequeue()
    6
    """

    def __init__(self) -> None:
        self._queue: list[T] = []

    def __repr__(self) -> str:
        return f"{self._queue}"

    def enqueue(self, item: T) -> None:
        """Add an item to the queue"""
        self._queue.append(item)

    def dequeue(self) -> Union[T, NoReturn]:
        """Remove and return the first item in the queue.

        :raises IndexError if queue is empty
        """

        if not self.is_empty():
            return self._queue.pop(0)

        raise IndexError("The queue is empty")

    def peek(self) -> Union[T, NoReturn]:
        """
        Return the first item in the queue without removing it from the queue

        :return: First item in the queue.
        :raises IndexError if queue is empty
        """

        if not self.is_empty():
            return self._queue[0]

        raise IndexError("The queue is empty")

    @property
    def size(self) -> int:
        return len(self._queue)

    def is_empty(self) -> bool:
        return self.size == 0

    def rotate(self, number_of_rotations: int) -> None:
        """Rotate a queue by `number_of_rotation` times"""
        for _ in range(number_of_rotations):
            self.enqueue(self.dequeue())
