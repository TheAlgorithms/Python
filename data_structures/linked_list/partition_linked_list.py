"""
Partitions a linked list around a value x such that all nodes less than x come before
nodes greater than or equal to x. The original relative order of the nodes in each
partition should be preserved. The partition value x can appear anywhere in the "right
partition" and it does not need to appear between the left and right partitions.

Explanation from GeeksforGeeks: https://www.geeksforgeeks.org/dsa/partitioning-a-linked-list-around-a-given-value-and-keeping-the-original-order/
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListNode:
    value: int = 0
    next_node: ListNode | None = None


def create_linked_list(values: list[int]) -> ListNode | None:
    """
    Helper function to create a linked list from a list of values.

    >>> head = create_linked_list([1, 2, 3])
    >>> head.value
    1
    >>> head.next_node.value
    2
    >>> head.next_node.next_node.value
    3
    >>> create_linked_list([]) is None
    True
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next_node = ListNode(value)
        current = current.next_node
    return head


def linked_list_to_list(head: ListNode | None) -> list[int]:
    """
    Helper function to convert a linked list to a list of values.

    >>> head = ListNode(1)
    >>> head.next_node = ListNode(2)
    >>> head.next_node.next_node = ListNode(3)
    >>> linked_list_to_list(head)
    [1, 2, 3]
    >>> linked_list_to_list(None)
    []
    """
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next_node
    return values


def partition_linked_list(head: ListNode | None, x: int) -> ListNode | None:
    """
    Args:
        head: The head of the linked list.
        x: The partition value.

    Returns:
        The head of the partitioned linked list.

    Examples:
    >>> linked_list_to_list(
    ...     partition_linked_list(create_linked_list([1, 4, 3, 2, 5, 2]), 3)
    ... )
    [1, 2, 2, 4, 3, 5]
    >>> linked_list_to_list(
    ...     partition_linked_list(create_linked_list([1, 2, 3]), 10)
    ... )
    [1, 2, 3]
    >>> linked_list_to_list(
    ...     partition_linked_list(create_linked_list([5, 6, 7]), 3)
    ... )
    [5, 6, 7]
    >>> linked_list_to_list(
    ...     partition_linked_list(create_linked_list([3, 5, 8, 5, 10, 2, 1]), 5)
    ... )
    [3, 2, 1, 5, 8, 5, 10]
    >>> linked_list_to_list(
    ...     partition_linked_list(create_linked_list([1]), 5)
    ... )
    [1]
    >>> linked_list_to_list(partition_linked_list(None, 5))
    []
    """
    if head is None:
        return None

    if head.next_node is None:
        return head

    left_head = ListNode(0)  # Dummy head for the left partition
    right_head = ListNode(0)  # Dummy head for the right partition
    left = left_head
    right = right_head

    current: ListNode | None = head
    while current:
        if current.value < x:
            left.next_node = current
            left = current
        else:
            right.next_node = current
            right = current
        current = current.next_node

    right.next_node = None  # Terminate the right partition
    left.next_node = right_head.next_node  # Connect the two partitions

    return left_head.next_node  # Return the head of the new partitioned list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
