"""
https://www.topcoder.com/thrive/articles/reverse-node-in-k-group
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
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

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse a linked list in groups of size k.

        Args:
            head: The head of the linked list.
            k: The group size for reversing.

        Returns:
            The new head of the reversed linked list.

        >>> sol = Solution()
        >>> linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> reversed_list = sol.reverseKGroup(linked_list, 2)
        >>> reversed_list.val
        2
        >>> reversed_list.next.val
        1
        >>> reversed_list.next.next.val
        4
        >>> reversed_list.next.next.next.val
        3
        >>> reversed_list.next.next.next.next.val
        5
        >>> reversed_list.next.next.next.next.next is None
        True
        """
        count = self.length(head)
        ans = self.reverse(head, count, k)
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
