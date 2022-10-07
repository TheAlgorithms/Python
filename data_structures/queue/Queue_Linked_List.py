#!/usr/bin/env python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class QueueLinkedList:
    def __init__(self):
        self._length = 0
        self.head = None

    def is_empty(self):
        return self._length == 0

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next_node:
                last = last.next_node
            # Append the new node
            last.next_node = node
        self._length += 1

    def remove(self):
        data = self.head.data
        self.head = self.head.next_node
        self._length -= 1
        return data

    def length(self):
        return self._length

qll = QueueLinkedList()
qll.insert(1)
qll.insert(2)
qll.insert(3)
qll.remove()
print("Length of QueueLinkedList: " + str(qll.length()))
print('QLL is Empty' if qll.is_empty() else 'QLL is NOT Empty')

# Output
# Length of QueueLinkedList: 2
# QLL is NOT Empty
#
