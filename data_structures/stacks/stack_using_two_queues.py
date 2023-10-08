from collections import deque
from typing import Optional


class StackUsingQueues:
    def __init__(self) -> None:
        self.queue1: deque = deque()
        self.queue2: deque = deque()

    def push(self, value: int) -> None:
        """
        Pushes an element onto the stack.

        Args:
            value (int): The element to push onto the stack.

        Example:
            >>> stack = StackUsingQueues()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
        """
        self.queue2.append(value)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> None:
        """
        Pops and removes the top element from the stack.

        Example:
            >>> stack = StackUsingQueues()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.pop()
        """
        if self.queue1:
            self.queue1.popleft()

    def top(self) -> Optional[int]:
        """
        Returns the top element of the stack without removing it.

        Returns:
            int: The top element of the stack, or None if the stack is empty.

        Example:
            >>> stack = StackUsingQueues()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.top()
            2
        """
        if self.queue1:
            return self.queue1[0]
        return None

    def size(self) -> int:
        """
        Returns the current size (number of elements) of the stack.

        Returns:
            int: The size of the stack.

        Example:
            >>> stack = StackUsingQueues()
            >>> stack.size()
            0
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> stack.size()
            3
            >>> stack.pop()
            >>> stack.size()
            2
        """
        return len(self.queue1)

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.

        Example:
            >>> stack = StackUsingQueues()
            >>> stack.is_empty()
            True
            >>> stack.push(1)
            >>> stack.is_empty()
            False
        """
        return len(self.queue1) == 0

    def peek(self) -> Optional[int]:
        """
        Returns the top element of the stack without removing it.

        Returns:
            int: The top element of the stack, or None if the stack is empty.

        Example:
            >>> stack = StackUsingQueues()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.peek()
            2
        """
        if self.queue1:
            return self.queue1[0]
        return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
