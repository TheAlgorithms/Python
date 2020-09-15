"""
Pure Python implementation of Priority Queue using lists
"""


class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class OverFlow(Error):
    def __init__(self, msg):
        self.msg = msg


class UnderFlow(Error):
    def __init__(self, msg):
        self.msg = msg


class FixedPriorityQueue:
    """
    In a Priority Queue the elements are entred as an when the come
    But while removing or deleting an element the highest priority element is deleted
    in FIFO fashion.
    Here the lowest integer has the highest priority.
    Example:
    priority(0) > priority(5)
    priority(16) > priority(32)
    Here as an example I have taken only 3 priorities viz. 0, 1, 2
    0 Being the highest priority and 2 being the lowest
    You can change the priorities as per your need

    Examples
    >>> FPQ = FixedPriorityQueue()
    >>> FPQ.enqueue(0, 10)
    >>> FPQ.enqueue(1, 70)
    >>> FPQ.enqueue(0, 100)
    >>> FPQ.enqueue(2, 1)
    >>> FPQ.enqueue(2, 5)
    >>> FPQ.enqueue(1, 7)
    >>> FPQ.enqueue(2, 4)
    >>> FPQ.enqueue(1, 64)
    >>> FPQ.enqueue(0, 128)
    >>> FPQ.print_queue()
    Priority 0: [10, 100, 128]
    Priority 1: [70, 7, 64]
    Priority 2: [1, 5, 4]
    >>> FPQ.dequeue()
    10
    >>> FPQ.dequeue()
    100
    >>> FPQ.dequeue()
    128
    >>> FPQ.dequeue()
    70
    >>> FPQ.dequeue()
    7
    >>> FPQ.print_queue()
    Priority 0: []
    Priority 1: [64]
    Priority 2: [1, 5, 4]
    >>> FPQ.dequeue()
    64
    >>> FPQ.dequeue()
    1
    >>> FPQ.dequeue()
    5
    >>> FPQ.dequeue()
    4
    >>> FPQ.dequeue()
    Traceback (most recent call last):
                    ...
    Exception: Under Flow!
    """

    def __init__(self):
        self.queue = [
            [],
            [],
            [],
        ]

    def enqueue(self, priority, data):
        """
        This function enters the element into the queue based on its priority
        If the priority is invalid an Exception is raised saying Invalid Priority!
        If the queue is full an Exception is raised saying Over Flow!
        """
        if priority > 2:
            raise Exception("Invalid Priority!")
        elif len(self.queue[priority]) == 100:
            raise OverFlow("Over Flow!")
        else:
            self.queue[priority].append(data)

    def dequeue(self):
        """
        Return the highest priority element in FIFO order.
        If the queue is empty then an under flow exception is raised.
        """
        if not self.queue[0] and not self.queue[1] and not self.queue[2]:
            raise UnderFlow("Under Flow!")

        if len(self.queue[0]) != 0:
            return self.queue[0].pop(0)
        elif len(self.queue[1]) != 0:
            return self.queue[1].pop(0)
        else:
            return self.queue[2].pop(0)

    def print_queue(self):
        print("Priority 0:", self.queue[0])
        print("Priority 1:", self.queue[1])
        print("Priority 2:", self.queue[2])

    def __str__(self):
        """
        Prints each priority queue within the FixedPriorityQueue
        """
        s = ""
        for i in range(len(self.queue)):
            for j in self.queue[i]:
                s += "Priority " + str(i) + ": "
                s += str(i) + " "
            s += "\n"
        print(s)
        return s


class ElementPriorityQueue:
    """
    Element Priority Queue is the same as Fixed Priority Queue
    The only difference being the value of the element itself is the priority
    The rule for priorities are the same
    The lowest integer has the highest priority.
    Example:
    priority(0) > priority(5)
    priority(16) > priority(32)
    You can change the priorities as per your need

    >>> EPQ = ElementPriorityQueue()
    >>> EPQ.enqueue(10)
    >>> EPQ.enqueue(70)
    >>> EPQ.enqueue(100)
    >>> EPQ.enqueue(1)
    >>> EPQ.enqueue(5)
    >>> EPQ.enqueue(7)
    >>> EPQ.enqueue(4)
    >>> EPQ.enqueue(64)
    >>> EPQ.enqueue(128)
    >>> EPQ.print_queue()
    [10, 70, 100, 1, 5, 7, 4, 64, 128]
    >>> EPQ.dequeue()
    1
    >>> EPQ.dequeue()
    4
    >>> EPQ.dequeue()
    5
    >>> EPQ.dequeue()
    7
    >>> EPQ.dequeue()
    10
    >>> EPQ.print_queue()
    [70, 100, 64, 128]
    >>> EPQ.dequeue()
    64
    >>> EPQ.dequeue()
    70
    >>> EPQ.dequeue()
    100
    >>> EPQ.dequeue()
    128
    >>> EPQ.dequeue()
    Traceback (most recent call last):
                    ...
    Exception: Under Flow!
    """

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        """
        This function enters the element into the queue
        If the queue is full an Exception is raised saying Over Flow!
        """
        if len(self.queue) == 100:
            raise OverFlow("Over Flow!")
        else:
            self.queue.append(data)

    def dequeue(self):
        """
        Return the highest priority element in FIFO order.
        If the queue is empty then an under flow exception is raised.
        """
        if len(self.queue) == 0:
            raise UnderFlow("Under Flow!")
        else:
            data = min(self.queue)
            self.queue.remove(data)
            return data

    def print_queue(self):
        print(self.queue)

    def __str__(self):
        """
        Prints all the elements within the Element Priority Queue
        """
        s = ""
        for i in self.queue:
            s += str(i) + " "
        return s


def fixed_priority_queue():
    FPQ = FixedPriorityQueue()
    FPQ.enqueue(0, 10)
    FPQ.enqueue(1, 70)
    FPQ.enqueue(0, 100)
    FPQ.enqueue(2, 1)
    FPQ.enqueue(2, 5)
    FPQ.enqueue(1, 7)
    FPQ.enqueue(2, 4)
    FPQ.enqueue(1, 64)
    FPQ.enqueue(0, 128)
    str(FPQ)
    print(FPQ.dequeue())
    print(FPQ.dequeue())
    print(FPQ.dequeue())
    print(FPQ.dequeue())
    print(FPQ.dequeue())
    str(FPQ)
    print(FPQ.dequeue())
    print(FPQ.dequeue())
    print(FPQ.dequeue())
    print(FPQ.dequeue())
    print(FPQ.dequeue())


def element_priority_queue():
    EPQ = ElementPriorityQueue()
    EPQ.enqueue(10)
    EPQ.enqueue(70)
    EPQ.enqueue(100)
    EPQ.enqueue(1)
    EPQ.enqueue(5)
    EPQ.enqueue(7)
    EPQ.enqueue(4)
    EPQ.enqueue(64)
    EPQ.enqueue(128)
    str(EPQ)
    print(EPQ)
    print(EPQ.dequeue())
    print(EPQ.dequeue())
    print(EPQ.dequeue())
    print(EPQ.dequeue())
    print(EPQ.dequeue())
    str(EPQ)
    print(EPQ)
    print(EPQ.dequeue())
    print(EPQ.dequeue())
    print(EPQ.dequeue())
    print(EPQ.dequeue())
    print(EPQ.dequeue())


if __name__ == "__main__":
    fixed_priority_queue()
    element_priority_queue()
