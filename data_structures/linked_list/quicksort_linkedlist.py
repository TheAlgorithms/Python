"""
Given a linked list with head pointer,
sort the linked list using quicksort technique without using any extra space
Time complexity: O(NlogN), Space complexity: O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # method to insert nodes at the start of linkedlist
    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # method to print the linkedlist
    def printLL(self):
        temp = self.head
        if temp == None:
            return "Linked List is empty"
        while temp.next:
            print(temp.data, "->", end="")
            temp = temp.next
        print(temp.data)
        return


# Partition algorithm with pivot as first element


def partition(start, end):
    if start == None or start.next == None:
        return start
    prev, curr = start, start.next
    pivot = prev.data
    while curr != end:
        if curr.data < pivot:
            prev = prev.next
            temp = prev.data
            prev.data = curr.data
            curr.data = temp
        curr = curr.next
    temp = prev.data
    prev.data = start.data
    start.data = temp
    return prev


# recursive quicksort for function calls
def quicksort_LL(start, end):
    if start != end:
        pos = partition(start, end)
        quicksort_LL(start, pos)
        quicksort_LL(pos.next, end)
        return


if __name__ == "__main__":
    ll = LinkedList()
    print(
        "Enter the space seperated values of numbers to be inserted in linkedlist prompted below:"
    )
    arr = list(map(int, input().split()))
    for num in arr:
        ll.insert(num)
    print("Linkedlist before sorting:")
    ll.printLL()
    quicksort_LL(ll.head, None)
    print("Linkedlist after sorting: ")
    ll.printLL()
