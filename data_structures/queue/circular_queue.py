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
        """ This function Return bool value of cond. self.size == 0
        >>> obj.is_empty()
        True                    # Queue size >= 1
        >>> obj.is_empty()
        False                   # Queue size < 1
        """
        
        return self.size == 0

    def first(self):
        """
        This function return the first element in the queue
        >>> obj.first()   # Queue -> [10, None, None, None, None]
        10
        >>> obj.first()  
        None              # if queue is empty
        """
        
        if self.is_empty():
            return False
        return self.array[self.front]

    def enqueue(self, data):
        """ 
        This function insert an element(data) at the end of the queue
        >>> obj.enqueue(5)
        return memory location of Class obj.
        >>> obj.array
        [5, None, None, None, None]

        # if Queue is full -> [5, 10, 15, 20, 25]
        >>> obj.enqueue(30)
        raise Exception
        """
        
        if self.size >= self.n:
            return False

        self.array[self.rear] = data
        self.rear = (self.rear+1)%self.n
        self.size += 1
        return self

    def dequeue(self):
         """ This function removes the first element of the queue.
        Queue -> [5, None, None, None, None]
        >>> obj.dequeue()
        5

        # if Queue size is equal to 0
        >>> obj.dequeue()
        raise Exception
        """
        
        if self.size == 0:
            return False

        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1)%self.n
        self.size -= 1
        return temp
