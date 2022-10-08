from typing import Any


class Node:
    def __init__(self, data:int, next=None) -> None:
        """
        create and initialize Node class instance.
         >>> node(6)
         <__main__.node object at 0x7fce380fd730>(address of the node)
        """
        self.data = data
        self.next = next


def print_linked_list(head: Any) -> None: # Print every node data
    """
    This function is intended for iterators to access
          and iterate through data inside linked list.
    The address of first of linked list is being passed
    in head
    >>> print_linked_list(head)
    >>> print_linked_list(head)
    >>> print_linked_list(head)
    head.data
    head.data
    head.data
    .
    .
    .
    >>>

    """
    while head:
        print(head.data)
        head = head.next


def insert_at_end_of_linkedlist(head:Any, data:int):
    """
    This method inserts data at the end of the linked list
    First it checks if there is any pre-existing node or not
    then it head pointer will move iterates over the linked list.
    it will search for Null/None after that the next of head will
    Be given a node with data and Noneas address
    >>> insert_at_end_of_linkedlist =insert_at_end_of_linkedlist(head,5)
        1
        2
        3
        4
        5
    """
    if not head:
        return Node(data)
    ptr = head
    while ptr.next:
        ptr = ptr.next
    ptr.next = Node(data)
    return head


def main() -> None:
    a = Node(1, Node(2, Node(3, Node(4))))  # creation of a linked list

    insert_at_end_of_linkedlist(a, 5)  # function calling and passing the parameters

    print_linked_list(a)  # then calling the function for printing the elements


if __name__ == "__main__":
    main()
