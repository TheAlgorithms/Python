from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count

    def reverse(
        self, head: Optional[ListNode], count: int, k: int
    ) -> Optional[ListNode]:
        if count < k:
            return head

        prev = None
        count1 = 0
        curr = head
        Next = None
        while curr and count1 < k:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
            count1 += 1

        if Next:
            head.next = self.reverse(Next, count - k, k)

        return prev

    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse k-sized groups of nodes in a linked list.

        Args:
            head: The head of the linked list.
            k: The size of the groups to reverse.

        Returns:
            The new head of the reversed linked list.

        Examples:
        >>> sol = Solution()
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> new_head = sol.reverse_k_group(head, 2)
        >>> new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val, new_head.next.next.next.next.val
        (2, 1, 4, 3, 5)

        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> new_head = sol.reverse_k_group(head, 3)
        >>> new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val, new_head.next.next.next.next.val
        (3, 2, 1, 4, 5)

        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> new_head = sol.reverse_k_group(head, 6)
        >>> new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val, new_head.next.next.next.next.val
        (1, 2, 3, 4, 5)
        """

        new_head, current_tail, next_group_head, success = self.reverse(head, k)

        while success:
            (
                new_group_head,
                new_group_tail,
                next_next_group_head,
                success,
            ) = self.reverse(next_group_head, k)

            # Connect the tail of the previous group to the head of the new group
            current_tail.next = new_group_head
            current_tail = new_group_tail
            next_group_head = next_next_group_head

        return new_head


if __name__ == "__main__":
    import doctest

    doctest.testmod()
