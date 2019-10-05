"""Queue represented by a python list"""


class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __str__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    """Enqueues {@code item}
    @param item
        item to enqueue"""

    def put(self, item):
        self.entries.append(item)
        self.length = self.length + 1

    """Dequeues {@code item}
    @requirement: |self.length| > 0
    @return dequeued
        item that was dequeued"""

    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        # self.front-=1
        # self.entries = self.entries[self.front:]
        self.entries = self.entries[1:]
        return dequeued

    """Rotates the queue {@code rotation} times
    @param rotation
        number of times to rotate queue"""

    def rotate(self, rotation):
        for i in range(rotation):
            self.put(self.get())

    """Enqueues {@code item}
    @return item at front of self.entries"""

    def front(self):
        return self.entries[0]

    """Returns the length of this.entries"""

    def size(self):
        return self.length
