"""
Implementation of double ended queue.
"""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any


class Deque:
    """
    Deque data structure.
    Operations
    ----------
    append(val: Any) -> None
    appendleft(val: Any) -> None
    extend(iterable: Iterable) -> None
    extendleft(iterable: Iterable) -> None
    pop() -> Any
    popleft() -> Any
    Observers
    ---------
    is_empty() -> bool
    Attributes
    ----------
    _front: _Node
        front of the deque a.k.a. the first element
    _back: _Node
        back of the element a.k.a. the last element
    _len: int
        the number of nodes
    """

    __slots__ = ["_front", "_back", "_len"]

    @dataclass
    class _Node:
        """
        Representation of a node.
        Contains a value and a pointer to the next node as well as to the previous one.
        """

        val: Any = None
        next_node: Deque._Node | None = None
        prev_node: Deque._Node | None = None

    class _Iterator:
        """
        Helper class for iteration. Will be used to implement iteration.
        Attributes
        ----------
        _cur: _Node
            the current node of the iteration.
        """

        __slots__ = ["_cur"]

        def __init__(self, cur: Deque._Node | None) -> None:
            self._cur = cur

        def __iter__(self) -> Deque._Iterator:
            """
            >>> our_deque = Deque([1, 2, 3])
            >>> iterator = iter(our_deque)
            """
            return self

        def __next__(self) -> Any:
            """
            >>> our_deque = Deque([1, 2, 3])
            >>> iterator = iter(our_deque)
            >>> next(iterator)
            1
            >>> next(iterator)
            2
            >>> next(iterator)
            3
            """
            if self._cur is None:
                # finished iterating
                raise StopIteration
            val = self._cur.val
            self._cur = self._cur.next_node

            return val

    def __init__(self, iterable: Iterable[Any] | None = None) -> None:
        self._front: Any = None
        self._back: Any = None
        self._len: int = 0

        if iterable is not None:
            # append every value to the deque
            for val in iterable:
                self.append(val)

    def append(self, val: Any) -> None:
        """
        Adds val to the end of the deque.
        Time complexity: O(1)
        >>> our_deque_1 = Deque([1, 2, 3])
        >>> our_deque_1.append(4)
        >>> our_deque_1
        [1, 2, 3, 4]
        >>> our_deque_2 = Deque('ab')
        >>> our_deque_2.append('c')
        >>> our_deque_2
        ['a', 'b', 'c']
        >>> from collections import deque
        >>> deque_collections_1 = deque([1, 2, 3])
        >>> deque_collections_1.append(4)
        >>> deque_collections_1
        deque([1, 2, 3, 4])
        >>> deque_collections_2 = deque('ab')
        >>> deque_collections_2.append('c')
        >>> deque_collections_2
        deque(['a', 'b', 'c'])
        >>> list(our_deque_1) == list(deque_collections_1)
        True
        >>> list(our_deque_2) == list(deque_collections_2)
        True
        """
        node = self._Node(val, None, None)
        if self.is_empty():
            # front = back
            self._front = self._back = node
            self._len = 1
        else:
            # connect nodes
            self._back.next_node = node
            node.prev_node = self._back
            self._back = node  # assign new back to the new node

            self._len += 1

            # make sure there were no errors
            assert not self.is_empty(), "Error on appending value."

    def appendleft(self, val: Any) -> None:
        """
        Adds val to the beginning of the deque.
        Time complexity: O(1)
        >>> our_deque_1 = Deque([2, 3])
        >>> our_deque_1.appendleft(1)
        >>> our_deque_1
        [1, 2, 3]
        >>> our_deque_2 = Deque('bc')
        >>> our_deque_2.appendleft('a')
        >>> our_deque_2
        ['a', 'b', 'c']
        >>> from collections import deque
        >>> deque_collections_1 = deque([2, 3])
        >>> deque_collections_1.appendleft(1)
        >>> deque_collections_1
        deque([1, 2, 3])
        >>> deque_collections_2 = deque('bc')
        >>> deque_collections_2.appendleft('a')
        >>> deque_collections_2
        deque(['a', 'b', 'c'])
        >>> list(our_deque_1) == list(deque_collections_1)
        True
        >>> list(our_deque_2) == list(deque_collections_2)
        True
        """
        node = self._Node(val, None, None)
        if self.is_empty():
            # front = back
            self._front = self._back = node
            self._len = 1
        else:
            # connect nodes
            node.next_node = self._front
            self._front.prev_node = node
            self._front = node  # assign new front to the new node

            self._len += 1

            # make sure there were no errors
            assert not self.is_empty(), "Error on appending value."

    def extend(self, iterable: Iterable[Any]) -> None:
        """
        Appends every value of iterable to the end of the deque.
        Time complexity: O(n)
        >>> our_deque_1 = Deque([1, 2, 3])
        >>> our_deque_1.extend([4, 5])
        >>> our_deque_1
        [1, 2, 3, 4, 5]
        >>> our_deque_2 = Deque('ab')
        >>> our_deque_2.extend('cd')
        >>> our_deque_2
        ['a', 'b', 'c', 'd']
        >>> from collections import deque
        >>> deque_collections_1 = deque([1, 2, 3])
        >>> deque_collections_1.extend([4, 5])
        >>> deque_collections_1
        deque([1, 2, 3, 4, 5])
        >>> deque_collections_2 = deque('ab')
        >>> deque_collections_2.extend('cd')
        >>> deque_collections_2
        deque(['a', 'b', 'c', 'd'])
        >>> list(our_deque_1) == list(deque_collections_1)
        True
        >>> list(our_deque_2) == list(deque_collections_2)
        True
        """
        for val in iterable:
            self.append(val)

    def extendleft(self, iterable: Iterable[Any]) -> None:
        """
        Appends every value of iterable to the beginning of the deque.
        Time complexity: O(n)
        >>> our_deque_1 = Deque([1, 2, 3])
        >>> our_deque_1.extendleft([0, -1])
        >>> our_deque_1
        [-1, 0, 1, 2, 3]
        >>> our_deque_2 = Deque('cd')
        >>> our_deque_2.extendleft('ba')
        >>> our_deque_2
        ['a', 'b', 'c', 'd']
        >>> from collections import deque
        >>> deque_collections_1 = deque([1, 2, 3])
        >>> deque_collections_1.extendleft([0, -1])
        >>> deque_collections_1
        deque([-1, 0, 1, 2, 3])
        >>> deque_collections_2 = deque('cd')
        >>> deque_collections_2.extendleft('ba')
        >>> deque_collections_2
        deque(['a', 'b', 'c', 'd'])
        >>> list(our_deque_1) == list(deque_collections_1)
        True
        >>> list(our_deque_2) == list(deque_collections_2)
        True
        """
        for val in iterable:
            self.appendleft(val)

    def pop(self) -> Any:
        """
        Removes the last element of the deque and returns it.
        Time complexity: O(1)
        @returns topop.val: the value of the node to pop.
        >>> our_deque = Deque([1, 2, 3, 15182])
        >>> our_popped = our_deque.pop()
        >>> our_popped
        15182
        >>> our_deque
        [1, 2, 3]
        >>> from collections import deque
        >>> deque_collections = deque([1, 2, 3, 15182])
        >>> collections_popped = deque_collections.pop()
        >>> collections_popped
        15182
        >>> deque_collections
        deque([1, 2, 3])
        >>> list(our_deque) == list(deque_collections)
        True
        >>> our_popped == collections_popped
        True
        """
        # make sure the deque has elements to pop
        assert not self.is_empty(), "Deque is empty."

        topop = self._back
        self._back = self._back.prev_node  # set new back
        # drop the last node - python will deallocate memory automatically
        self._back.next_node = None

        self._len -= 1

        return topop.val

    def popleft(self) -> Any:
        """
        Removes the first element of the deque and returns it.
        Time complexity: O(1)
        @returns topop.val: the value of the node to pop.
        >>> our_deque = Deque([15182, 1, 2, 3])
        >>> our_popped = our_deque.popleft()
        >>> our_popped
        15182
        >>> our_deque
        [1, 2, 3]
        >>> from collections import deque
        >>> deque_collections = deque([15182, 1, 2, 3])
        >>> collections_popped = deque_collections.popleft()
        >>> collections_popped
        15182
        >>> deque_collections
        deque([1, 2, 3])
        >>> list(our_deque) == list(deque_collections)
        True
        >>> our_popped == collections_popped
        True
        """
        # make sure the deque has elements to pop
        assert not self.is_empty(), "Deque is empty."

        topop = self._front
        self._front = self._front.next_node  # set new front and drop the first node
        self._front.prev_node = None

        self._len -= 1

        return topop.val

    def is_empty(self) -> bool:
        """
        Checks if the deque is empty.
        Time complexity: O(1)
        >>> our_deque = Deque([1, 2, 3])
        >>> our_deque.is_empty()
        False
        >>> our_empty_deque = Deque()
        >>> our_empty_deque.is_empty()
        True
        >>> from collections import deque
        >>> empty_deque_collections = deque()
        >>> list(our_empty_deque) == list(empty_deque_collections)
        True
        """
        return self._front is None

    def __len__(self) -> int:
        """
        Implements len() function. Returns the length of the deque.
        Time complexity: O(1)
        >>> our_deque = Deque([1, 2, 3])
        >>> len(our_deque)
        3
        >>> our_empty_deque = Deque()
        >>> len(our_empty_deque)
        0
        >>> from collections import deque
        >>> deque_collections = deque([1, 2, 3])
        >>> len(deque_collections)
        3
        >>> empty_deque_collections = deque()
        >>> len(empty_deque_collections)
        0
        >>> len(our_empty_deque) == len(empty_deque_collections)
        True
        """
        return self._len

    def __eq__(self, other: object) -> bool:
        """
        Implements "==" operator. Returns if *self* is equal to *other*.
        Time complexity: O(n)
        >>> our_deque_1 = Deque([1, 2, 3])
        >>> our_deque_2 = Deque([1, 2, 3])
        >>> our_deque_1 == our_deque_2
        True
        >>> our_deque_3 = Deque([1, 2])
        >>> our_deque_1 == our_deque_3
        False
        >>> from collections import deque
        >>> deque_collections_1 = deque([1, 2, 3])
        >>> deque_collections_2 = deque([1, 2, 3])
        >>> deque_collections_1 == deque_collections_2
        True
        >>> deque_collections_3 = deque([1, 2])
        >>> deque_collections_1 == deque_collections_3
        False
        >>> (our_deque_1 == our_deque_2) == (deque_collections_1 == deque_collections_2)
        True
        >>> (our_deque_1 == our_deque_3) == (deque_collections_1 == deque_collections_3)
        True
        """

        if not isinstance(other, Deque):
            return NotImplemented

        me = self._front
        oth = other._front

        # if the length of the dequeues are not the same, they are not equal
        if len(self) != len(other):
            return False

        while me is not None and oth is not None:
            # compare every value
            if me.val != oth.val:
                return False
            me = me.next_node
            oth = oth.next_node

        return True

    def __iter__(self) -> Deque._Iterator:
        """
        Implements iteration.
        Time complexity: O(1)
        >>> our_deque = Deque([1, 2, 3])
        >>> for v in our_deque:
        ...     print(v)
        1
        2
        3
        >>> from collections import deque
        >>> deque_collections = deque([1, 2, 3])
        >>> for v in deque_collections:
        ...     print(v)
        1
        2
        3
        """
        return Deque._Iterator(self._front)

    def __repr__(self) -> str:
        """
        Implements representation of the deque.
        Represents it as a list, with its values between '[' and ']'.
        Time complexity: O(n)
        >>> our_deque = Deque([1, 2, 3])
        >>> our_deque
        [1, 2, 3]
        """
        values_list = []
        aux = self._front
        while aux is not None:
            # append the values in a list to display
            values_list.append(aux.val)
            aux = aux.next_node

        return f"[{', '.join(repr(val) for val in values_list)}]"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
