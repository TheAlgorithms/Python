from __future__ import annotations


class Node:
    """A node in the doubly linked list."""

    def __init__(self, key: int, val: int) -> None:
        self.key, self.val = key, val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    """
    A Least Recently Used (LRU) Cache data structure.
    >>> cache = LRUCache(2)
    >>> cache.put(1, 1)
    >>> cache.put(2, 2)
    >>> cache.get(1)
    1
    >>> cache.put(3, 3)  # evicts key 2
    >>> cache.get(2)
    -1
    >>> cache.put(4, 4)  # evicts key 1
    >>> cache.get(1)
    -1
    >>> cache.get(3)
    3
    >>> cache.get(4)
    4
    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.cache: dict[int, Node] = {}  # Maps key to node

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Helper to remove a node from the list."""
        if node.prev and node.next:
            prev, nxt = node.prev, node.next
            prev.next = nxt
            nxt.prev = prev

    def _add(self, node: Node) -> None:
        """Helper to add a node to the front of the list (most recent)."""
        if self.head.next:
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Adds or updates a key-value pair in the cache.
        >>> cache = LRUCache(1)
        >>> cache.put(1, 10)
        >>> cache.get(1)
        10
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)

            if len(self.cache) > self.capacity and self.tail.prev:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
