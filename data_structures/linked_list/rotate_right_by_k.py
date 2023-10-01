from __future__ import annotations

import doctest


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


def print_list(head: Node) -> None:
    """
    Prints the entire linked list iteratively
    >>> head = None
    >>> head = insert_node(head, 1)
    >>> head = insert_node(head, 2)
    >>> head = insert_node(head, 3)
    >>> print_list(head)
    1->2->3
    >>> head = insert_node(head, 4)
    >>> head = insert_node(head, 5)
    >>> print_list(head)
    1->2->3->4->5
    """
    while head.next is not None:
        print(head.data, end="->")
        head = head.next
    print(head.data)


def insert_node(head: Node | None, data: int) -> Node:
    """
    Returns new head of linked list after inserting new node
    >>> head = None
    >>> head = insert_node(head, 1)
    >>> head = insert_node(head, 2)
    >>> head = insert_node(head, 3)
    >>> print_list(head)
    1->2->3
    """
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    temp_node = head
    while temp_node.next is not None:
        temp_node = temp_node.next
    temp_node.next = new_node
    return head


def right_rotate_by_k(head: Node, k_places: int) -> Node:
    """
    This function receives head and k as input
    parameters and returns head of linked list
    after rotation to the right by k places
    >>> head = None
    >>> head = insert_node(head, 1)
    >>> head = insert_node(head, 2)
    >>> head = insert_node(head, 3)
    >>> head = insert_node(head, 4)
    >>> head = insert_node(head, 5)
    >>> k = 2
    >>> new_head = right_rotate_by_k(head, k)
    >>> print_list(new_head)
    4->5->1->2->3
    """
    if head is None or head.next is None:
        return head
    for _ in range(k_places):
        temp_node = head
        while temp_node.next.next is not None:
            temp_node = temp_node.next
        end = temp_node.next
        temp_node.next = None
        end.next = head
        head = end
    return head


if __name__ == "__main__":
    doctest.testmod()
    head = None

    head = insert_node(head, 1)
    head = insert_node(head, 2)
    head = insert_node(head, 3)
    head = insert_node(head, 4)
    head = insert_node(head, 5)

    print("Original list: ", end="")
    print_list(head)

    k = 2
    new_head = right_rotate_by_k(head, k)

    print("After", k, "iterations: ", end="")
    print_list(new_head)
