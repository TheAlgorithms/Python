# for explanation refer this  https://www.geeksforgeeks.org/implement-stack-using-queue/

class StackWithQueues:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, element):
        self.queue1.append(element)

    def pop(self):
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        element = self.queue1.pop(0)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return element

    def peek(self):
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        element = self.queue1[0]

        self.queue2.append(self.queue1.pop(0))

        self.queue1, self.queue2 = self.queue2, self.queue1

        return element

    """
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
    """


# Initialize the stack
stack = StackWithQueues()

while True:
    print("\nChoose operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Quit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        element = input("Enter element to push: ")
        stack.push(element)
        print(f"{element} pushed onto the stack.")
    elif choice == '2':
        popped_element = stack.pop()
        if popped_element is not None:
            print(f"Popped element: {popped_element}")
        else:
            print("Stack is empty.")
    elif choice == '3':
        peeked_element = stack.peek()
        if peeked_element is not None:
            print(f"Top element: {peeked_element}")
        else:
            print("Stack is empty.")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
