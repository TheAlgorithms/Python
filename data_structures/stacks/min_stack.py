"""
Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Operations:
1. push(x)   -> Push element x onto stack.
2. pop()     -> Removes the element on top of the stack.
3. top()     -> Get the top element.
4. getMin()  -> Retrieve the minimum element in the stack.

Example:
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    min_stack.getMin()  # returns -3
    min_stack.pop()
    min_stack.top()     # returns 0
    min_stack.getMin()  # returns -2

Time Complexity:
- push: O(1)
- pop: O(1)
- top: O(1)
- getMin: O(1)

Space Complexity:
- O(n) extra space for the min_stack
"""

class MinStack:
    def __init__(self):
        """
        Initialize two stacks:
        - main_stack: stores all elements
        - min_stack: stores the current minimum element at each level
        """
        self.main_stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.

        Args:
        x (int): Element to push
        """
        self.main_stack.append(x)
        # Push to min_stack if it's empty or x is <= current minimum
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        """
        if self.main_stack:
            val = self.main_stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack.

        Returns:
        int: Top element if stack is not empty, else None
        """
        return self.main_stack[-1] if self.main_stack else None

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.

        Returns:
        int: Minimum element if stack is not empty, else None
        """
        return self.min_stack[-1] if self.min_stack else None


# Example Usage
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print("Current Min:", min_stack.getMin())  # Output: -3
    min_stack.pop()
    print("Top Element:", min_stack.top())     # Output: 0
    print("Current Min:", min_stack.getMin())  # Output: -2
