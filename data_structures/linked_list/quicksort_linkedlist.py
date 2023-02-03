"""
Given a linked list with head pointer,
sort the linked list using quicksort technique without using any extra space
Time complexity: O(NlogN), Space complexity: O(1)
"""
from __future__ import annotations


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # method to insert nodes at the start of linkedlist
    def insert(self, new_data: int):
        """
        Pushes the element at the start of the linkedlist and returns None
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return

    # method to print the linkedlist
    def printll(self):
        """
        Prints the linkedlist in the particular format and returns None
        example: 1 ->3 ->4 ->2 ->9 ->6 ->8 -> 7
        """
        temp = self.head
        if temp == None:
            return "Linked List is empty"
        while temp.next:
            print(temp.data, "->", end="")
            temp = temp.next
        print(temp.data)
        return


def partition_algo(start: Node, end: Node):
    """
    This function takes in two pointers and returns the correct position of the pivot
    in the linkedlist between the given two pointers
    """
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
def quicksort_ll(start: Node, end: None):
    """
    This function sorts the linkedlist using quicksort and returns None
    """
    if start != end:
        pos = partition_algo(start, end)
        quicksort_ll(start, pos)
        quicksort_ll(pos.next, end)
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
    ll.printll()
    quicksort_ll(ll.head, None)
    print("Linkedlist after sorting: ")
    ll.printll()
