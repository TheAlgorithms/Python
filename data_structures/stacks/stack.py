from typing import List


class StackOverflowError(BaseException):
    pass


class Stack:
    """A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, limit: int = 10):
        self.stack: List[int] = []
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, data):
        """Push an element to the top of the stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        """Pop an element off of the top of the stack."""
        return self.stack.pop()

    def peek(self):
        """Peek at the top-most element of the stack."""
        return self.stack[-1]

    def is_empty(self) -> bool:
        """Check if a stack is empty."""
        return not bool(self.stack)

    def is_full(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        """Return the size of the stack."""
        return len(self.stack)

    def __contains__(self, item) -> bool:
        """Check if item is in stack"""
        return item in self.stack


def test_stack() -> None:
    """
    >>> test_stack()
    """
    stack = Stack(10)
    assert bool(stack) is False
    assert stack.is_empty() is True
    assert stack.is_full() is False
    assert str(stack) == "[]"

    try:
        _ = stack.pop()
        assert False  # This should not happen
    except IndexError:
        assert True  # This should happen

    try:
        _ = stack.peek()
        assert False  # This should not happen
    except IndexError:
        assert True  # This should happen

    for i in range(10):
        assert stack.size() == i
        stack.push(i)

    assert bool(stack) is True
    assert stack.is_empty() is False
    assert stack.is_full() is True
    assert str(stack) == str(list(range(10)))
    assert stack.pop() == 9
    assert stack.peek() == 8

    stack.push(100)
    assert str(stack) == str([0, 1, 2, 3, 4, 5, 6, 7, 8, 100])

    try:
        stack.push(200)
        assert False  # This should not happen
    except StackOverflowError:
        assert True  # This should happen

    assert stack.is_empty() is False
    assert stack.size() == 10

    assert 5 in stack
    assert 55 not in stack


if __name__ == "__main__":
    test_stack()
