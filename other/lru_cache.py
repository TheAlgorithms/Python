from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Generic, Optional, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class DoubleLinkedListNode(Generic[T, U]):
    """
    Double Linked List Node built specifically for LRU Cache

    >>> DoubleLinkedListNode(1,1)
    Node: key: 1, val: 1, has next: False, has prev: False
    """

    def __init__(self, key: Optional[T], val: Optional[U]) -> None:
        self.key = key
        self.val = val
        self.next: Optional[DoubleLinkedListNode[T, U]] = None
        self.prev: Optional[DoubleLinkedListNode[T, U]] = None

    def __repr__(self) -> str:
        return (
            f"Node: key: {self.key}, val: {self.val}, "
            f"has next: {bool(self.next)}, has prev: {bool(self.prev)}"
        )


class DoubleLinkedList(Generic[T, U]):
    """
    Double Linked List built specifically for LRU Cache
    ... [docstring unchanged] ...
    """

    def __init__(self) -> None:
        self.head: DoubleLinkedListNode[T, U] = DoubleLinkedListNode(None, None)
        self.rear: DoubleLinkedListNode[T, U] = DoubleLinkedListNode(None, None)
        self.head.next, self.rear.prev = self.rear, self.head

    def __repr__(self) -> str:
        rep = ["DoubleLinkedList"]
        node = self.head
        while node.next is not None:
            rep.append(str(node))
            node = node.next
        rep.append(str(self.rear))
        return ",\n    ".join(rep)

    def add(self, node: DoubleLinkedListNode[T, U]) -> None:
        """Adds the given node to the end of the list (before rear)"""
        previous = self.rear.prev
        if previous is None:
            raise ValueError("Invalid list state: rear.prev is None")
        
        previous.next = node
        node.prev = previous
        self.rear.prev = node
        node.next = self.rear
    def remove(
        self, node: DoubleLinkedListNode[T, U]
    ) -> Optional[DoubleLinkedListNode[T, U]]:
        """Removes and returns the given node from the list"""
        if node.prev is None or node.next is None:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node


class LRUCache(Generic[T, U]):
    """
    LRU Cache to store a given capacity of data
    ... [docstring unchanged] ...
    """

    def __init__(self, capacity: int) -> None:
        self.list: DoubleLinkedList[T, U] = DoubleLinkedList()
        self.capacity = capacity
        self.num_keys = 0
        self.hits = 0
        self.miss = 0
        self.cache: dict[T, DoubleLinkedListNode[T, U]] = {}

    def __repr__(self) -> str:
        return (
            f"CacheInfo(hits={self.hits}, misses={self.miss}, "
            f"capacity={self.capacity}, current size={self.num_keys})"
        )

    def __contains__(self, key: T) -> bool:
        return key in self.cache

    def get(self, key: T) -> Optional[U]:
        """Returns the value for the input key"""
        if key in self.cache:
            self.hits += 1
            value_node = self.cache[key]
            node = self.list.remove(value_node)
            if node is None:
                return None
            self.list.add(node)
            return node.val
        self.miss += 1
        return None
    def put(self, key: T, value: U) -> None:
        """Sets the value for the input key"""
        if key in self.cache:
            node = self.list.remove(self.cache[key])
            if node is None:
                return
            node.val = value
            self.list.add(node)
            return

        if self.num_keys >= self.capacity:
            first_node = self.list.head.next
            if first_node is None or first_node.key is None:
                return
            if self.list.remove(first_node) is not None:
                del self.cache[first_node.key]
                self.num_keys -= 1

        new_node = DoubleLinkedListNode(key, value)
        self.cache[key] = new_node
        self.list.add(new_node)
        self.num_keys += 1

    @classmethod
    def decorator(
        cls, size: int = 128
    ) -> Callable[[Callable[..., U]], Callable[..., U]]:
        """Decorator version of LRU Cache"""
        def decorator_func(func: Callable[..., U]) -> Callable[..., U]:
            cache_instance = cls(size)

            @wraps(func)
            def wrapper(*args: T, **kwargs: T) -> U:
                key = (args, tuple(kwargs.items()))
                result = cache_instance.get(key)
                if result is None:
                    result = func(*args, **kwargs)
                    cache_instance.put(key, result)
                return result
            def cache_info() -> LRUCache:
                return cache_instance

            setattr(wrapper, "cache_info", cache_info)
            return wrapper

        return decorator_func


if __name__ == "__main__":
    import doctest
    doctest.testmod()
