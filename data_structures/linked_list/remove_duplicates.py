from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, item: Any, next: Any) -> None:  # noqa: A002
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size = 0

    def add(self, item: Any) -> None:
        self.head = Node(item, self.head)
        self.size += 1

    def remove(self) -> Any:
        # Switched 'self.is_empty()' to 'self.head is None'
        # because mypy was considering the possibility that 'self.head'
        # can be None in below else part and giving error
        if self.head is None:
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item

    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        """
        >>> linked_list = LinkedList()
        >>> linked_list.add(23)
        >>> linked_list.add(14)
        >>> linked_list.add(9)
        >>> print(linked_list)
        9 --> 14 --> 23
        """
        if not self.is_empty:
            return ""
        else:
            iterate = self.head
            item_str = ""
            item_list: list[str] = []
            while iterate:
                item_list.append(str(iterate.item))
                iterate = iterate.next

            item_str = " --> ".join(item_list)

            return item_str

    def __len__(self) -> int:
        """
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.add("a")
        >>> len(linked_list)
        1
        >>> linked_list.add("b")
        >>> len(linked_list)
        2
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        1
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        0
        """
        return self.size
    
    def remove_duplicates(self):
        if self.head is None or self.head.next is None:
            return 
        hash = set()
 
        current = self.head
        hash.add(self.head.item)
 
        while current.next is not None:
 
            if current.next.item in hash:
                current.next = current.next.next
                self.size-=1
            else:
                hash.add(current.next.item)
                current = current.next
 
        return 

    def printList(self):
        temp = self.head
 
        while(temp != None):
            print(temp.item, end=" ")
            temp = temp.next
 
        print()

l=LinkedList()
l.add(1)
l.add(2)
l.add(1)
l.add(4)
l.add(5)
l.add(6)
l.add(1)
l.add(4)
#list before removing duplicate elements
l.printList()
l.remove_duplicates()
#list after removing duplicate elements
l.printList()
