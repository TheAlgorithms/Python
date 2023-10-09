# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        cl1, cl2 = 0, 0
        while l1:
            l1 = l1.next
            cl1 += 1
        while l2:
            l2 = l2.next
            cl2 += 1   
        l1, l2 = headA, headB
        if cl1 > cl2:
            for _ in range(cl1 - cl2):
                l1 = l1.next     
        elif cl1 < cl2:
            for _ in range(cl2 - cl1) :
                l2 = l2.next         
        while l1:
            if l1 == l2:
                return l1
            l1, l2 = l1.next, l2.next
                
        return None
