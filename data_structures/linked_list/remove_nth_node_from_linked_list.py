# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        while(temp!=None):
            length+=1
            temp=temp.next
        n=length-n
        temp=head
        for i in range(n-1):
            temp=temp.next
        if length==1:
            head=None
        if n==0:
            head=temp.next
        elif n>=length-1:
            temp.next=None
        else:
            temp.next=temp.next.next 
        return head