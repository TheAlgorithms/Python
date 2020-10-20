from typing import Tuple

"""
`group_odd_even_nodes` will group all odd indexed nodes at the beginning
of the list and all even indexed nodes following the odd indexed nodes.

https://www.geeksforgeeks.org/rearrange-a-linked-list-such-that-all-even-and-odd-positioned-nodes-are-together/

- This will run in O(1) space and O(n) time
- Groups by index and **NOT** the value of the node
- Will return the head if there is one or none elements in the Linked List
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """Returns a visual representation of the node and all its
        following nodes."""
        string_rep = []
        temp = self
        while temp:
            string_rep.append(f"{temp.data}")
            temp = temp.next
        return "->".join(string_rep)


class LinkedList:
    """
    >>> linked_list = LinkedList()
    >>> linked_list.group_odd_even_nodes()

    >>> linked_list.insert(5)
    >>> linked_list.group_odd_even_nodes()
    5
    >>> linked_list.insert(7)
    >>> linked_list.group_odd_even_nodes()
    7->5
    >>> linked_list.insert(8)
    >>> linked_list.group_odd_even_nodes()
    8->5->7
    >>> linked_list.clear_list()
    >>> linked_list.insert(5)
    >>> linked_list.insert(7)
    >>> linked_list.insert(8)
    >>> linked_list.insert(9)
    >>> linked_list.group_odd_even_nodes()
    9->7->8->5
    >>> linked_list.clear_list()
    >>> linked_list.insert(5)
    >>> linked_list.insert(7)
    >>> linked_list.insert(8)
    >>> linked_list.insert(9)
    >>> linked_list.insert(2)
    >>> linked_list.group_odd_even_nodes()
    2->8->5->9->7
    """

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head

        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        """
        String representation/visualization of a Linked Lists
        """
        return "->".join([str(item) for item in self])

    def insert(self, data) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            self.head = Node(data, self.head)

    def remove(self, data) -> Tuple[str, Node]:
        if self.is_empty():
            return "Linked List is empty"
        else:
            prev, current = None, self.head
            while current:
                if current.data == data:
                    if prev:
                        prev.next = current.next
                        current = prev
                    else:
                        self.head = self.head.next
                else:
                    prev = current
                current = current.next
            return self.head

    def is_empty(self) -> bool:
        return self.head is None

    def group_odd_even_nodes(self) -> Node:
        if not self.head or not self.head.next:
            return self.head

        odd = self.head
        even = self.head.next

        while even and even.next:
            temp = even.next
            even.next = even.next.next

            temp.next = odd.next
            odd.next = temp

            odd = odd.next
            even = even.next

        return self.head

    def clear_list(self):
        self.head = None


def main():
    from doctest import testmod

    testmod()

    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert(8)
    linked_list.insert(9)
    linked_list.insert(2)
    print(linked_list)  # expect 2->9->8->7->5

    linked_list.group_odd_even_nodes()
    print(linked_list)  # expect 2->8->5->9->7


if __name__ == "__main__":
    main()
