from __future__ import annotations

from collections.abc import Callable, Hashable
from functools import wraps
from typing import Any, Generic, ParamSpec, TypeVar, cast

P = ParamSpec("P")
R = TypeVar("R")


class DoubleLinkedListNode:
    """Node for LRU Cache"""

    def __init__(self, key: Any | None, val: Any | None) -> None:
        self.key = key
        self.val = val
        self.next: DoubleLinkedListNode | None = None
        self.prev: DoubleLinkedListNode | None = None

    def __repr__(self) -> str:
        return f"Node(key={self.key}, val={self.val})"


class DoubleLinkedList:
    """Double Linked List for LRU Cache"""

    def __init__(self) -> None:
        self.head = DoubleLinkedListNode(None, None)
        self.rear = DoubleLinkedListNode(None, None)
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
        """Add node to list end"""
        prev = self.rear.prev
        if prev is None:
            raise ValueError("Invalid list state")
        
        prev.next = node
        node.prev = prev
        self.rear.prev = node
        node.next = self.rear

    def remove(self, node: DoubleLinkedListNode) -> DoubleLinkedListNode | None:
        """Remove node from list"""
        if node.prev is None or node.next is None:
            return None
            
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
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
            node = self.cache[key]
            if self.list.remove(node):
                node.val = value
                self.list.add(node)
            return

        if self.size >= self.capacity:
            first = self.list.head.next
            if first and first.key and self.list.remove(first):
                del self.cache[first.key]
                self.size -= 1

        new_node = DoubleLinkedListNode(key, value)
        self.cache[key] = new_node
        self.list.add(new_node)
        self.size += 1


def lru_cache(size: int = 128) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """LRU Cache decorator"""
    def decorator_func(func: Callable[P, R]) -> Callable[P, R]:
        cache = LRUCache(size)
        
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            key = (args, tuple(sorted(kwargs.items())))
            cached = cache.get(key)
            if cached is not None:
                return cached
            
            result = func(*args, **kwargs)
            cache.put(key, result)
            return result
        
        # Add cache_info attribute
        wrapper.cache_info = lambda: cache  # type: ignore[attr-defined]
        return wrapper
    
    return decorator_func


if __name__ == "__main__":
    import doctest
    doctest.testmod()
