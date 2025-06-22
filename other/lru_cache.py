from __future__ import annotations

from collections.abc import Callable, Hashable
from functools import wraps
from typing import Generic, TypeVar, Any, cast, overload, TYPE_CHECKING
from typing_extensions import ParamSpec

if TYPE_CHECKING:
    from typing_extensions import TypeAlias

T = TypeVar("T", bound=Hashable)
U = TypeVar("U")
P = ParamSpec("P")
R = TypeVar("R")

if TYPE_CHECKING:
    NodeKey: TypeAlias = T | None
    NodeValue: TypeAlias = U | None
else:
    NodeKey = TypeVar("NodeKey", bound=Hashable)
    NodeValue = TypeVar("NodeValue")


class DoubleLinkedListNode(Generic[T, U]):
    """
    Double Linked List Node built specifically for LRU Cache

    >>> DoubleLinkedListNode(1,1)
    Node: key: 1, val: 1, has next: False, has prev: False
    """

    def __init__(self, key: NodeKey, val: NodeValue) -> None:
        self.key = key
        self.val = val
        self.next: DoubleLinkedListNode[T, U] | None = None
        self.prev: DoubleLinkedListNode[T, U] | None = None

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
    ) -> DoubleLinkedListNode[T, U] | None:
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

    def get(self, key: T) -> U | None:
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

    @overload
    @classmethod
    def decorator(
        cls, size: int = 128
    ) -> Callable[[Callable[P, R]], Callable[P, R]]:
        ...
    
    @overload
    @classmethod
    def decorator(
        cls, func: Callable[P, R]
    ) -> Callable[P, R]:
        ...

    @classmethod
    def decorator(
        cls, size: int | Callable[P, R] = 128
    ) -> Callable[[Callable[P, R]], Callable[P, R]] | Callable[P, R]:
        """Decorator version of LRU Cache"""
        if callable(size):
            # Called without parentheses (@LRUCache.decorator)
            return cls.decorator()(size)
        
        def decorator_func(func: Callable[P, R]) -> Callable[P, R]:
            cache_instance = cls[Any, R](size)  # type: ignore[valid-type]

            @wraps(func)
            def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
                # Create normalized key
                sorted_kwargs = tuple(sorted(kwargs.items(), key=lambda x: x[0]))
                key = (args, sorted_kwargs)
                result = cache_instance.get(key)
                if result is None:
                    result = func(*args, **kwargs)
                    cache_instance.put(key, result)
                return result
            def cache_info() -> LRUCache[Any, R]:  # type: ignore[valid-type]
                return cache_instance

            wrapper.cache_info = cache_info  # Direct assignment
            return wrapper

        return decorator_func


if __name__ == "__main__":
    import doctest
    doctest.testmod()
