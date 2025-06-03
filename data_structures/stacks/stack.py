from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass


class Stack(Generic[T]):
    """A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, limit: int = 10):
        self.stack: list[T] = []
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, data: T) -> None:
        """
        Push an element to the top of the stack.

        >>> S = Stack(2) # stack size = 2
        >>> S.push(10)
        >>> S.push(20)
        >>> print(S)
        [10, 20]

        >>> S = Stack(1) # stack size = 1
        >>> S.push(10)
        >>> S.push(20)
        Traceback (most recent call last):
        ...
        data_structures.stacks.stack.StackOverflowError

        """
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self) -> T:
        """
        Pop an element off of the top of the stack.

        >>> S = Stack()
        >>> S.push(-5)
        >>> S.push(10)
        >>> S.pop()
        10

        >>> Stack().pop()
        Traceback (most recent call last):
            ...
        data_structures.stacks.stack.StackUnderflowError
        """
        if not self.stack:
            raise StackUnderflowError
        return self.stack.pop()

    def peek(self) -> T:
        """
        Peek at the top-most element of the stack.

        >>> S = Stack()
        >>> S.push(-5)
        >>> S.push(10)
        >>> S.peek()
        10

        >>> Stack().peek()
        Traceback (most recent call last):
            ...
        data_structures.stacks.stack.StackUnderflowError
        """
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]

    def is_empty(self) -> bool:
        """
        Check if a stack is empty.

        >>> S = Stack()
        >>> S.is_empty()
        True

        >>> S = Stack()
        >>> S.push(10)
        >>> S.is_empty()
        False
        """
        return not bool(self.stack)

    def is_full(self) -> bool:
        """
        >>> S = Stack()
        >>> S.is_full()
        False

        >>> S = Stack(1)
        >>> S.push(10)
        >>> S.is_full()
        True
        """
        return self.size() == self.limit

    def size(self) -> int:
        """
        Return the size of the stack.

        >>> S = Stack(3)
        >>> S.size()
        0

        >>> S = Stack(3)
        >>> S.push(10)
        >>> S.size()
        1

        >>> S = Stack(3)
        >>> S.push(10)
        >>> S.push(20)
        >>> S.size()
        2
        """
        return len(self.stack)

    def __contains__(self, item: T) -> bool:
        """
        Check if item is in stack

        >>> S = Stack(3)
        >>> S.push(10)
        >>> 10 in S
        True

        >>> S = Stack(3)
        >>> S.push(10)
        >>> 20 in S
        False
        """
        return item in self.stack


def test_stack() -> None:
    """
    >>> test_stack()
    """
    stack: Stack[int] = Stack(10)
    assert bool(stack) is False
    assert stack.is_empty() is True
    assert stack.is_full() is False
    assert str(stack) == "[]"

    try:
        _ = stack.pop()
        raise AssertionError  # This should not happen
    except StackUnderflowError:
        assert True  # This should happen

    try:
        _ = stack.peek()
        raise AssertionError  # This should not happen
    except StackUnderflowError:
        assert True  # This should happen

    for i in range(10):
        assert stack.size() == i
        stack.push(i)

    assert bool(stack)
    assert not stack.is_empty()
    assert stack.is_full()
    assert str(stack) == str(list(range(10)))
    assert stack.pop() == 9
    assert stack.peek() == 8

    stack.push(100)
    assert str(stack) == str([0, 1, 2, 3, 4, 5, 6, 7, 8, 100])

    try:
        stack.push(200)
        raise AssertionError  # This should not happen
    except StackOverflowError:
        assert True  # This should happen

    assert not stack.is_empty()
    assert stack.size() == 10

    assert 5 in stack
    assert 55 not in stack


if __name__ == "__main__":
    test_stack()

    import doctest

    doctest.testmod()
