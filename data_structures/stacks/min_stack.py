class MinStack:
    """ Designing a Stack that can return Minimum element in Constant time"""

    def __init__(self):
        """ Creating stack minStack and size Variable"""
        self.stack = []
        self.minStack = []
        self.size = 0

    def push(self, data: int) -> None:
        """
        Push helps to put a element a the end of the stack
        >>> s = MinStack()
        >>> s.push(1)
        >>> assert s.size == 1
        """
        if self.size == 0:
            self.minStack.append(data)
        elif data <= self.minStack[-1]:
            self.minStack.append(data)
        self.stack.append(data)
        self.size = self.size + 1

    def pop(self) -> None:
        """Removes the topmost element from the Stack
        >>> s = MinStack()
        >>> s.push(1)
        >>> s.push(2)
        >>> assert s.pop() == 2
        """
        top = self.stack.pop()
        self.size = self.size - 1
        if top <= self.minStack[-1]:
            self.minStack.pop()
        return top

    def top(self) -> None:
        """Returns the top element from the stack
        >>> s = MinStack()
        >>> s.push(3)
        >>> s.push(2)
        >>> assert s.top() == 2
        """
        return self.stack[-1]

    def get_min(self):
        """Returns the top element from the  Minstack
        >>> s = MinStack()
        >>> s.push(5)
        >>> assert s.get_min() == 5
        """
        return self.minStack[-1]


# Code execution starts here
if __name__ == "__main__":

    # Creating a min Stack
    stack = MinStack()

    stack.push(6)
    print(stack.get_min())  # prints  6

    stack.push(7)
    print(stack.get_min())  # prints 6

    stack.push(8)
    print(stack.get_min())  # prints 6

    stack.push(5)
    print(stack.get_min())  # prints 5

    stack.push(3)
    print(stack.get_min())  # prints 3

    stack.pop()
    print(stack.get_min())  # prints 5

    stack.push(10)
    print(stack.get_min())  # prints 5

    stack.pop()
    print(stack.get_min())  # prints 5
