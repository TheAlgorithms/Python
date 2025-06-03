"""Queue represented by a Python list"""

from collections.abc import Iterable
from typing import Generic, TypeVar

_T = TypeVar("_T")


class QueueByList(Generic[_T]):
    def __init__(self, iterable: Iterable[_T] | None = None) -> None:
        """
        >>> QueueByList()
        Queue(())
        >>> QueueByList([10, 20, 30])
        Queue((10, 20, 30))
        >>> QueueByList((i**2 for i in range(1, 4)))
        Queue((1, 4, 9))
        """
        self.entries: list[_T] = list(iterable or [])

    def __len__(self) -> int:
        """
        >>> len(QueueByList())
        0
        >>> from string import ascii_lowercase
        >>> len(QueueByList(ascii_lowercase))
        26
        >>> queue = QueueByList()
        >>> for i in range(1, 11):
        ...     queue.put(i)
        >>> len(queue)
        10
        >>> for i in range(2):
        ...   queue.get()
        1
        2
        >>> len(queue)
        8
        """

        return len(self.entries)

    def __repr__(self) -> str:
        """
        >>> queue = QueueByList()
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

        return f"Queue({tuple(self.entries)})"

    def put(self, item: _T) -> None:
        """Put `item` to the Queue

        >>> queue = QueueByList()
        >>> queue.put(10)
        >>> queue.put(20)
        >>> len(queue)
        2
        >>> queue
        Queue((10, 20))
        """

        self.entries.append(item)

    def get(self) -> _T:
        """
        Get `item` from the Queue

        >>> queue = QueueByList((10, 20, 30))
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

        if not self.entries:
            raise IndexError("Queue is empty")
        return self.entries.pop(0)

    def rotate(self, rotation: int) -> None:
        """Rotate the items of the Queue `rotation` times

        >>> queue = QueueByList([10, 20, 30, 40])
        >>> queue
        Queue((10, 20, 30, 40))
        >>> queue.rotate(1)
        >>> queue
        Queue((20, 30, 40, 10))
        >>> queue.rotate(2)
        >>> queue
        Queue((40, 10, 20, 30))
        """

        put = self.entries.append
        get = self.entries.pop

        for _ in range(rotation):
            put(get(0))

    def get_front(self) -> _T:
        """Get the front item from the Queue

        >>> queue = QueueByList((10, 20, 30))
        >>> queue.get_front()
        10
        >>> queue
        Queue((10, 20, 30))
        >>> queue.get()
        10
        >>> queue.get_front()
        20
        """

        return self.entries[0]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
