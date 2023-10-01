from __future__ import annotations

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


def print_linked_list(head: Node) -> None:
    """
    Print the entire linked list iteratively.

    Parameters:
        head (Node): The head of the linked list to be printed.
    
    >>> head = None
    >>> head = insert_node(head, 0)
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
    while head.next is not None:
        print(head.data, end="->")
        head = head.next
    print(head.data)


def insert_node(head: Node, data: int) -> Node:
    """
    Insert a new node at the end of a linked list and return the new head.

    Parameters:
        head (Node): The head of the linked list.
        data (int): The data to be inserted into the new node.

    Returns:
        Node: The new head of the linked list.

    >>> head = None
    >>> head = insert_node(head, 10)
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
    while temp_node.next is not None:
        temp_node = temp_node.next

    temp_node.next = new_node
    return head


def right_rotate_by_k(head: Node, k: int) -> Node:
    """
    Rotate a linked list to the right by k times.

    Parameters:
        head (Node): The head of the linked list.
        k (int): The number of places to rotate.

    Returns:
        Node: The head of the rotated linked list.

    >>> head = None
    >>> head = insert_node(head, 1)
    >>> head = insert_node(head, 2)
    >>> head = insert_node(head, 3)
    >>> head = insert_node(head, 4)
    >>> head = insert_node(head, 5)
    >>> k = 2
    >>> new_head = right_rotate_by_k(head, k)
    >>> print_linked_list(new_head)
    4->5->1->2->3
    """
    # Check if the list is empty or has only one element
    if head is None or head.next is None:
        return head

    # Calculate the length of the linked list
    length = 1
    temp_node = head
    while temp_node.next is not None:
        length += 1
        temp_node = temp_node.next

    # Adjust the value of k to avoid unnecessary rotations.
    k = k % length

    if k == 0:
        return head  #As No rotation needed.

    # Find the new head position after rotation.
    new_head_index = length - k

    # Traverse to the new head position
    temp_node = head
    for _ in range(new_head_index - 1):
        temp_node = temp_node.next

    # Update pointers to perform rotation
    new_head = temp_node.next
    temp_node.next = None
    temp_node = new_head
    while temp_node.next is not None:
        temp_node = temp_node.next
    temp_node.next = head

    return new_head

if __name__ == "__main__":
    import doctest 

    doctest.testmod()
    head = None

    head = insert_node(head, 5)
    head = insert_node(head, 1)
    head = insert_node(head, 2)
    head = insert_node(head, 4)
    head = insert_node(head, 3)

    print("Original list: ", end="")
    print_linked_list(head)

    k = 3
    new_head = right_rotate_by_k(head, k)

    print("After", k, "iterations: ", end="")
    print_linked_list(new_head)