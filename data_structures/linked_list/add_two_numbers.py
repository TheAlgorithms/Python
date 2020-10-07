'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and
each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

import time


class ListNode():
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


class Solution():
    def add_two_numbers(self, l_1, l_2, c = 0):
        val = l_1.val + l_2.val + c
        c = val//10
        sum_ll = ListNode(val%10)
        if (l_1.next!= None, l_2.next!=None, c!=0):
            if l_1.next == None:
                l_1.next = ListNode(0)
            if l_2.next == None:
                l_2.next = ListNode(0)
            else:
                sum_ll.next = self.add_two_numbers(l_1.next, l_2.next, c)
        return sum_ll

    def list_to_link(self, arr):
        if len(arr) == 1:
            return ListNode(arr[0])
        else:
            return ListNode(arr[0], self.list_to_link(arr[1:]))

    def reverse_list(self, head):
        new_head = None
        while head:
            head.next, head, new_head = new_head, head.next, head
        return new_head

    def display(self, ll):
        while ll:
            print(ll.val)
            ll = ll.next


if __name__ == "__main__":
    s = Solution()
    start = time.time()
    print("ENTER FIRST LIST")
    num1 = input()
    num1 = list(map(int, num1.split()))
    print("\n")
    print("ENTER SECOND LIST")
    num2 = input()
    num2 = list(map(int, num2.split()))
    print("\n")
    l1 = s.list_to_link(num1)
    l2 = s.list_to_link(num2)
    l_1 = s.reverse_list(l1)
    l_2 = s.reverse_list(l2)
    l_s = s.add_two_numbers(l_1, l_2)
    l_s = s.reverse_list(l_s)
    s.display(l_s)
    print("time taken: {} seconds".format(time.time() - start))