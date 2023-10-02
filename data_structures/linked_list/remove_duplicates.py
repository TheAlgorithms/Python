from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next_node: Node | None = None


def print_linked_list(head: Node | None) -> None:
    """
    Print the entire linked list iteratively.

    >>> head = insert_node(None, 0)
    >>> head = insert_node(head, 2)
    >>> head = insert_node(head, 1)
    >>> print_linked_list(head)
    0->2->1
    >>> head = insert_node(head, 4)
    >>> head = insert_node(head, 5)
    >>> print_linked_list(head)
    0->2->1->4->5
    """
    if head is None:
        return
    while head.next_node is not None:
        print(head.data, end="->")
        head = head.next_node
    print(head.data)


def insert_node(head: Node | None, data: int) -> Node | None:
    """
    Insert a new node at the end of a linked list
    and return the new head.

    >>> head = insert_node(None, 10)
    >>> head = insert_node(head, 9)
    >>> head = insert_node(head, 8)
    >>> print_linked_list(head)
    10->9->8
    """
    new_node = Node(data)
    if head is None:
        return new_node

    temp_node = head
    while temp_node.next_node:
        temp_node = temp_node.next_node
    temp_node.next_node = new_node
    return head


def remove_duplicates(head: Node | None) -> Node | None:
    """
    Remove nodes with duplicate data

    >>> head=insert_node(None,1)
    >>> head=insert_node(head,1)
    >>> head=insert_node(head,2)
    >>> head=insert_node(head,3)
    >>> head=insert_node(head,3)
    >>> head=insert_node(head,4)
    >>> head=insert_node(head,5)
    >>> head=insert_node(head,5)
    >>> head=insert_node(head,5)
    >>> new_head= remove_duplicates(head)
    >>> print_linked_list(new_head)
    1->2->3->4->5
    """
    if head is None or head.next_node is None:
        return head

    has_occurred = {}

    new_head = head
    last_node = head
    has_occurred[head.data] = True
    current_node = None
    if head.next_node:
        current_node = head.next_node
    while current_node is not None:
        if current_node.data not in has_occurred:
            last_node.next_node = current_node
            last_node = current_node
            has_occurred[current_node.data] = True
        current_node = current_node.next_node
    last_node.next_node = None
    return new_head


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    head = insert_node(None, 1)
    head = insert_node(head, 1)
    head = insert_node(head, 2)
    head = insert_node(head, 3)
    head = insert_node(head, 3)
    head = insert_node(head, 4)
    head = insert_node(head, 5)
    head = insert_node(head, 5)

    new_head = remove_duplicates(head)
    print_linked_list(new_head)
