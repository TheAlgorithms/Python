class StackUsingQueues:
    def __init__(self) -> None:
        """
        Initializing the stack using two queues.

        >>> stack = StackUsingQueues()
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, item:int) -> None:
        """
        Push an item onto the stack.

        >>> stack = StackUsingQueues()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.peek()
        3
        """
        while len(self.queue1) != 0:
            self.queue2.append(self.queue1[0])
            self.queue1.pop(0)
        self.queue1.append(item)
        while len(self.queue2) != 0:
            self.queue1.append(self.queue2[0])
            self.queue2.pop(0)

    def pop(self) -> int:
        """
        Pop the top item from the stack and return it.

        >>> stack = StackUsingQueues()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        >>> stack.pop()
        1
        >>> stack.pop()
        0
        """
        if len(self.queue1) != 0:
            popped = self.queue1.pop(0)
            return popped
        else:
            return 0

    def peek(self) -> int:
        """
        Return the top item from the stack without removing it.

        >>> stack = StackUsingQueues()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.peek()
        2
        >>> stack.pop()
        2
        >>> stack.peek()
        1
        >>> stack.pop()
        1
        >>> stack.peek()
        0
        """
        if len(self.queue1) != 0:
            return self.queue1[0]
        else:
            return 0
