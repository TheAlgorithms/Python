"""
https://www.enjoyalgorithms.com/blog/reverse-linked-list
"""

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverse a singly linked list.

    Args:
        head: The head node of the linked list.

    Returns:
        The new head node of the reversed linked list.

    Examples:
        >>> a = ListNode(1)
        >>> b = ListNode(2)
        >>> c = ListNode(3)
        >>> a.next, b.next = b, c
        >>> head = reverse_linked_list(a)
        >>> [head.val, head.next.val, head.next.next.val]
        [3, 2, 1]
    """
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Example execution
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next, b.next = b, c

    print("Original Linked List: 1 -> 2 -> 3")
    new_head = reverse_linked_list(a)
    print(f"Reversed Linked List: {new_head.val} -> {new_head.next.val} -> {new_head.next.next.val}")
