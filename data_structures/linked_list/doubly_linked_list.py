"""
- A linked list is similar to an array, it holds values. However, links in a linked
    list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous
    pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - It can be traversed in both forward and backward direction.
     Delete operation is more efficient
"""


class Node:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    """
    >>> linked_list = LinkedList()
    >>> linked_list.is_empty == True
    True
    >>> linked_list.insert(0)
    >>> linked_list.is_empty == False
    True
    >>> linked_list.delete_value(0)
    >>> linked_list.is_empty == True
    True
    """

    def __init__(self):
        self.head = None  # First node in list
        self.tail = None  # Last node in list

    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.data)
            current = current.next
        return "<-->".join(str(node) for node in nodes)

    def set_head(self, node: Node) -> None:

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insert_before_node(self.head, node)

    def set_tail(self, node: Node) -> None:
        if self.head is None:
            self.set_head(node)
        else:
            self.insert_after_node(self.tail, node)

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.set_head(node)
        else:
            self.set_tail(node)

    def insert_before_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.next = node
        node_to_insert.previous = node.previous

        if node.previous is None:
            self.head = node_to_insert
        else:
            node.previous.next = node_to_insert

        node.previous = node_to_insert

    def insert_after_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.previous = node
        node_to_insert.next = node.next

        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.previous = node_to_insert

        node.next = node_to_insert

    def insert_at_position(self, position: int, value: int) -> None:
        if position == 1:
            self.insert(value)
        current_position = 1
        new_node = Node(value)
        node = self.head
        while node:
            if current_position == position:
                self.insert_before_node(node, new_node)
                return None
            current_position += 1
            node = node.next
        self.insert_after_node(self.tail, new_node)

    def get_node(self, item):
        node = self.head
        while node:
            if node.data == item:
                return node
            node = node.next
        return None

    def delete_value(self, value):
        node = self.get_node(value)

        if node is not None:
            if node == self.head:
                self.head = self.head.next

            if node == self.tail:
                self.tail = self.tail.previous

            self.remove_node_pointers(node)

    @staticmethod
    def remove_node_pointers(node: Node) -> None:
        if node.next:
            node.next.previous = node.previous

        if node.previous:
            node.previous.next = node.next

        node.next = None
        node.previous = None


    @property
    def is_empty(self):  
        return self.head is None
