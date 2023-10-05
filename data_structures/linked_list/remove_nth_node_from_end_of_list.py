from __future__ import annotations


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data: int) -> int:
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return self.head.data

    def view(self):
        ret = ""
        temp = self.head
        while temp is not None:
            ret += str(temp.data)
            ret += "->"
            temp = temp.next
        return ret[:-2]

    def remove_nth_from_end(self, n) -> int | None:
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
        5 -> 6 -> 8 -> 8 -> 10 -> 12 -> -25 -> -20
        #removed 17
        >>>
        """
        # want to have two pointers, one at the start and the other k nodes forward
        # We could complete this in one pass if we stored a self.size variable

        if not self.head:
            print("No element found.")
            return None

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        if n > size or n <= 0:
            print(f"Try with an N in range of: 1 to {size}")
            return None

        if n == size:
            self.head = self.head.next
            return link.view()

        first = self.head
        for _i in range(n):
            first = first.next
        second = self.head
        prev = None

        while first:
            first = first.next
            prev = second
            second = second.next

        if prev:
            prev.next = second.next
        return self.view()


if __name__ == "__main__":
    link = LinkedList()
    for _ in range(int(input().strip())):
        data = int(input().strip())
        link.append(data)
    print(link.view())
    print(link.remove_nth_from_end(int(input().strip())))
