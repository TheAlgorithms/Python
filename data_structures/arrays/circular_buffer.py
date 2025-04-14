class CircularBuffer:
    def __init__(self, capacity):
        self._tail = 0
        self._head = 0
        self._array = [None] * capacity

    def _push(self, item):
        if self.is_full:
            raise Exception("push to full queue")
        self._array[self._head] = item
        self._head = self.wrap(self._head + 1)

    def push(self, item, overwrite=True):
        res = None
        if self.is_full and overwrite:
            res = self.pop()
        self._push(item)
        return res

    @property
    def is_full(self):
        return self._tail == self.wrap(self._head + 1)

    @property
    def is_empty(self):
        return self._tail == self._head

    def pop(self):
        if self.is_empty:
            raise Exception("pop from empty queue")
        item = self._array[self._tail]
        self._tail = self.wrap(self._tail + 1)
        return item

    def wrap(self, value):
        """
        >>> cb = CircularBuffer(6)
        >>> cb.wrap(5)
        5
        >>> cb.wrap(6)
        0

        >>> cb = CircularBuffer(8)
        >>> cb.wrap(7)
        7
        >>> cb.wrap(8)
        0
        """
        if self._is_power_of_two():
            # optimization taken from https://github.com/AndersKaloer/Ring-Buffer/blob/1468e24fc55986/ringbuffer.c#L26
            return value & (self.capacity - 1)
        return value % self.capacity

    def _is_power_of_two(self):
        return not self.capacity & (self.capacity - 1)

    @property
    def capacity(self):
        """Length of the underlying storage array

        One slot is always left empty to distinguish between “full” and “empty”
        states. As a result, although len(self._array) is N, the usable
        capacity is N-1.
        """
        return len(self._array)

    @property
    def size(self):
        return self.wrap(self._head - self._tail)

    def __iter__(self):
        # WARNING: the object should not be changed during iteration
        i = self._tail
        while i != self._head:
            yield self._array[i]
            i = self.wrap(i + 1)

    def __getitem__(self, index_from_tail):
        """
        >>> cb = CircularBuffer(8)
        >>> for i in range(10):
        ...     cb.push(i);
        0
        1
        2
        >>> cb.pop()
        3
        >>> cb.pop()
        4
        >>> print(cb, end='')
               8
               9
          h -> <free>
               <free>
               <free>
          t -> 5
               6
               7

        >>> cb[0]
        5
        >>> cb[1]
        6
        >>> cb[3]
        8
        >>> cb[5]
        Traceback (most recent call last):
        ...
        IndexError: ...

        >>> cb[-1]
        9
        >>> cb[-5]
        5
        >>> cb[-6]
        Traceback (most recent call last):
        ...
        IndexError: ...
        """

        if not -self.size <= index_from_tail < self.size:
            raise IndexError(
                "%d not in range [%d, %d)" % (index_from_tail, -self.size, self.size)
            )
        if index_from_tail >= 0:
            index_array = index_from_tail + self._tail
        else:
            index_array = self._head + index_from_tail
        return self._array[self.wrap(index_array)]

    def __str__(self):
        res = ""
        for i in range(self.capacity):
            if i == self._head == self._tail:
                res += "h=t -> "
            elif i == self._head:
                res += "  h -> "
            elif i == self._tail:
                res += "  t -> "
            else:
                res += "       "

            if self.wrap(i - self._tail) < self.size:
                res += str(self._array[i])
            else:
                res += "<free>"
            res += "\n"
        return res


import pytest


def test():
    b = CircularBuffer(8)
    assert b.capacity == 8

    assert (
        str(b)
        == """\
h=t -> <free>
       <free>
       <free>
       <free>
       <free>
       <free>
       <free>
       <free>
"""
    )

    for i in range(6):
        b.push(i)
    assert b.size == 6

    assert list(iter(b)) == list(range(6))

    assert b.pop() == 0
    assert b.pop() == 1

    assert (
        str(b)
        == """\
       <free>
       <free>
  t -> 2
       3
       4
       5
  h -> <free>
       <free>
"""
    )

    for _ in range(4):
        b.pop()

    with pytest.raises(Exception, match="pop from empty queue"):
        b.pop()


def test_overflow():
    b = CircularBuffer(8)

    for i in range(10):
        b.push(i)

    assert list(iter(b)) == list(range(3, 10))
    assert b.size == 7

    assert (
        str(b)
        == """\
       8
       9
  h -> <free>
  t -> 3
       4
       5
       6
       7
"""
    )

    assert b.pop() == 3
    assert b.pop() == 4
    assert (
        str(b)
        == """\
       8
       9
  h -> <free>
       <free>
       <free>
  t -> 5
       6
       7
"""
    )
