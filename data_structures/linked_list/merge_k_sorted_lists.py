# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in lists:
            while i:
                arr.append([i.val, i])
                i = i.next

        arr.sort(key=lambda x: x[0])
        head = ListNode()
        curr = head
        for i in arr:
            curr.next = i[1]
            curr = curr.next

        return head.next
