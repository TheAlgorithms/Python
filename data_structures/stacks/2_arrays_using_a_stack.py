class TwoArraysOneStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top1 = -1  # Top of the first array
        self.top2 = size  # Top of the second array

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.stack[self.top1] = data
        else:
            print("Stack Overflow")

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.stack[self.top2] = data
        else:
            print("Stack Overflow")

    def pop1(self):
        if self.top1 >= 0:
            data = self.stack[self.top1]
            self.top1 -= 1
            return data
        else:
            print("Stack 1 is empty")

    def pop2(self):
        if self.top2 < self.size:
            data = self.stack[self.top2]
            self.top2 += 1
            return data
        else:
            print("Stack 2 is empty")

# Example usage:
stack = TwoArraysOneStack(5)

stack.push1(1)
stack.push1(2)
stack.push2(3)
stack.push2(4)
stack.push2(5)

print("Popping from Stack 1:", stack.pop1())  # Outputs 2
print("Popping from Stack 2:", stack.pop2())  # Outputs 5
