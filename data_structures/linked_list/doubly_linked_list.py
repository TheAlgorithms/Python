"""
- A linked list is similar to an array, it holds values. However, links in a linked
    list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous
    pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - It can be traversed in both forward and backward direction.
     Delete operation is more efficient"""


class LinkedList:
    """
    >>> linked_list = LinkedList()
    >>> linked_list.insert_at_head("a")
    >>> linked_list.insert_at_tail("b")
    >>> linked_list.delete_tail()
    'b'
    >>> linked_list.is_empty
    False
    >>> linked_list.delete_head()
    'a'
    >>> linked_list.is_empty
    True
    """

    def __init__(self):
        self.head = None  # First node in list
        self.tail = None  # Last node in list

    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current)
            current = current.next
        return " ".join(str(node) for node in nodes)

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def delete_head(self) -> str:
        if self.is_empty:
            return "List is empty"

        head_data = self.head.data
        if self.head.next:
            self.head = self.head.next
            self.head.previous = None

        else:  # If there is no next previous node
            self.head = None
            self.tail = None

        return head_data

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def delete_tail(self) -> str:
        if self.is_empty:
            return "List is empty"

        tail_data = self.tail.data
        if self.tail.previous:
            self.tail = self.tail.previous
            self.tail.next = None
        else:  # if there is no previous node
            self.head = None
            self.tail = None

        return tail_data

    def delete(self, data) -> str:
        current = self.head

        while current.data != data:  # Find the position to delete
            if current.next:
                current = current.next
            else:  # We have reached the end an no value matches
                return "No data matching given value"

        if current == self.head:
            self.delete_head()

        elif current == self.tail:
            self.delete_tail()

        else:  # Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next  # 1 --> 3
            current.next.previous = current.previous  # 1 <--> 3
        return data

    @property
    def is_empty(self):  # return True if the list is empty
        return self.head is None


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return f"{self.data}"
