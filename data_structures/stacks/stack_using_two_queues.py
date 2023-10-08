class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Create a stack
stack = Stack()

# PUSH operation
stack.push(1)
stack.push(2)
stack.push(3)

# Display the stack
print("Stack:", stack.items)

# POP operation
popped_item = stack.pop()
print("Popped item:", popped_item)

# Display the updated stack
print("Stack after POP:", stack.items)

# PEEK operation
top_item = stack.peek()
print("Top item (PEEK):", top_item)

# Check the size of the stack
stack_size = stack.size()
print("Stack size:", stack_size)
