"""
Recursive Program to create a Linked List from a sequence and
print a string representation of it.
"""


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


def make_linked_list(elements_list: list | tuple) -> Node:
    """
    Creates a Linked List from the elements of the given sequence
    (list/tuple) and returns the head of the Linked List.

    >>> make_linked_list([])
    Traceback (most recent call last):
        ...
    ValueError: The Elements List is empty
    >>> make_linked_list(())
    Traceback (most recent call last):
        ...
    ValueError: The Elements List is empty
    >>> make_linked_list([1])
    <1> ---> <END>
    >>> make_linked_list((1,))
    <1> ---> <END>
    >>> make_linked_list([1, 3, 5, 32, 44, 12, 43])
    <1> ---> <3> ---> <5> ---> <32> ---> <44> ---> <12> ---> <43> ---> <END>
    >>> make_linked_list((1, 3, 5, 32, 44, 12, 43))
    <1> ---> <3> ---> <5> ---> <32> ---> <44> ---> <12> ---> <43> ---> <END>
    """

    # if elements_list is empty
    if not elements_list:
        raise ValueError("The Elements List is empty")

    # Set first element as Head
    head = Node(elements_list[0])
    current = head
    # Loop through elements from position 1
    for data in elements_list[1:]:
        current.next = Node(data)
        current = current.next
    return head
