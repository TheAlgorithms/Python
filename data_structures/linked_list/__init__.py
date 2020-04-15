class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
        self.size=0

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)
        self.size+=1

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size-=1
            return item

    def is_empty(self):
        return self.head is None
    def size(self):
        return self.size
