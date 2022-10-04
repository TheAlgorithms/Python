from collections.abc import Iterator
from typing import Any

"""
*************************************************** Rotate Linked List **************************************************************
- Given a linked list, rotate the list to the right by k places, where k is non-negative.
- Example 1:
    Input: linked list = 1->2->3->4->5->6, k = 4
    Output: 5->6->1->2->3->4.
    Explanation: k is smaller than the count of nodes in a linked list so (k+1)th node i.e. 5 becomes the head node and 6's next points to 1.
- Example 2:
    Input: linked list = 3->4->5->6, k = 2
    Output: 5->6->3->4.
    Explanation: k is smaller than the count of nodes in a linked list so (k+1)th node i.e. 5 becomes the head node and 6's next points to 3.
*************************************************************************************************************************************
"""

"""
Algorithm:
    1. Find the length of the linked list
    2. Find the (k+1)th node from the end of the linked list
    3. Make the (k+1)th node as the head node
    4. Make the (k+1)th node's next node as the head node's next node
    5. Make the head node's next node as the head node
"""


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class RotateLinkedList:
    # This magic function is called when the object is created
    def __init__(self) -> None:
        self.head = None

    # This magic function is to iterate through the linked list
    def __iter__(self) -> Iterator[Any]:
        node = self.head
        while self.head:
            yield node.data
            node = node.next
            if node == self.head:
                break

    # This magic function is to calculate the length of linked list
    def __len__(self) -> int:
        return len(tuple(iter(self)))

    # This magic function is to print the linked list
    def __repr__(self):
        return "->".join(str(item) for item in iter(self))

    def is_empty(self) -> bool:
        return len(self) == 0

    def Insert(self, newValue: int) -> None:
        newNode = Node(newValue)
        if self.head == None:
            self.head = newNode
            return

        current = self.head

        while current.next != None:
            current = current.next

        current.next = newNode

    """
    To rotate the linked list, we need to change the next pointer of kth node to NULL,
    the next pointer of the last node should point to the previous head node, and finally,
    change the head to (k+1)th node. So we need to get hold of three nodes: kth node,
    (k+1)th node, and last node.
    """

    def rotateRight(self, k: int) -> None:
        if k == 0:
            return self.head

        if self.head == None:
            return None

        current = Node()
        current = self.head

        length = 1

        # Find the length of the linked list
        while current.next != None:
            current = current.next
            length += 1

        current.next = self.head
        current = self.head

        """
        Traverse the list from the beginning and stop at kth node. store k's
        next in a tem pointer and point k's next to NULL then start traversing
        from tem and keep traversing till the end and point end node's next to
        start node and make tem as the new head.
        """
        # To perform rotation, we need to find the (length - k % length)th node from the beginning
        for i in range(0, length - (k % length) - 1):
            current = current.next

        # The next node of the current node will be the new head
        self.head = current.next
        current.next = None

        return self.head


def test_rotate_linked_list() -> None:
    """
    >>> test_rotate_linked_list()
    """
    rotate_linked_list = RotateLinkedList()
    assert len(rotate_linked_list) == 0
    assert rotate_linked_list.is_empty() is True
    assert str(rotate_linked_list) == ""

    rotate_linked_list.Insert(1)
    rotate_linked_list.Insert(2)
    rotate_linked_list.Insert(3)
    rotate_linked_list.Insert(4)
    rotate_linked_list.Insert(5)
    """
    >>> str(rotate_linked_list)
    1->2->3->4->5
    """

    rotate_linked_list.rotateRight(2)
    """
    >>> str(rotate_linked_list)
    3->4->5->1->2
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
