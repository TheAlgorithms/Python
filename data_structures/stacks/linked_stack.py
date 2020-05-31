""" A Stack using a Linked List like structure """
from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional["Node"] = None):
        self.data: Any = data
        self.next: Optional["Node"] = next


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
    >>> stack.is_empty();
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
        self.top: Optional[Node] = None

    def is_empty(self) -> bool:
        """ returns boolean describing if stack is empty """
        return self.top is None

    def push(self, item: Any) -> None:
        """ append item to top of stack """
        node: Node = Node(item)
        if self.is_empty():
            self.top = node
        else:
            # each node points to the item "lower" in the stack
            node.next = self.top
            self.top = node

    def pop(self) -> Any:
        """ returns and removes item at top of stack """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        else:
            # "remove" element by having top point to the next one
            assert isinstance(self.top, Node)
            node: Node = self.top
            self.top = node.next
            return node.data
