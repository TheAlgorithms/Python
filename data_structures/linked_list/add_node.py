class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_ll(self):
        """
        Prints the elements of the linked list.

        If the linked list is empty, it prints "The Linked List is empty."

        Example:
        >>> linked_list = LinkedList()
        >>> linked_list.add_begin(11)
        >>> linked_list.add_end(100)
        >>> linked_list.add_begin(22)
        >>> linked_list.add_after(30, 11)
        >>> linked_list.print_ll()
        22
        11
        30
        100
        """
        if self.head is None:
            print("The Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data: int) -> None:
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data: int) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data: int, target_value: int) -> None:
        """
        Inserts a new node with the given 'data' after the first occurrence of 'target_value' in the linked list.

        Args:
            data (int): The data to be added to the new node.
            target_value (int): The value after which the new node will be added.

        Example:
        >>> linked_list = LinkedList()
        >>> linked_list.add_begin(11)
        >>> linked_list.add_end(100)
        >>> linked_list.add_begin(22)
        >>> linked_list.add_after(30, 11)
        >>> linked_list.print_ll()
        22
        11
        30
        100
        """
        n = self.head
        while n is not None:
            if target_value == n.data:
                break
            n = n.ref
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node


linked_list = LinkedList()
linked_list.add_begin(11)
linked_list.add_end(100)
linked_list.add_begin(22)
linked_list.add_after(30, 11)
linked_list.print_ll()
# https://youtu.be/xRTdfZsAz6Y?si=EMrqVJpXjDDz1kEF
