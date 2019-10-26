class CircularQueue:

    #Constructor
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 8

    #Adding elements to the queue
    def enqueue(self,data):
        """
        Insert the element in the Queue
        >>> CQ=CircularQueue()
        >>> CQ.enqueue(5)
        True
        >>> CQ.size()
        1
        """
        if self.size() == self.maxSize-1:
            return ("Queue Full!")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True

    #Removing elements from the queue
    def dequeue(self):
        """
        Delete the element from the Queue
        >>> CQ=CircularQueue()
        >>> CQ.enqueue(5)
        True
        >>> CQ.dequeue()
        5
        >>> CQ.size()
        0
        """
        if self.size()==0:
            return ("Queue Empty!")
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

    #Calculating the size of the queue
    def size(self):
        """
        >>> CQ=CircularQueue()
        >>> CQ.enqueue(5)
        True
        >>> CQ.size()
        1
        """
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))

q = CircularQueue()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(7))
print(q.enqueue(8))
print(q.enqueue(9))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
