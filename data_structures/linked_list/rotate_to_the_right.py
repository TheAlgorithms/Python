from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next_node: Node | None = None


def print_linked_list(head: Node | None) -> None:
    """
        Print the entire linked list iteratively.

        This function prints the elements of a linked list separated by '->'.

        Parameters:
            head (Node | None): The head of the linked list to be printed,
    or None if the linked list is empty.

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


def insert_node(head: Node | None, data: int) -> Node:
    """
    Insert a new node at the end of a linked list and return the new head.

    Parameters:
        head (Node | None): The head of the linked list.
        data (int): The data to be inserted into the new node.

    Returns:
        Node: The new head of the linked list.

    >>> head = insert_node(None, 10)
    >>> head = insert_node(head, 9)
    >>> head = insert_node(head, 8)
    >>> print_linked_list(head)
    10->9->8
    """
    new_node = Node(data)
    # If the linked list is empty, the new_node becomes the head
    if head is None:
        return new_node

    temp_node = head
    while temp_node.next_node:
        temp_node = temp_node.next_node

    temp_node.next_node = new_node  # type: ignore
    return head


def rotate_to_the_right(head: Node, places: int) -> Node:
    """
    Rotate a linked list to the right by places times.

    Parameters:
        head: The head of the linked list.
        places: The number of places to rotate.

    Returns:
        Node: The head of the rotated linked list.

    >>> rotate_to_the_right(None, places=1)
    Traceback (most recent call last):
        ...
    ValueError: The linked list is empty.
    >>> head = insert_node(None, 1)
    >>> rotate_to_the_right(head, places=1) == head
    True
    >>> head = insert_node(None, 1)
    >>> head = insert_node(head, 2)
    >>> head = insert_node(head, 3)
    >>> head = insert_node(head, 4)
    >>> head = insert_node(head, 5)
    >>> new_head = rotate_to_the_right(head, places=2)
    >>> print_linked_list(new_head)
    4->5->1->2->3
    """
    # Check if the list is empty or has only one element
    if not head:
        raise ValueError("The linked list is empty.")

    if head.next_node is None:
        return head

    # Calculate the length of the linked list
    length = 1
    temp_node = head
    while temp_node.next_node is not None:
        length += 1
        temp_node = temp_node.next_node

    # Adjust the value of places to avoid places longer than the list.
    places %= length

    if places == 0:
        return head  # As no rotation is needed.

    # Find the new head position after rotation.
    new_head_index = length - places

    # Traverse to the new head position
    temp_node = head
    for _ in range(new_head_index - 1):
        assert temp_node.next_node
        temp_node = temp_node.next_node

    # Update pointers to perform rotation
    assert temp_node.next_node
    new_head = temp_node.next_node
    temp_node.next_node = None
    temp_node = new_head
    while temp_node.next_node:
        temp_node = temp_node.next_node
    temp_node.next_node = head

    assert new_head
    return new_head


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    head = insert_node(None, 5)
    head = insert_node(head, 1)
    head = insert_node(head, 2)
    head = insert_node(head, 4)
    head = insert_node(head, 3)

    print("Original list: ", end="")
    print_linked_list(head)

    places = 3
    new_head = rotate_to_the_right(head, places)

    print(f"After {places} iterations: ", end="")
    print_linked_list(new_head)
