"""Queue implementation using two stacks"""

from typing import Any


class Queue:
    def __init__(self) -> None:
        self._stack1: list[Any] = []
        self._stack2: list[Any] = []

    def put(self, item: Any) -> None:
        """
        Put `item` into the Queue

        >>> queue = Queue()
        >>> queue.put(10)
        >>> queue.put(20)
        >>> len(queue) == 2
        True
        >>> str(queue)
        '<[10, 20]>'
        """

        self._stack1.append(item)

    def get(self) -> Any:
        """
        Get `item` from the Queue

        >>> queue = Queue()
        >>> for i in (10, 20, 30):
        ...     queue.put(i)
        >>> len(queue)
        3
        >>> queue.get()
        10
        >>> queue.get()
        20
        >>> len(queue) == 1
        True
        >>> queue.get()
        30
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

        >>> queue = Queue()
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

    def __str__(self) -> str:
        """
        >>> queue = Queue()
        >>> str(queue)
        '<[]>'
        >>> queue.put(10)
        >>> str(queue)
        '<[10]>'
        >>> queue.put(20)
        >>> str(queue)
        '<[10, 20]>'
        >>> queue.get()
        10
        >>> queue.put(30)
        >>> str(queue) == '<[20, 30]>'
        True
        """

        return f"<{self._stack2[::-1] + self._stack1}>"

    def __len__(self) -> int:
        """
        >>> queue = Queue()
        >>> for i in range(1, 11):
        ...     queue.put(i)
        ...
        >>> len(queue) == 10
        True
        >>> for i in range(2):
        ...   queue.get()
        ...
        1
        2
        >>> len(queue) == 8
        True
        """

        return len(self._stack1) + len(self._stack2)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
