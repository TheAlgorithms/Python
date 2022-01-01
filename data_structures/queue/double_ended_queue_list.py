'''
Implementation of double ended queue using list.
'''
from typing import Any

class Dequeue:
    def __init__(self) -> None:
        self.queue = []     
        self.size = 0       

    def enqueueFront(self, val: Any) -> None:
        '''
        Adds value to front of dequeue
        Time Complexity: O(1)
        
        '''
        self.queue.insert(0, val)
        self.size += 1

    def enqueueEnd(self, val: Any) -> None:
        self.queue.append(val)
        self.size += 1

    def dequeueFront(self) -> None:
        if self.size == 0:
            print('dql empty')
            return
        self.queue = self.queue[1:]
        self.size -= 1

    def dequeueEnd(self) -> None:
        if self.size == 0:
            print('dql empty')
            return
        self.queue = self.queue[:-1]
        self.size -= 1

    def printQueue(self) -> None:
        print(*self.queue, sep=' ')

    def queueSize(self) -> int:
        return self.size


if __name__ == "__main__":
    import doctest
    doctest.testmod()
