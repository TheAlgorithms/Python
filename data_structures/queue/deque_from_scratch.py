"""
Implementation of double ended queue.
"""
import collections  # just for doctests
from dataclasses import dataclass
from typing import Any, Iterable


class Deque:
    """
    Deque data structure.

    Operations
    ----------
    append(val: Any) -> None

    appendleft(val: Any) -> None

    extend(iter: list) -> None

    extendleft(iter: list) -> None

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
        next: "_Node" = None
        prev: "_Node" = None

    class _Iterator:
        """
        Helper class for iteration. Will be used to implement iteration.

        Attributes
        ----------
        _cur: _Node
            the current node of the iteration.
        """

        __slots__ = ["_cur"]

        def __init__(self, cur: "_Node") -> None:
            self._cur = cur

        def __iter__(self) -> "_Iterator":
            """
            >>> d = Deque([1, 2, 3])
            >>> iterator = iter(d)
            """
            return self

        def __next__(self) -> Any:
            """
            >>> d = Deque([1, 2, 3])
            >>> iterator = iter(d)
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
            self._cur = self._cur.next

            return val

    def __init__(self, iterable: Iterable = None) -> None:
        self._front = self._back = None
        self._len = 0

        if iterable is not None:
            # append every value to the deque
            for val in iterable:
                self.append(val)

    def append(self, val: Any) -> None:
        """
        Adds val to the end of the deque.
        Time complexity: O(1)

        >>> d = Deque([1, 2, 3])
        >>> d.append(4)
        >>> print(d)
        [1, 2, 3, 4]

        >>> d2 = collections.deque([1, 2, 3])
        >>> d2.append(4)
        >>> print(d2)
        deque([1, 2, 3, 4])
        """
        node = self._Node(val, None, None)
        if self.is_empty():
            # front = back
            self._front = self._back = node
            self._len = 1
        else:
            # connect nodes
            self._back.next = node
            node.prev = self._back
            self._back = node  # assign new back to the new node

            self._len += 1

            # make sure there was no errors
            assert not self.is_empty(), "Error on appending value."

    def appendleft(self, val: Any) -> None:
        """
        Adds val to the beginning of the deque.
        Time complexity: O(1)

        >>> d = Deque([2, 3])
        >>> d.appendleft(1)
        >>> print(d)
        [1, 2, 3]

        >>> d2 = collections.deque([2, 3])
        >>> d2.appendleft(1)
        >>> print(d2)
        deque([1, 2, 3])
        """
        node = self._Node(val, None, None)
        if self.is_empty():
            # front = back
            self._front = self._back = node
            self._len = 1
        else:
            # connect nodes
            node.next = self._front
            self._front.prev = node
            self._front = node  # assign new front to the new node

            self._len += 1

            # make sure there was no errors
            assert not self.is_empty(), "Error on appending value."

    def extend(self, iter: Iterable) -> None:
        """
        Appends every value of iter to the end of the deque.
        Time complexity: O(n)

        >>> d = Deque([1, 2, 3])
        >>> d.extend([4, 5])
        >>> print(d)
        [1, 2, 3, 4, 5]

        >>> d2 = collections.deque([1, 2, 3])
        >>> d2.extend([4, 5])
        >>> print(d2)
        deque([1, 2, 3, 4, 5])
        """
        for val in iter:
            self.append(val)

    def extendleft(self, iter: Iterable) -> None:
        """
        Appends every value of iter to the beginning of the deque.
        Time complexity: O(n)

        >>> d = Deque([1, 2, 3])
        >>> d.extendleft([0, -1])
        >>> print(d)
        [-1, 0, 1, 2, 3]

        >>> d2 = collections.deque([1, 2, 3])
        >>> d2.extendleft([0, -1])
        >>> print(d2)
        deque([-1, 0, 1, 2, 3])
        """
        for val in iter:
            self.appendleft(val)

    def pop(self) -> Any:
        """
        Removes the last element of the deque and returns it.
        Time complexity: O(1)

        @returns topop.val: the value of the node to pop.

        >>> d = Deque([1, 2, 3, 15182])
        >>> popped = d.pop()
        >>> print(popped)
        15182
        >>> print(d)
        [1, 2, 3]

        >>> d2 = collections.deque([1, 2, 3, 15182])
        >>> popped = d2.pop()
        >>> print(popped)
        15182
        >>> print(d2)
        deque([1, 2, 3])
        """
        # make sure the deque has elements to pop
        assert not self.is_empty(), "Deque is empty."

        topop = self._back
        self._back = self._back.prev  # set new back
        self._back.next = (
            None  # drop the last node - python will deallocate memory automatically
        )

        self._len -= 1

        return topop.val

    def popleft(self) -> Any:
        """
        Removes the first element of the deque and returns it.
        Time complexity: O(1)

        @returns topop.val: the value of the node to pop.

        >>> d = Deque([15182, 1, 2, 3])
        >>> popped = d.popleft()
        >>> print(popped)
        15182
        >>> print(d)
        [1, 2, 3]

        >>> d2 = collections.deque([15182, 1, 2, 3])
        >>> popped = d2.popleft()
        >>> print(popped)
        15182
        >>> print(d2)
        deque([1, 2, 3])
        """
        # make sure the deque has elements to pop
        assert not self.is_empty(), "Deque is empty."

        topop = self._front
        self._front = self._front.next  # set new front and drop the first node
        self._front.prev = None

        self._len -= 1

        return topop.val

    def is_empty(self) -> bool:
        """
        Checks if the deque is empty.
        Time complexity: O(1)

        >>> d = Deque([1, 2, 3])
        >>> print(d.is_empty())
        False
        >>> d2 = Deque()
        >>> print(d2.is_empty())
        True
        """
        return self._front is None

    def __len__(self) -> int:
        """
        Implements len() function. Returns the length of the deque.
        Time complexity: O(1)

        >>> d = Deque([1, 2, 3])
        >>> print(len(d))
        3
        >>> d2 = Deque()
        >>> print(len(d2))
        0

        >>> d3 = collections.deque([1, 2, 3])
        >>> print(len(d3))
        3
        >>> d4 = collections.deque()
        >>> print(len(d4))
        0
        """
        return self._len

    def __eq__(self, other: "Deque") -> bool:
        """
        Implements "==" operator. Returns if *self* is equal to *other*.
        Time complexity: O(n)

        >>> d = Deque([1, 2, 3])
        >>> d2 = Deque([1, 2, 3])
        >>> print(d == d2)
        True
        >>> d3 = Deque([1, 2])
        >>> print(d == d3)
        False

        >>> d4 = collections.deque([1, 2, 3])
        >>> d5 = collections.deque([1, 2, 3])
        >>> print(d4 == d5)
        True
        >>> d6 = collections.deque([1, 2])
        >>> print(d5 == d6)
        False
        """
        me = self._front
        oth = other._front

        # if the length of the deques are not the same, they are not equal
        if len(self) != len(other):
            return False

        while me is not None and oth is not None:
            # compare every value
            if me.val != oth.val:
                return False
            me = me.next
            oth = oth.next

        return True

    def __iter__(self) -> "_Iterator":
        """
        Implements iteration.
        Time complexity: O(1)

        >>> d = Deque([1, 2, 3])
        >>> for v in d:
        ...     print(v)
        1
        2
        3

        >>> d2 = collections.deque([1, 2, 3])
        >>> for v in d2:
        ...     print(v)
        1
        2
        3
        """
        return Deque._Iterator(self._front)

    def __repr__(self) -> str:
        """
        Implements representation of the deque. Represents it as a list, with its values between '[' and ']'.
        Time complexity: O(n)

        >>> d = Deque([1, 2, 3])
        >>> print(d)
        [1, 2, 3]
        """
        l = []
        aux = self._front
        while aux is not None:
            # append the values in a list to display
            l.append(aux.val)
            aux = aux.next

        return "[" + ", ".join(repr(x) for x in l) + "]"
