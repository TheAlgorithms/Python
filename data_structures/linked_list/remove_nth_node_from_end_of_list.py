"""Learn more about this algorithm: https://www.geeksforgeeks.org/delete-nth-node-from-the-end-of-the-given-linked-list/"""

from __future__ import annotations


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Node | None = None


class LinkedListExceptionError(Exception):
    pass


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    # from middle_element_of_linked_list
    def append(self, new_data: int) -> int:
        """
        >>> link = LinkedList()
        >>> link.append(5)
        5
        >>> link.append(6)
        6
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        if not self.head:
            raise LinkedListExceptionError(
                "Unexpected error: Head of linked list is None after append operation."
            )
        return self.head.data

    def view(self) -> str:
        """
        >>> link = LinkedList()
        >>> link.append(5)
        >>> link.append(6)
        >>> link.view()
        '6->5'
        """
        ret = ""
        temp = self.head
        while temp is not None:
            ret += str(temp.data)
            ret += "->"
            temp = temp.next
        return ret[:-2]

    def remove_nth_from_end(self, position_from_end: int) -> Node | None:
        """
        >>> link = LinkedList()
        >>> link.remove_nth_from_end(3)
        No element found.
        >>> link.append(5)
        5
        >>> link.append(6)
        6
        >>> link.append(8)
        8
        >>> link.append(8)
        8
        >>> link.append(10)
        10
        >>> link.append(12)
        12
        >>> link.append(17)
        17
        >>> link.append(-25)
        -25
        >>> link.append(-20)
        -20
        >>> link.remove_nth_from_end(3)
        5->6->8->8->10->12->-25->-20
        >>>
        """
        # want to have two pointers, one at the start and the other k nodes forward
        # We could complete this in one pass if we stored a self.size variable
        if not self.head:
            print("No element found.")
            return None

        size = 0
        current: Node | None = self.head
        while current:
            size += 1
            current = current.next

        if position_from_end > size or position_from_end <= 0:
            print(f"Try with an N in range of: 1 to {size}")
            return None

        first: Node | None = self.head
        for _i in range(position_from_end):
            if first:
                first = first.next

        second: Node | None = self.head
        prev: Node | None = None

        while first:
            first = first.next
            prev = second
            if second:
                second = second.next

        if prev and second:
            prev.next = second.next
        elif not prev and self.head:
            self.head = self.head.next

        return self.head


if __name__ == "__main__":
    link = LinkedList()
    for _ in range(int(input().strip())):
        data = int(input().strip())
        link.append(data)
    print("Before list: ")
    print(link.view())
    print(link.remove_nth_from_end(int(input().strip())))
    print("After list: ")
    print(link.view())
