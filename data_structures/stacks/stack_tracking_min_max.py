from __future__ import annotations

import math

"""
Python3 stack implementation that retrieves min/max
elements of the stack in constant time
"""


class StackData:
    """
    Object stored on the stack
    """

    def __init__(
        self, current_value: float, min_value: float, max_value: float
    ) -> None:
        self.current_value = current_value
        self.min_value = min_value
        self.max_value = max_value


class MinMaxStack:
    """
    Main stack implementation
    """

    def __init__(self, max_stack_size: int = 10) -> None:
        self.max_size = max_stack_size
        self.stack: list[StackData] = []

    def push_value(self, value: float) -> bool:
        """
        Push new value on top of stack

        >>> test_stack = MinMaxStack(3)
        >>> test_stack.push_value(1)
        True
        >>> test_stack.push_value(2)
        True
        >>> test_stack.push_value(3)
        True
        >>> test_stack.push_value(4)
        Traceback (most recent call last):
            ...
        Exception: Max stack size reached.

        """

        if len(self.stack) == self.max_size:
            raise Exception("Max stack size reached.")

        if len(self.stack) == 0:
            self.stack.append(StackData(value, value, value))
        else:
            """Store min/max values with current value"""

            new_min = min(self.stack[-1].min_value, value)
            new_max = max(self.stack[-1].max_value, value)
            self.stack.append(StackData(value, new_min, new_max))

        return True

    def pop_value(self) -> float:
        """
        Remove the top value from the stack.

        >>> test_stack = MinMaxStack()
        >>> test_stack.push_value(1)
        True
        >>> test_stack.push_value(2)
        True
        >>> test_stack.pop_value()
        2
        >>> test_stack.pop_value()
        1
        >>> test_stack.pop_value()
        Stack is empty
        -inf
        """

        if self.stack_is_valid():
            return self.stack.pop().current_value

        return -math.inf

    def get_current_max(self) -> float:
        """
        Get the highest value on the stack in constant time

        >>> test_stack = MinMaxStack(3)
        >>> test_stack.push_value(-450.45)
        True
        >>> test_stack.push_value(450.45)
        True
        >>> test_stack.push_value(0)
        True
        >>> test_stack.get_current_max()
        450.45
        >>> test_stack.pop_value()
        0
        >>> test_stack.get_current_max()
        450.45
        >>> test_stack.pop_value()
        450.45
        >>> test_stack.get_current_max()
        -450.45
        >>> test_stack.pop_value()
        -450.45
        >>> test_stack.get_current_max()
        Stack is empty
        -inf
        """
        if self.stack_is_valid():
            return self.stack[-1].max_value

        return -math.inf

    def get_current_min(self) -> float:
        """
        Get the lowest value on the stack in constant time

        >>> test_stack = MinMaxStack(3)
        >>> test_stack.push_value(123)
        True
        >>> test_stack.push_value(-123)
        True
        >>> test_stack.push_value(0)
        True
        >>> test_stack.get_current_min()
        -123
        >>> test_stack.pop_value()
        0
        >>> test_stack.get_current_min()
        -123
        >>> test_stack.pop_value()
        -123
        >>> test_stack.get_current_min()
        123
        >>> test_stack.pop_value()
        123
        >>> test_stack.get_current_min()
        Stack is empty
        -inf
        """
        if self.stack_is_valid():
            return self.stack[-1].min_value

        return -math.inf

    def stack_is_valid(self) -> bool:
        """
        Validate stack is not empty

        >>> test_stack = MinMaxStack(3)
        >>> test_stack.stack_is_valid()
        Stack is empty
        False
        >>> test_stack.push_value(0)
        True
        >>> test_stack.stack_is_valid()
        True
        """
        if len(self.stack) == 0:
            print("Stack is empty")
            return False

        return True


if __name__ == "__main__":
    from doctest import testmod

    testmod()
