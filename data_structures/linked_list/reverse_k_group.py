from __future__ import annotations

from dataclasses import dataclass

@dataclass
class ListNode:
    data: int
    next_node: ListNode | None = None

def print_linked_list(head: ListNode | None) -> None:
    """
    Print the entire linked list iteratively.

    This function prints the elements of a linked list separated by '->'.

    Parameters:
        head (ListNode | None): The head of the linked list to be printed,
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

def insert_node(head: ListNode | None, data: int) -> ListNode:
    """
    Insert a new node at the end of a linked list and return the new head.

    Parameters:
        head: The head of the linked list.
        data: The data to be inserted into the new node.

    Returns:
        The new head of the linked list.

    >>> head = insert_node(None, 10)
    >>> head = insert_node(head, 9)
    >>> head = insert_node(head, 8)
    >>> print_linked_list(head)
    10->9->8
    """
    new_node = ListNode(data)
    if head is None:
        return new_node

    temp_node = head
    while temp_node.next_node:
        temp_node = temp_node.next_node

    temp_node.next_node = new_node
    return head

class Solution:
    def reverse_k_group(self, head: ListNode | None, k: int) -> ListNode | None:
        """
        Reverse k-sized groups of nodes in a linked list.

        Parameters:
            head: The head of the linked list.
            k: The size of each group to reverse.

        Returns:
            The head of the reversed linked list.

        >>> head = insert_node(None, 1)
        >>> head = insert_node(head, 2)
        >>> head = insert_node(head, 3)
        >>> head = insert_node(head, 4)
        >>> head = insert_node(head, 5)
        >>> head = insert_node(head, 6)
        >>> solution = Solution()
        >>> new_head = solution.reverse_k_group(head, 2)
        >>> print_linked_list(new_head)
        2->1->4->3->6->5
        """
        def reverse_group(head: ListNode | None, k: int) -> tuple:
            prev_group_tail = None
            nodes_left = k
            current_group_head = head

            while current_group_head:
                current_group_head = current_group_head.next_node
                nodes_left -= 1

            if nodes_left > 0:
                return head, None, None, False

            current_tail = head

            while head and k > 0:
                k -= 1
                next_node = head.next_node
                head.next_node = prev_group_tail
                prev_group_tail = head
                head = next_node

            return prev_group_tail, current_tail, head, True

        new_head, current_tail, next_group_head, success = reverse_group(head, k)

        while success:
            new_group_head, new_group_tail, next_next_group_head, success = reverse_group(next_group_head, k)
            current_tail.next_node = new_group_head
            current_tail = new_group_tail
            next_group_head = next_next_group_head

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

    k = 3
    solution = Solution()
    new_head = solution.reverse_k_group(head, k)

    print(f"After reversing groups of size {k}: ", end="")
    print_linked_list(new_head)
