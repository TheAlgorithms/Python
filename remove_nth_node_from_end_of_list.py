class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
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
