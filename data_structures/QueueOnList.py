"""Queue represented by a python list"""
class Queue():
    def __init__(self):
        self.entries = []
        self.length = 0

    """Enqueues {@code item}
    @param item
        item to enqueue"""
    def put(self, item):
        self.entries.append(item)
        self.length = self.length + 1
        print(self.entries)

    """Dequeues {@code item}
    @requirement: |self.length| > 0
    @return dequeued
        item that was dequeued"""
    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[0]
        self.entries = self.entries[1:]
        return dequeued

    """Enqueues {@code item}
    @return item at front of self.entries"""
    def front(self):
        return self.entries[0]

    """Returns the length of this.entries"""
    def size(self):
        return self.length



