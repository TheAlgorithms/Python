"""
Given two numbers represented by linked lists, where each node
contains a single digit, write a function that adds the two
numbers and returns the sum as a linked list. The digits are
stored in reverse order, meaning the 1's digit is at the
head of the list.
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

    >>> head = create_linked_list([2, 4, 3])
    >>> (head.value, head.next_node.value, head.next_node.next_node.value)
    (2, 4, 3)
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

    >>> head = ListNode(2)
    >>> head.next_node = ListNode(4)
    >>> head.next_node.next_node = ListNode(3)
    >>> linked_list_to_list(head)
    [2, 4, 3]
    >>> linked_list_to_list(None)
    []
    """
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next_node
    return values


def sum_linked_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    Adds two numbers represented by linked lists and returns the sum as a linked list.

    Args:
        l1: The head of the first linked list.
        l2: The head of the second linked list.
    Returns:
        The head of the linked list representing the sum of the two numbers.
    >>> l1 = create_linked_list([2, 4, 3])  # Represents the number 342
    >>> l2 = create_linked_list([5, 6, 4])  # Represents the number 465
    >>> linked_list_to_list(sum_linked_lists(l1, l2))  # Represents the number 807
    [7, 0, 8]
    >>> l1 = create_linked_list([0])  # Represents the number 0
    >>> l2 = create_linked_list([0])  # Represents the number 0
    >>> linked_list_to_list(sum_linked_lists(l1, l2))  # Represents the number 0
    [0]
    >>> l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])  # Represents the number 9999999
    >>> l2 = create_linked_list([9, 9, 9, 9])  # Represents the number 9999
    >>> linked_list_to_list(sum_linked_lists(l1, l2))  # Represents the number 10009998
    [8, 9, 9, 9, 0, 0, 0, 1]
    """
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next_node = ListNode(total % 10)
        current = current.next_node

        if l1:
            l1 = l1.next_node
        if l2:
            l2 = l2.next_node

    return dummy_head.next_node
