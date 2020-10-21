""" A Stack using a linked list like structure """
from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedStack:
    """
    Linked List Stack implementing push (to top),
    pop (from top) and is_empty

    >>> stack = LinkedStack()
    >>> stack.is_empty()
    True
    >>> stack.push(5)
    >>> stack.push(9)
    >>> stack.push('python')
    >>> stack.is_empty()
    False
    >>> stack.pop()
    'python'
    >>> stack.push('algorithms')
    >>> stack.pop()
    'algorithms'
    >>> stack.pop()
    9
    >>> stack.pop()
    5
    >>> stack.is_empty()
    True
    >>> stack.pop()
    Traceback (most recent call last):
        ...
    IndexError: pop from empty stack
    """

    def __init__(self) -> None:
        self.top = None

    def __iter__(self):
        node = self.top
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        """
        >>> stack = LinkedStack()
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> str(stack)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])

    def __len__(self):
        """
        >>> stack = LinkedStack()
        >>> len(stack) == 0
        True
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> len(stack) == 3
        True
        """
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        """
        >>> stack = LinkedStack()
        >>> stack.is_empty()
        True
        >>> stack.push(1)
        >>> stack.is_empty()
        False
        """
        return self.top is None

    def push(self, item: Any) -> None:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Python")
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> str(stack)
        'C->Java->Python'
        """
        node = Node(item)
        if not self.is_empty():
            node.next = self.top
        self.top = node

    def pop(self) -> Any:
        """
        >>> stack = LinkedStack()
        >>> stack.pop()
        Traceback (most recent call last):
        ...
        IndexError: pop from empty stack
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> stack.pop() == 'a'
        True
        >>> stack.pop() == 'b'
        True
        >>> stack.pop() == 'c'
        True
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        assert isinstance(self.top, Node)
        pop_node = self.top
        self.top = self.top.next
        return pop_node.data

    def peek(self) -> Any:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> stack.push("Python")
        >>> stack.peek()
        'Python'
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def clear(self) -> None:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> stack.push("Python")
        >>> str(stack)
        'Python->C->Java'
        >>> stack.clear()
        >>> len(stack) == 0
        True
        """
        self.top = None


if __name__ == "__main__":
    from doctest import testmod

    testmod()
