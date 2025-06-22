# Complete Python program demonstrating stack operations using a doubly linked list
from __future__ import annotations

class Node[T]:
    """Node class for doubly linked list"""
    def __init__(self, data: T):
        self.data = data  # Node data
        self.next: Node[T] | None = None  # Reference to next node
        self.prev: Node[T] | None = None  # Reference to previous node

class Stack[T]:
    """
    Stack implementation using doubly linked list
    
    >>> stack = Stack()
    >>> stack.is_empty()
    True
    >>> stack.print_stack()
    stack elements are:
    >>> for i in range(4):
    ...     stack.push(i)
    ...
    >>> stack.is_empty()
    False
    >>> stack.print_stack()
    stack elements are:
    3->2->1->0->
    >>> stack.top()
    3
    >>> len(stack)
    4
    >>> stack.pop()
    3
    >>> stack.print_stack()
    stack elements are:
    2->1->0->
    """

    def __init__(self) -> None:
        self.head: Node[T] | None = None  # Top of stack

    def push(self, data: T) -> None:
        """Push element onto stack"""
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            # Insert new node at head
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> T | None:
        """Pop element from top of stack"""
        if self.head is None:
            return None
            
        # Remove and return head node data
        temp = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None  # Clear prev reference for new head
        return temp

    def top(self) -> T | None:
        """Peek at top element without removing"""
        return self.head.data if self.head is not None else None

    def __len__(self) -> int:
        """Return number of elements in stack"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self) -> bool:
        """Check if stack is empty"""
        return self.head is None

    def print_stack(self) -> None:
        """Print all stack elements"""
        print("stack elements are:")
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next

# Program entry point
if __name__ == "__main__":
    stack: Stack[int] = Stack()  # Create integer stack

    print("Stack operations using Doubly LinkedList")
    # Push elements onto stack
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)

    stack.print_stack()  # Print current stack

    print("\nTop element is", stack.top())  # Show top element
    print("Size of stack is", len(stack))  # Show size

    # Pop two elements
    stack.pop()
    stack.pop()

    stack.print_stack()  # Print modified stack
    print("\nStack is empty:", stack.is_empty())  # Check emptiness
