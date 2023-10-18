from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field


@dataclass
class StackWithQueues:
    """
    https://www.geeksforgeeks.org/implement-stack-using-queue/

    >>> stack = StackWithQueues()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.push(3)
    >>> stack.peek()
    3
    >>> stack.pop()
    3
    >>> stack.peek()
    2
    >>> stack.pop()
    2
    >>> stack.pop()
    1
    >>> stack.peek() is None
    True
    >>> stack.pop()
    Traceback (most recent call last):
        ...
    IndexError: pop from an empty deque
    """

    main_queue: deque[int] = field(default_factory=deque)
    temp_queue: deque[int] = field(default_factory=deque)

    def push(self, item: int) -> None:
        self.temp_queue.append(item)
        while self.main_queue:
            self.temp_queue.append(self.main_queue.popleft())
        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue

    def pop(self) -> int:
        return self.main_queue.popleft()

    def peek(self) -> int | None:
        return self.main_queue[0] if self.main_queue else None


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    stack: StackWithQueues | None = StackWithQueues()
    while stack:
        print("\nChoose operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Quit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            element = int(input("Enter an integer to push: ").strip())
            stack.push(element)
            print(f"{element} pushed onto the stack.")
        elif choice == "2":
            popped_element = stack.pop()
            if popped_element is not None:
                print(f"Popped element: {popped_element}")
            else:
                print("Stack is empty.")
        elif choice == "3":
            peeked_element = stack.peek()
            if peeked_element is not None:
                print(f"Top element: {peeked_element}")
            else:
                print("Stack is empty.")
        elif choice == "4":
            del stack
            stack = None
        else:
            print("Invalid choice. Please try again.")
