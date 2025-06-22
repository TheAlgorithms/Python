from __future__ import annotations

from collections.abc import Callable, Hashable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


class DoubleLinkedListNode:
    """Node for LRU Cache"""

    __slots__ = ("key", "val", "next", "prev")

    def __init__(self, key: Any, val: Any) -> None:
        self.key = key
        self.val = val
        self.next: DoubleLinkedListNode | None = None
        self.prev: DoubleLinkedListNode | None = None

    def __repr__(self) -> str:
        return f"Node(key={self.key}, val={self.val})"


class DoubleLinkedList:
    """Double Linked List for LRU Cache"""

    def __init__(self) -> None:
        # Create sentinel nodes
        self.head = DoubleLinkedListNode(None, None)
        self.rear = DoubleLinkedListNode(None, None)
        # Link sentinel nodes together
        self.head.next = self.rear
        self.rear.prev = self.head

    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return f"LinkedList({nodes})"

    def add(self, node: DoubleLinkedListNode) -> None:
        """Add node before rear"""
        prev = self.rear.prev
        if prev is None:
            return

        # Insert node between prev and rear
        prev.next = node
        node.prev = prev
        self.rear.prev = node
        node.next = self.rear

    def remove(self, node: DoubleLinkedListNode) -> DoubleLinkedListNode | None:
        """Remove node from list"""
        if node.prev is None or node.next is None:
            return None

        # Bypass node
        node.prev.next = node.next
        node.next.prev = node.prev

        # Clear node references
        node.prev = None
        node.next = None
        return node


class LRUCache:
    """LRU Cache implementation"""

    def __init__(self, capacity: int) -> None:
        self.list = DoubleLinkedList()
        self.capacity = capacity
        self.size = 0
        self.hits = 0
        self.misses = 0
        self.cache: dict[Any, DoubleLinkedListNode] = {}

    def __repr__(self) -> str:
        return (
            f"Cache(hits={self.hits}, misses={self.misses}, "
            f"cap={self.capacity}, size={self.size})"
        )

    def get(self, key: Any) -> Any | None:
        """Get value for key"""
        if key in self.cache:
            self.hits += 1
            node = self.cache[key]
            if self.list.remove(node):
                self.list.add(node)
            return node.val
        self.misses += 1
        return None

    def put(self, key: Any, value: Any) -> None:
        """Set value for key"""
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            if self.list.remove(node):
                node.val = value
                self.list.add(node)
            return

        # Evict LRU item if at capacity
        if self.size >= self.capacity:
            first_node = self.list.head.next
            if first_node and first_node.key and first_node != self.list.rear:
                if self.list.remove(first_node):
                    del self.cache[first_node.key]
                    self.size -= 1

        # Add new node
        new_node = DoubleLinkedListNode(key, value)
        self.cache[key] = new_node
        self.list.add(new_node)
        self.size += 1

    def cache_info(self) -> dict[str, Any]:
        """Get cache statistics"""
        return {
            "hits": self.hits,
            "misses": self.misses,
            "capacity": self.capacity,
            "size": self.size,
        }


def lru_cache(maxsize: int = 128) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """LRU Cache decorator"""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache = LRUCache(maxsize)

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Create normalized cache key
            key = (args, tuple(sorted(kwargs.items())))

            # Try to get cached result
            if (cached := cache.get(key)) is not None:
                return cached

            # Compute and cache result
            result = func(*args, **kwargs)
            cache.put(key, result)
            return result

        # Attach cache info method
        wrapper.cache_info = cache.cache_info  # type: ignore[attr-defined]
        return wrapper

    return decorator


if __name__ == "__main__":
    import doctest

    doctest.testmod()
