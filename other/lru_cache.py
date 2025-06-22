from __future__ import annotations

from collections.abc import Callable, Hashable
from functools import wraps
from typing import Any, Generic, ParamSpec, TypeVar, overload, TYPE_CHECKING

if TYPE_CHECKING:
    type NodeKey = T | None
    type NodeValue = U | None
else:
    NodeKey = TypeVar("NodeKey", bound=Hashable)
    NodeValue = TypeVar("NodeValue")

T = TypeVar("T", bound=Hashable)
U = TypeVar("U")
P = ParamSpec("P")
R = TypeVar("R")


class DoubleLinkedListNode(Generic[T, U]):
    """Node built for LRU Cache"""

    def __init__(self, key: NodeKey, val: NodeValue) -> None:
        self.key = key
        self.val = val
        self.next: DoubleLinkedListNode[T, U] | None = None
        self.prev: DoubleLinkedListNode[T, U] | None = None

    def __repr__(self) -> str:
        return f"Node(key={self.key}, val={self.val})"


class DoubleLinkedList(Generic[T, U]):
    """Double Linked List for LRU Cache"""

    def __init__(self) -> None:
        self.head: DoubleLinkedListNode[T, U] = DoubleLinkedListNode(None, None)
        self.rear: DoubleLinkedListNode[T, U] = DoubleLinkedListNode(None, None)
        self.head.next, self.rear.prev = self.rear, self.head

    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return f"LinkedList({nodes})"

    def add(self, node: DoubleLinkedListNode[T, U]) -> None:
        """Add node to list end"""
        prev = self.rear.prev
        if not prev:
            raise ValueError("Invalid list state")

        prev.next = node
        node.prev = prev
        self.rear.prev = node
        node.next = self.rear

    def remove(
        self, node: DoubleLinkedListNode[T, U]
    ) -> DoubleLinkedListNode[T, U] | None:
        """Remove node from list"""
        if not node.prev or not node.next:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        return node


class LRUCache(Generic[T, U]):
    """LRU Cache implementation"""

    def __init__(self, capacity: int) -> None:
        self.list = DoubleLinkedList[T, U]()
        self.capacity = capacity
        self.size = 0
        self.hits = 0
        self.misses = 0
        self.cache: dict[T, DoubleLinkedListNode[T, U]] = {}

    def __repr__(self) -> str:
        return f"Cache(hits={self.hits}, misses={self.misses}, cap={self.capacity}, size={self.size})"

    def __contains__(self, key: T) -> bool:
        return key in self.cache

    def get(self, key: T) -> U | None:
        """Get value for key"""
        if key in self.cache:
            self.hits += 1
            node = self.cache[key]
            if self.list.remove(node):
                self.list.add(node)
            return node.val
        self.misses += 1
        return None

    def put(self, key: T, value: U) -> None:
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

        new_node: DoubleLinkedListNode[T, U] = DoubleLinkedListNode(key, value)
        self.cache[key] = new_node
        self.list.add(new_node)
        self.size += 1

    @classmethod
    def decorator(cls, size: int = 128) -> Callable[[Callable[P, R]], Callable[P, R]]:
        """LRU Cache decorator"""

        def decorator_func(func: Callable[P, R]) -> Callable[P, R]:
            cache = cls[Any, R](size)

            @wraps(func)
            def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
                key = (args, tuple(sorted(kwargs.items())))
                if (result := cache.get(key)) is None:
                    result = func(*args, **kwargs)
                    cache.put(key, result)
                return result

            wrapper.cache_info = lambda: cache  # Direct attribute assignment
            return wrapper

        return decorator_func


if __name__ == "__main__":
    import doctest

    doctest.testmod()
