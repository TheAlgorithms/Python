from __future__ import annotations

from typing import Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class DoubleLinkedListNode(Generic[T, U]):
    """
    Double Linked List Node built specifically for LFU Cache

    >>> node = DoubleLinkedListNode(1,1)
    >>> node
    Node: key: 1, val: 1, freq: 0, has next: False, has prev: False
    """

    def __init__(self, key: T | None, val: U | None):
        self.key = key
        self.val = val
        self.freq: int = 0
        self.next: DoubleLinkedListNode[T, U] | None = None
        self.prev: DoubleLinkedListNode[T, U] | None = None

    def __repr__(self) -> str:
        return "Node: key: {}, val: {}, freq: {}, has next: {}, has prev: {}".format(
            self.key, self.val, self.freq, self.next is not None, self.prev is not None
        )


class DoubleLinkedList(Generic[T, U]):
    """
    Double Linked List built specifically for LFU Cache

    >>> dll: DoubleLinkedList = DoubleLinkedList()
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, freq: 0, has next: True, has prev: False,
        Node: key: None, val: None, freq: 0, has next: False, has prev: True

    >>> first_node = DoubleLinkedListNode(1,10)
    >>> first_node
    Node: key: 1, val: 10, freq: 0, has next: False, has prev: False


    >>> dll.add(first_node)
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, freq: 0, has next: True, has prev: False,
        Node: key: 1, val: 10, freq: 1, has next: True, has prev: True,
        Node: key: None, val: None, freq: 0, has next: False, has prev: True

    >>> # node is mutated
    >>> first_node
    Node: key: 1, val: 10, freq: 1, has next: True, has prev: True

    >>> second_node = DoubleLinkedListNode(2,20)
    >>> second_node
    Node: key: 2, val: 20, freq: 0, has next: False, has prev: False

    >>> dll.add(second_node)
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, freq: 0, has next: True, has prev: False,
        Node: key: 1, val: 10, freq: 1, has next: True, has prev: True,
        Node: key: 2, val: 20, freq: 1, has next: True, has prev: True,
        Node: key: None, val: None, freq: 0, has next: False, has prev: True

    >>> removed_node = dll.remove(first_node)
    >>> assert removed_node == first_node
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, freq: 0, has next: True, has prev: False,
        Node: key: 2, val: 20, freq: 1, has next: True, has prev: True,
        Node: key: None, val: None, freq: 0, has next: False, has prev: True


    >>> # Attempt to remove node not on list
    >>> removed_node = dll.remove(first_node)
    >>> removed_node is None
    True

    >>> # Attempt to remove head or rear
    >>> dll.head
    Node: key: None, val: None, freq: 0, has next: True, has prev: False
    >>> dll.remove(dll.head) is None
    True

    >>> # Attempt to remove head or rear
    >>> dll.rear
    Node: key: None, val: None, freq: 0, has next: False, has prev: True
    >>> dll.remove(dll.rear) is None
    True


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
        """
        Adds the given node at the tail of the list and shifting it to proper position
        """

        previous = self.rear.prev

        # All nodes other than self.head are guaranteed to have non-None previous
        assert previous is not None

        previous.next = node
        node.prev = previous
        self.rear.prev = node
        node.next = self.rear
        node.freq += 1
        self._position_node(node)

    def _position_node(self, node: DoubleLinkedListNode[T, U]) -> None:
        """
        Moves node forward to maintain invariant of sort by freq value
        """

        while node.prev is not None and node.prev.freq > node.freq:
            # swap node with previous node
            previous_node = node.prev

            node.prev = previous_node.prev
            previous_node.next = node.prev
            node.next = previous_node
            previous_node.prev = node

    def remove(
        self, node: DoubleLinkedListNode[T, U]
    ) -> DoubleLinkedListNode[T, U] | None:
        """
        Removes and returns the given node from the list

        Returns None if node.prev or node.next is None
        """

        if node.prev is None or node.next is None:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node


class LFUCache(Generic[T, U]):
    """
    LFU Cache to store a given capacity of data. Can be used as a stand-alone object
    or as a function decorator.

    >>> cache = LFUCache(2)
    >>> cache.set(1, 1)
    >>> cache.set(2, 2)
    >>> cache.get(1)
    1
    >>> cache.set(3, 3)
    >>> cache.get(2) is None
    True
    >>> cache.set(4, 4)
    >>> cache.get(1) is None
    True
    >>> cache.get(3)
    3
    >>> cache.get(4)
    4
    >>> cache
    CacheInfo(hits=3, misses=2, capacity=2, current_size=2)
    >>> @LFUCache.decorator(100)
    ... def fib(num):
    ...     if num in (1, 2):
    ...         return 1
    ...     return fib(num - 1) + fib(num - 2)

    >>> for i in range(1, 101):
    ...     res = fib(i)

    >>> fib.cache_info()
    CacheInfo(hits=196, misses=100, capacity=100, current_size=100)
    """

    # class variable to map the decorator functions to their respective instance
    decorator_function_to_instance_map: dict[Callable[[T], U], LFUCache[T, U]] = {}

    def __init__(self, capacity: int):
        self.list: DoubleLinkedList[T, U] = DoubleLinkedList()
        self.capacity = capacity
        self.num_keys = 0
        self.hits = 0
        self.miss = 0
        self.cache: dict[T, DoubleLinkedListNode[T, U]] = {}

    def __repr__(self) -> str:
        """
        Return the details for the cache instance
        [hits, misses, capacity, current_size]
        """

        return (
            f"CacheInfo(hits={self.hits}, misses={self.miss}, "
            f"capacity={self.capacity}, current_size={self.num_keys})"
        )

    def __contains__(self, key: T) -> bool:
        """
        >>> cache = LFUCache(1)

        >>> 1 in cache
        False

        >>> cache.set(1, 1)
        >>> 1 in cache
        True
        """

        return key in self.cache

    def get(self, key: T) -> U | None:
        """
        Returns the value for the input key and updates the Double Linked List. Returns
        Returns None if key is not present in cache
        """

        if key in self.cache:
            self.hits += 1
            value_node: DoubleLinkedListNode[T, U] = self.cache[key]
            node = self.list.remove(self.cache[key])
            assert node == value_node

            # node is guaranteed not None because it is in self.cache
            assert node is not None
            self.list.add(node)
            return node.val
        self.miss += 1
        return None

    def set(self, key: T, value: U) -> None:
        """
        Sets the value for the input key and updates the Double Linked List
        """

        if key not in self.cache:
            if self.num_keys >= self.capacity:
                # delete first node when over capacity
                first_node = self.list.head.next

                # guaranteed to have a non-None first node when num_keys > 0
                # explain to type checker via assertions
                assert first_node is not None
                assert first_node.key is not None
                assert self.list.remove(first_node) is not None
                # first_node guaranteed to be in list

                del self.cache[first_node.key]
                self.num_keys -= 1
            self.cache[key] = DoubleLinkedListNode(key, value)
            self.list.add(self.cache[key])
            self.num_keys += 1

        else:
            node = self.list.remove(self.cache[key])
            assert node is not None  # node guaranteed to be in list
            node.val = value
            self.list.add(node)

    @classmethod
    def decorator(
        cls: type[LFUCache[T, U]], size: int = 128
    ) -> Callable[[Callable[[T], U]], Callable[..., U]]:
        """
        Decorator version of LFU Cache

        Decorated function must be function of T -> U
        """

        def cache_decorator_inner(func: Callable[[T], U]) -> Callable[..., U]:
            def cache_decorator_wrapper(*args: T) -> U:
                if func not in cls.decorator_function_to_instance_map:
                    cls.decorator_function_to_instance_map[func] = LFUCache(size)

                result = cls.decorator_function_to_instance_map[func].get(args[0])
                if result is None:
                    result = func(*args)
                    cls.decorator_function_to_instance_map[func].set(args[0], result)
                return result

            def cache_info() -> LFUCache[T, U]:
                return cls.decorator_function_to_instance_map[func]

            setattr(cache_decorator_wrapper, "cache_info", cache_info)

            return cache_decorator_wrapper

        return cache_decorator_inner


if __name__ == "__main__":
    import doctest

    doctest.testmod()
