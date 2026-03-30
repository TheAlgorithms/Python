"""
Queue Implementation using Linked List (Optimized)

- Time Complexity:
    enqueue → O(1)
    dequeue → O(1)
    is_empty → O(1)
    size → O(1)

Author: Sufiyan
"""

from __future__ import annotations
from typing import Any, Iterator


class Node:
    """A node in the linked list."""

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None


class LinkedQueue:
    """Efficient Queue implementation using a linked list (FIFO)."""

    def __init__(self) -> None:
        self.front: Node | None = None
        self.rear: Node | None = None
        self._size: int = 0  # 🔥 O(1) size tracking

    def __len__(self) -> int:
        """Return number of elements in queue (O(1))."""
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """Iterate through elements."""
        current = self.front
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """String representation."""
        return " <- ".join(map(str, self))

    def is_empty(self) -> bool:
        """Check if queue is empty (O(1))."""
        return self.front is None

    # 🔥 Professional naming (industry standard)
    def enqueue(self, item: Any) -> None:
        """Add element to rear (O(1))."""
        new_node = Node(item)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self._size += 1

    def dequeue(self) -> Any:
        """Remove element from front (O(1))."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        assert self.front is not None
        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self._size -= 1
        return temp.data

    def peek(self) -> Any:
        """Return front element without removing."""
        if self.is_empty():
            raise IndexError("peek from empty queue")

        assert self.front is not None
        return self.front.data

    def clear(self) -> None:
        """Remove all elements."""
        self.front = self.rear = None
        self._size = 0


if __name__ == "__main__":
    q = LinkedQueue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue:", q)
    print("Front:", q.peek())
    print("Dequeued:", q.dequeue())
    print("Queue after dequeue:", q)
