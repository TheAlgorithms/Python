from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self, capacity: int = 100) -> None:
        """Stack implementation using a static array"""

        self.__capacity = capacity
        self.__stack = [None] * self.__capacity
        self.__size = 0
        self.__top = -1

    def push(self, value: T) -> None:
        """Insert an item to the top of the stack
        >>> stack = Stack(3)

        >>> stack.display()
        []

        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)

        >>> stack.display()
        [1, 2, 3]
        """

        if self.is_full():
            self.__resize()

        self.__top += 1
        self.__stack[self.__top] = value
        self.__size += 1

    def peek(self) -> T:
        """Return the top item of the stack
        >>> stack = Stack(3)

        >>> stack.peek()
        Traceback (most recent call last):
        ...
        Exception: The stack is empty

        >>> stack.push(10)
        >>> stack.peek()
        10

        >>> stack.push(30)
        >>> stack.peek()
        30
        """

        if self.is_empty():
            raise Exception("The stack is empty")

        return self.__stack[self.__top]

    def pop(self) -> T:
        """Remove an item from the top of the stack

        >>> stack = Stack(3)

        >>> stack.pop()
        Traceback (most recent call last):
        ...
        Exception: The stack is empty

        >>> stack.push(56)
        >>> stack.push(45)
        >>> stack.push(2)

        >>> stack.pop()
        2
        >>> stack.pop()
        45
        >>> stack.pop()
        56
        """

        if self.is_empty():
            raise Exception("The stack is empty")

        deleted = self.__stack[self.__top]

        self.__size -= 1
        self.__top -= 1

        return deleted

    def get_capacity(self) -> int:
        """Returns the capacity of the stack

        >>> stack = Stack(34)

        >>> stack.get_capacity()
        34

        >>> stack = Stack()

        >>> stack.get_capacity()
        100

        """
        return self.__capacity

    def size(self) -> int:
        """Returns the length of the stack
        >>> stack = Stack(3)
        >>> stack.size()
        0
        >>> stack.push(1)
        >>> stack.size()
        1
        >>> stack.pop()
        1
        >>> stack.size()
        0
        """

        return self.__size

    def is_empty(self) -> bool:
        """Returns True if the stack is empty

        >>> stack = Stack(3)

        >>> stack.is_empty()
        True

        >>> stack.push(8)

        >>> stack.is_empty()
        False
        """

        return not self.__size

    def display(self) -> None:
        """Print each item inside the stack
        >>> stack = Stack(3)

        >>> stack.display()
        []

        >>> stack.push(13)
        >>> stack.push(23)
        >>> stack.push(34)

        >>> stack.display()
        [13, 23, 34]
        """

        print("[", end="")

        for i in range(self.__size):
            print(self.__stack[i], end=", " if i != self.__size - 1 else "")

        print("]")

    def is_full(self) -> bool:
        """Returns True if the stack is full

        >>> stack = Stack(3)

        >>> stack.is_full()
        False

        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)

        >>> stack.is_full()
        True
        """

        return self.__size == self.__capacity

    def __resize(self) -> None:
        """Double the size of the stack when it's full"""

        self.__capacity *= 2
        temp_list = [None] * self.__capacity

        for i in range(self.__size):
            temp_list[i] = self.__stack[i]

        self.__stack = temp_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
