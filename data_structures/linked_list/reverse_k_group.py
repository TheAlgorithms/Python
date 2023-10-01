from typing import Optional

class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next = None

class Solution:
    def reverse(self, head: Optional[ListNode], node_size: int) -> tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode], bool]:
        """
        Reverse the next k(node_size) nodes in a linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.
            node_size (int): The number of nodes to reverse.

        Returns:
            tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode], bool]: 
                - The new head of the reversed group.
                - The tail of the reversed group.
                - The new head after the reversed group.
                - A boolean indicating if there are more nodes to reverse.

        Example:
        >>> sol = Solution()
        >>> head = ListNode(1)
        >>> head.next = ListNode(2)
        >>> head.next.next = ListNode(3)
        >>> head.next.next.next = ListNode(4)
        >>> head.next.next.next.next = ListNode(5)
        >>> reversed_head, tail, new_head, found = sol.reverse(head, 2)
        >>> reversed_head.val
        2
        >>> tail.val
        1
        >>> new_head.val
        3
        >>> found
        True
        """
        prev_group_end = None
        remaining_count = node_size
        current_group_start = head

        # Calculate the remaining nodes in the list
        while current_group_start:
            current_group_start = current_group_start.next
            remaining_count -= 1

        # If there are less than k nodes remaining, return the original head
        if remaining_count > 0:
            return head, None, None, False

        current_group_end = head
        while head and node_size > 0:
            node_size -= 1
            next_node = head.next
            head.next = prev_group_end
            prev_group_end = head
            head = next_node

        return prev_group_end, current_group_end, head, True

    def reverse_k_group(self, head: Optional[ListNode], group_size: int) -> Optional[ListNode]:
        """
        Reverse nodes in a linked list in groups of k(group_size).

        Args:
            head (Optional[ListNode]): The head of the linked list.
            group_size (int): The number of nodes in each group to reverse.

        Returns:
            Optional[ListNode]: The new head of the reversed linked list.

        Example:
        >>> sol = Solution()
        >>> head = ListNode(1)
        >>> head.next = ListNode(2)
        >>> head.next.next = ListNode(3)
        >>> head.next.next.next = ListNode(4)
        >>> head.next.next.next.next = ListNode(5)
        >>> new_head = sol.reverse_k_group(head, 2)
        >>> new_head.val
        2
        >>> new_head.next.val
        1
        >>> new_head.next.next.val
        4
        >>> new_head.next.next.next.val
        3
        >>> new_head.next.next.next.next.val
        5
        """
        reversed_head, tail, new_head, found = self.reverse(head, group_size)

        while found:
            group_head, group_tail, new_head, found = self.reverse(new_head, group_size)
            tail.next = group_head
            tail = group_tail

        return reversed_head

if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
