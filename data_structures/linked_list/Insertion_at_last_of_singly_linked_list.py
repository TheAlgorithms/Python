from typing import Any


class Node:
    def __init__(self, data: int, next:Any=None) -> None:
        """
        create and initialize Node class instance.
         >>> node(6)
         <__main__.node object at 0x7fce380fd730>(address of the node)
        """
        self.data = data
        self.next = next


def print_linked_list(head: Any) -> None:  # Print every node data
    """
    This function is intended for iterators to access
          and iterate through data inside linked list.
    The address of first of linked list is being passed
    in head
    >>> print_linked_list(head)
    >>> print_linked_list(head)
    >>> print_linked_list(head)
    1
    2
    3
    """
    while head:
        print(head.data)
        head = head.next


def insert_at_end_of_linkedlist(head: Any, data: int) -> Any:

    if not head:
        return Node(data)
    ptr = head
    while ptr.next:
        ptr = ptr.next
    ptr.next = Node(data)
    return head


def main() :
    from doctest import testmod
    a = Node(1, Node(2, Node(3, Node(4))))  # creation of a linked list

    insert_at_end_of_linkedlist(a, 5)  # function calling and passing the parameters

    print_linked_list(a)  # then calling the function for printing the elements


if __name__ == "__main__":
    main()
