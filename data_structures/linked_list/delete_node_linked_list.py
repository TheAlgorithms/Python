"""
Write a function to delete a node in a singly-linked list.
You will not be given access to the head of the list,
instead you will be given access to the node to be deleted directly.
"""


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


def make_linked_list(numbers: list = []) -> ListNode:
    """Creates a Linked List given a list of numbers, returns
    the head of the Linked List

    >>> make_linked_list([])
    Traceback (most recent call last):
        ...
    Exception: The Numbers List is empty
    >>> print(make_linked_list([1,2,3]).val)
    1
    >>> print(make_linked_list([0,2,15]).val)
    0
    """

    if not numbers:
        raise Exception("The Numbers List is empty")

    current = head = ListNode(numbers[0])

    for i in range(1, len(numbers)):
        current.next = ListNode(numbers[i])
        current = current.next
    return head


def print_linked_list(head: ListNode) -> None:
    """Prints a Linked List to the console
    >>> L = make_linked_list([0,25,6,4])
    >>> print_linked_list(L)
    0
    25
    6
    4
    """
    current = head
    while current is not None:
        print(current.val)
        current = current.next


def delete_node(node: ListNode) -> None:
    """Deletes a given node from a linked list
    without accessing the head of the linked list.


    >>> L = make_linked_list([1,2,3])
    >>> to_delete = L.next
    >>> delete_node(to_delete)
    >>> print_linked_list(L)
    1
    3
    """

    node.val = node.next.val
    node.next = node.next.next


if __name__ == "__main__":
    from doctest import testmod

    testmod()
