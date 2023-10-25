class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right is not None:
            left = left.next
            right = right.next

        # deletion code

        left.next = left.next.next

        return dummy.next
