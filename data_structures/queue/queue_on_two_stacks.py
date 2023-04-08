"""Queue implementation using two stacks"""

from collections.abc import Iterable
from typing import Generic, TypeVar

_T = TypeVar("_T")


class QueueByTwoStacks(Generic[_T]):
    def __init__(self, iterable: Iterable[_T] | None = None) -> None:
        """
        >>> queue1 = QueueByTwoStacks()
        >>> str(queue1)
        'Queue([])'
        >>> queue2 = QueueByTwoStacks([10, 20, 30])
        >>> str(queue2)
        'Queue([10, 20, 30])'
        >>> queue3 = QueueByTwoStacks((i**2 for i in range(1, 4)))
        >>> str(queue3)
        'Queue([1, 4, 9])'
        """

        self._stack1: list[_T] = [] if iterable is None else list(iterable)
        self._stack2: list[_T] = []

    def __len__(self) -> int:
        """
        >>> queue = QueueByTwoStacks()
        >>> for i in range(1, 11):
        ...     queue.put(i)
        ...
        >>> len(queue) == 10
        True
        >>> for i in range(2):
        ...   queue.get()
        1
        2
        >>> len(queue) == 8
        True
        """

        return len(self._stack1) + len(self._stack2)

    def __repr__(self) -> str:
        """
        >>> queue = QueueByTwoStacks()
        >>> queue
        Queue([])
        >>> str(queue)
        'Queue([])'
        >>> queue.put(10)
        >>> queue
        Queue([10])
        >>> queue.put(20)
        >>> queue.put(30)
        >>> queue
        Queue([10, 20, 30])
        """

        items = self._stack2[::-1] + self._stack1
        return f"Queue({items})"

    def put(self, item: _T) -> None:
        """
        Put `item` into the Queue

        >>> queue = QueueByTwoStacks()
        >>> queue.put(10)
        >>> queue.put(20)
        >>> len(queue) == 2
        True
        >>> str(queue)
        'Queue([10, 20])'
        """

        self._stack1.append(item)

    def get(self) -> _T:
        """
        Get `item` from the Queue

        >>> queue = QueueByTwoStacks()
        >>> for i in (10, 20, 30):
        ...     queue.put(i)
        >>> queue.get()
        10
        >>> queue.put(40)
        >>> queue.get()
        20
        >>> queue.get()
        30
        >>> len(queue) == 1
        True
        >>> queue.get()
        40
        >>> queue.get()
        Traceback (most recent call last):
            ...
        IndexError: Queue is empty
        """

        # To reduce number of attribute look-ups in `while` loop.
        stack1_pop = self._stack1.pop
        stack2_append = self._stack2.append

        if not self._stack2:
            while self._stack1:
                stack2_append(stack1_pop())

        if not self._stack2:
            raise IndexError("Queue is empty")
        return self._stack2.pop()

    def size(self) -> int:
        """
        Returns the length of the Queue

        >>> queue = QueueByTwoStacks()
        >>> queue.size()
        0
        >>> queue.put(10)
        >>> queue.put(20)
        >>> queue.size()
        2
        >>> queue.get()
        10
        >>> queue.size() == 1
        True
        """

        return len(self)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
