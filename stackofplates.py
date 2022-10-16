# stack of plates


class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stack) > 0 and (len(self.stack[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stackes.append([item])

    def pop(self):
        if len(self.stack) and (len(self.stack[-1])) == 0:
            self.stack.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stacknumber):
        if len(self.stacks[stacknumber]) > 0:
            return self.stacks[stacknumber].pop()
        else:
            return None
