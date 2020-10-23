class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item

    def is_empty(self):
        return self.head is None

    def __len__(self):
        """
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.add("a")
        >>> len(linked_list)
        1
        >>> linked_list.add("b")
        >>> len(linked_list)
        2
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        1
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        0
        """
        return self.size
