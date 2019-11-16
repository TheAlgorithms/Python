# Implementation of Circular Queue (using python lists)

class CircularQueue:
    """ Circular queue with fixed capacity """

    def __init__(self, n):
        self.n = n
        self.array = [None]*self.n
        self.front = 0              # For first ele. Index
        self.rear = 0
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            return False
        return self.array[self.front]

    def enqueue(self, data):
        if self.size >= self.n:
            return False

        self.array[self.rear] = data
        self.rear = (self.rear+1)%self.n
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            return False

        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1)%self.n
        self.size -= 1
        return temp
