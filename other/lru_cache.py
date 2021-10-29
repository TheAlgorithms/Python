from __future__ import annotations

from typing import Callable


class DoubleLinkedListNode:
    """
    Double Linked List Node built specifically for LRU Cache

    >>> node = DoubleLinkedListNode(1,1)
    >>> node
    Node: key: 1, val: 1, has next: False, has prev: False
    """

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return "Node: key: {}, val: {}, has next: {}, has prev: {}".format(
            self.key, self.val, self.next is not None, self.prev is not None
        )


class DoubleLinkedList:
    """
    Double Linked List built specifically for LRU Cache

    >>> dll: DoubleLinkedList = DoubleLinkedList()
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, has next: True, has prev: False,
        Node: key: None, val: None, has next: False, has prev: True

    >>> first_node = DoubleLinkedListNode(1,10)
    >>> first_node
    Node: key: 1, val: 10, has next: False, has prev: False


    >>> dll.add(first_node)
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, has next: True, has prev: False,
        Node: key: 1, val: 10, has next: True, has prev: True,
        Node: key: None, val: None, has next: False, has prev: True

    >>> # node is mutated
    >>> first_node
    Node: key: 1, val: 10, has next: True, has prev: True

    >>> second_node = DoubleLinkedListNode(2,20)
    >>> second_node
    Node: key: 2, val: 20, has next: False, has prev: False

    >>> dll.add(second_node)
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, has next: True, has prev: False,
        Node: key: 1, val: 10, has next: True, has prev: True,
        Node: key: 2, val: 20, has next: True, has prev: True,
        Node: key: None, val: None, has next: False, has prev: True

    >>> removed_node = dll.remove(first_node)
    >>> assert removed_node == first_node
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, has next: True, has prev: False,
        Node: key: 2, val: 20, has next: True, has prev: True,
        Node: key: None, val: None, has next: False, has prev: True


    >>> # Attempt to remove node not on list
    >>> removed_node = dll.remove(first_node)
    >>> removed_node is None
    True

    >>> # Attempt to remove head or rear
    >>> dll.head
    Node: key: None, val: None, has next: True, has prev: False
    >>> dll.remove(dll.head) is None
    True

    >>> # Attempt to remove head or rear
    >>> dll.rear
    Node: key: None, val: None, has next: False, has prev: True
    >>> dll.remove(dll.rear) is None
    True


    """

    def __init__(self):
        self.head = DoubleLinkedListNode(None, None)
        self.rear = DoubleLinkedListNode(None, None)
        self.head.next, self.rear.prev = self.rear, self.head

    def __repr__(self) -> str:
        rep = ["DoubleLinkedList"]
        node = self.head
        while node.next is not None:
            rep.append(str(node))
            node = node.next
        rep.append(str(self.rear))
        return ",\n    ".join(rep)

    def add(self, node: DoubleLinkedListNode) -> None:
        """
        Adds the given node to the end of the list (before rear)
        """

        previous = self.rear.prev
        previous.next = node
        node.prev = previous
        self.rear.prev = node
        node.next = self.rear

    def remove(self, node: DoubleLinkedListNode) -> DoubleLinkedListNode | None:
        """
        Removes and returns the given node from the list

        Returns None if node.prev or node.next is None
        """

        if node.prev is None:
            return None
        elif node.next is None:
            return None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        return node


class LRUCache:
    """
    LRU Cache to store a given capacity of data. Can be used as a stand-alone object
    or as a function decorator.

    >>> cache = LRUCache(2)

    >>> cache.set(1, 1)
    >>> cache.set(2, 2)
    >>> cache.get(1)
    1

    >>> cache.list
    DoubleLinkedList,
        Node: key: None, val: None, has next: True, has prev: False,
        Node: key: 2, val: 2, has next: True, has prev: True,
        Node: key: 1, val: 1, has next: True, has prev: True,
        Node: key: None, val: None, has next: False, has prev: True

    >>> cache.cache
    {1: Node: key: 1, val: 1, has next: True, has prev: True, 2: Node: key: 2, val: 2, has next: True, has prev: True}

    >>> cache.set(3, 3)

    >>> cache.list
    DoubleLinkedList,
        Node: key: None, val: None, has next: True, has prev: False,
        Node: key: 1, val: 1, has next: True, has prev: True,
        Node: key: 3, val: 3, has next: True, has prev: True,
        Node: key: None, val: None, has next: False, has prev: True

    >>> cache.cache
    {1: Node: key: 1, val: 1, has next: True, has prev: True, 3: Node: key: 3, val: 3, has next: True, has prev: True}

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
    CacheInfo(hits=3, misses=2, capacity=2, current size=2)

    >>> @LRUCache.decorator(100)
    ... def fib(num):
    ...     if num in (1, 2):
    ...         return 1
    ...     return fib(num - 1) + fib(num - 2)

    >>> for i in range(1, 100):
    ...     res = fib(i)

    >>> fib.cache_info()
    CacheInfo(hits=194, misses=99, capacity=100, current size=99)
    """

    # class variable to map the decorator functions to their respective instance
    decorator_function_to_instance_map = {}

    def __init__(self, capacity: int):
        self.list = DoubleLinkedList()
        self.capacity = capacity
        self.num_keys = 0
        self.hits = 0
        self.miss = 0
        self.cache = {}

    def __repr__(self) -> str:
        """
        Return the details for the cache instance
        [hits, misses, capacity, current_size]
        """

        return (
            f"CacheInfo(hits={self.hits}, misses={self.miss}, "
            f"capacity={self.capacity}, current size={self.num_keys})"
        )

    def __contains__(self, key: int) -> bool:
        """
        >>> cache = LRUCache(1)

        >>> 1 in cache
        False

        >>> cache.set(1, 1)

        >>> 1 in cache
        True
        """

        return key in self.cache

    def get(self, key: int) -> int | None:
        """
        Returns the value for the input key and updates the Double Linked List.
        Returns None if key is not present in cache
        """

        if key in self.cache:
            self.hits += 1
            self.list.add(self.list.remove(self.cache[key]))
            return self.cache[key].val
        self.miss += 1
        return None

    def set(self, key: int, value: int) -> None:
        """
        Sets the value for the input key and updates the Double Linked List
        """

        if key not in self.cache:
            if self.num_keys >= self.capacity:
                key_to_delete = self.list.head.next.key
                self.list.remove(self.cache[key_to_delete])
                del self.cache[key_to_delete]
                self.num_keys -= 1
            self.cache[key] = DoubleLinkedListNode(key, value)
            self.list.add(self.cache[key])
            self.num_keys += 1

        else:
            node = self.list.remove(self.cache[key])
            node.val = value
            self.list.add(node)

    @staticmethod
    def decorator(size: int = 128):
        """
        Decorator version of LRU Cache
        """

        def cache_decorator_inner(func: Callable):
            def cache_decorator_wrapper(*args, **kwargs):
                if func not in LRUCache.decorator_function_to_instance_map:
                    LRUCache.decorator_function_to_instance_map[func] = LRUCache(size)

                result = LRUCache.decorator_function_to_instance_map[func].get(args[0])
                if result is None:
                    result = func(*args, **kwargs)
                    LRUCache.decorator_function_to_instance_map[func].set(
                        args[0], result
                    )
                return result

            def cache_info():
                return LRUCache.decorator_function_to_instance_map[func]

            cache_decorator_wrapper.cache_info = cache_info

            return cache_decorator_wrapper

        return cache_decorator_inner


if __name__ == "__main__":
    import doctest

    doctest.testmod()
