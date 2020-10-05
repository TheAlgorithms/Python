# Program to print the elements of a linked list in reverse

from typing import List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        """Returns a visual representation of the node and all its following nodes."""
        string_rep = ""
        temp = self
        while temp:
            string_rep += f"<{temp.data}> ---> "
            temp = temp.next
        string_rep += "<END>"
        return string_rep


def make_linked_list(elements_list: List):
    """Creates a Linked List from the elements of the given sequence
    (list/tuple) and returns the head of the Linked List."""
    """
    >>> make_linked_list()
    Traceback (most recent call last):
        ...
    Exception: The Elements List is empty
    >>> make_linked_list([])
    Traceback (most recent call last):
        ...
    Exception: The Elements List is empty
    >>> make_linked_list([7])
    '<7> ---> <END>'
    >>> make_linked_list(['abc'])
    '<abc> ---> <END>'
    >>> make_linked_list([7, 25])
    '<7> ---> <25> ---> <END>'
    """

    # if elements_list is empty
    if not elements_list:
        raise Exception("The Elements List is empty")

    # Set first element as Head
    head = Node(elements_list[0])
    current = head
    list_length = len(elements_list)

    # Iterate over values from generator expression starting from position 1
    for data in (elements_list[i] for i in range(1, list_length)):
        current.next = Node(data)
        current = current.next
    return head


def print_reverse(head_node: Node):
    """Prints the elements of the given Linked List in reverse order"""
    """
    >>> print_reverse()
    None
    >>> print_reverse([])
    None
    """

    # If reached end of the List
    if head_node is None or not isinstance(head_node, Node):
        return None
    else:
        # Recurse
        print_reverse(head_node.next)
        print(head_node.data)


list_data = [14, 52, 14, 12, 43]
linked_list = make_linked_list(list_data)
print("Linked List:")
print(linked_list)
print("Elements in Reverse:")
print_reverse(linked_list)
