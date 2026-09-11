from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(order=True)
class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the linked list.
    """

    data: int
    next: Node | None = None


def iter_linked_list(head: Node | None) -> Iterable[Node]:
    """
    Iterate over the nodes of a linked list.

    Parameters:
        head: The head node of the linked list.

    Yields:
        Each node in the linked list, one by one.

    Example:
    >>> head = Node(3, Node(1, Node(2)))
    >>> head  # dataclasses provide a nice .__repr__().
    Node(data=3, next=Node(data=1, next=Node(data=2, next=None)))
    >>> tuple(iter_linked_list(head))
    (3, 1, 2)
    """
    current = head
    while current:
        yield current.data
        current = current.next


def get_middle(head: Node | None) -> Node | None:
    """
    Find the node before the middle of the linked list
    using the slow and fast pointer technique.

    Parameters:
        head: The head node of the linked list.

    Returns:
        The node before the middle of the linked list,
        or None if the list has fewer than 2 nodes.

    Example:
    >>> head = Node(1)
    >>> head.next = Node(2)
    >>> head.next.next = Node(3)
    >>> middle = get_middle(head)
    >>> middle.data
    2
    """
    if head is None or head.next is None:
        return None

    slow: Node | None = head
    fast: Node | None = head.next

    while fast is not None and fast.next is not None:
        if slow is None:
            return None
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left: Node | None, right: Node | None) -> Node | None:
    """
    Merge two sorted linked lists into one sorted linked list.

    Parameters:
        left: The head of the first sorted linked list.
        right: The head of the second sorted linked list.

    Returns:
        The head of the merged sorted linked list.

    Example:
    >>> left = Node(1)
    >>> left.next = Node(3)
    >>> tuple(iter_linked_list(left))
    (1, 3)
    >>> right = Node(2)
    >>> right.next = Node(4)
    >>> tuple(iter_linked_list(right))
    (2, 4)
    >>> merged = merge(left, right)
    >>> tuple(iter_linked_list(merged))
    (1, 2, 3, 4)
    """

    if left is None:
        return right
    if right is None:
        return left

    if left <= right:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result


def merge_sort_linked_list(head: Node | None) -> Node | None:
    """
    Sort a linked list using the Merge Sort algorithm.

    Parameters:
        head: The head node of the linked list to be sorted.

    Returns:
        The head node of the sorted linked list.

    Example:
    >>> head = Node(4)
    >>> head.next = Node(2)
    >>> head.next.next = Node(1)
    >>> head.next.next.next = Node(3)
    >>> tuple(iter_linked_list(head))
    (4, 2, 1, 3)
    >>> sorted_head = merge_sort_linked_list(head)
    >>> tuple(iter_linked_list(sorted_head))
    (1, 2, 3, 4)
    """

    # Base Case: 0 or 1 node
    if head is None or head.next is None:
        return head

    # Split the linked list into two halves
    middle = get_middle(head)
    if middle is None or middle.next is None:
        return head

    next_to_middle = middle.next
    middle.next = None  # Split the list into two parts

    # Recursively sort both halves
    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    # Merge sorted halves
    return merge(left, right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
