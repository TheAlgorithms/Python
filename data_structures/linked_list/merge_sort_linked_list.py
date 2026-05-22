"""
Merge sort for a singly linked list.

https://en.wikipedia.org/wiki/Merge_sort
"""

from data_structures.linked_list.singly_linked_list import Node


def split_middle(node: Node) -> tuple[Node | None, Node | None]:
    """
    Find the middle node of a linked list using the fast/slow pointer method.

    Returns a tuple containing:
    - the node before the middle
    - the middle node
    """
    fast = slow = node
    previous: Node | None = None

    while fast and fast.next_node:
        fast = fast.next_node.next_node if fast.next_node else None
        previous = slow
        slow = slow.next_node

    return previous, slow


def sort_list(head: Node | None) -> Node | None:
    """
    Sort a linked list using merge sort.
    """
    if head is None:
        return head

    if head.next_node is None:
        return head

    previous, middle_node = split_middle(head)
    if previous:
        previous.next_node = None

    left = head
    right = middle_node

    left = sort_list(left)
    right = sort_list(right)

    dummy_head = current = Node(0)

    while left and right:
        if left.data < right.data:
            current.next_node = left
            left = left.next_node
        else:
            current.next_node = right
            right = right.next_node

        current = current.next_node

    while left:
        current.next_node = left
        next_node = left.next_node
        left.next_node = None
        left = next_node
        current = current.next_node

    while right:
        current.next_node = right
        next_node = right.next_node
        right.next_node = None
        right = next_node
        current = current.next_node

    return dummy_head.next_node
