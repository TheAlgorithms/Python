"""Queue implementation using two stacks"""

from collections.abc import Iterable
from typing import Generic, TypeVar

_T = TypeVar("_T")


class QueueByTwoStacks(Generic[_T]):
    def __init__(self, iterable: Iterable[_T] | None = None) -> None:
        """
        >>> QueueByTwoStacks()
        Queue(())
        >>> QueueByTwoStacks([10, 20, 30])
        Queue((10, 20, 30))
        >>> QueueByTwoStacks((i**2 for i in range(1, 4)))
        Queue((1, 4, 9))
        """
        self._stack1: list[_T] = list(iterable or [])
        self._stack2: list[_T] = []

    def __len__(self) -> int:
        """
        >>> len(QueueByTwoStacks())
        0
        >>> from string import ascii_lowercase
        >>> len(QueueByTwoStacks(ascii_lowercase))
        26
        >>> queue = QueueByTwoStacks()
        >>> for i in range(1, 11):
        ...     queue.put(i)
        ...
        >>> len(queue)
        10
        >>> for i in range(2):
        ...   queue.get()
        1
        2
        >>> len(queue)
        8
        """

        return len(self._stack1) + len(self._stack2)

    def __repr__(self) -> str:
        """
        >>> queue = QueueByTwoStacks()
        >>> queue
        Queue(())
        >>> str(queue)
        'Queue(())'
        >>> queue.put(10)
        >>> queue
        Queue((10,))
        >>> queue.put(20)
        >>> queue.put(30)
        >>> queue
        Queue((10, 20, 30))
        """
        return f"Queue({tuple(self._stack2[::-1] + self._stack1)})"

    def put(self, item: _T) -> None:
        """
        Put `item` into the Queue

        >>> queue = QueueByTwoStacks()
        >>> queue.put(10)
        >>> queue.put(20)
        >>> len(queue)
        2
        >>> queue
        Queue((10, 20))
        """

        self._stack1.append(item)

    def get(self) -> _T:
        """
        Get `item` from the Queue

        >>> queue = QueueByTwoStacks((10, 20, 30))
        >>> queue.get()
        10
        >>> queue.put(40)
        >>> queue.get()
        20
        >>> queue.get()
        30
        >>> len(queue)
        1
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


if __name__ == "__main__":
    from doctest import testmod

    testmod()
