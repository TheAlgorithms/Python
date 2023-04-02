"""Queue represented by a Python list"""

from typing import Any


class Queue:
    def __init__(self) -> None:
        self.entries: list[Any] = []

    def __str__(self) -> str:
        """
        >>> queue = Queue()
        >>> str(queue)
        '<>'
        >>> queue.put(10)
        >>> queue.put(20)
        >>> queue.put(30)
        >>> str(queue)
        '<10, 20, 30>'
        """

        return "<" + str(self.entries)[1:-1] + ">"

    def __len__(self) -> int:
        """
        >>> queue = Queue()
        >>> queue.put(10)
        >>> queue.put(20)
        >>> queue.put(30)
        >>> len(queue)
        3
        """

        return len(self.entries)

    def put(self, item: Any) -> None:
        """Put `item` to the Queue

        >>> queue = Queue()
        >>> queue.put(10)
        >>> str(queue)
        '<10>'
        >>> queue.put(20)
        >>> str(queue)
        '<10, 20>'
        >>> len(queue)
        2
        """

        self.entries.append(item)

    def get(self) -> Any:
        """Get `item` from the Queue

        >>> queue = Queue()
        >>> queue.put(10)
        >>> queue.get() == 10
        True
        >>> len(queue) == 0
        True
        >>> queue.get()
        Traceback (most recent call last):
        ...
        IndexError: Queue is empty
        """

        if not self.entries:
            raise IndexError("Queue is empty")
        return self.entries.pop(0)

    def rotate(self, rotation: int) -> None:
        """Rotate the items of the Queue `rotation` times

        >>> queue = Queue()
        >>> for i in (10, 20, 30, 40):
        ...     queue.put(i)
        ...
        >>> str(queue)
        '<10, 20, 30, 40>'
        >>> queue.rotate(1)
        >>> str(queue)
        '<20, 30, 40, 10>'
        >>> queue.rotate(2)
        >>> str(queue)
        '<40, 10, 20, 30>'
        """

        # An optimization to reduce the number of attribute look-ups in the for-loop.
        put = self.entries.append
        get = self.entries.pop

        for _ in range(rotation):
            put(get(0))

    def get_front(self) -> Any:
        """Get the front item from the Queue

        >>> queue = Queue()
        >>> for i in (10, 20, 30):
        ...     queue.put(i)
        ...
        >>> queue.get_front()
        10
        >>> len(queue) == 3
        True
        """

        return self.entries[0]

    def size(self) -> int:
        """Returns the length of the Queue

        >>> queue = Queue()
        >>> queue.put(10)
        >>> queue.size()
        1
        >>> queue.put(20)
        >>> queue.size()
        2
        >>> queue.get()
        10
        >>> queue.size() == 1
        True
        """

        return len(self.entries)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
