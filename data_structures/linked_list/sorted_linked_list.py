from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(order=True)
class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the linked list.

    >>> Node(1, Node(2, Node(3)))
    Node(data=1, next=Node(data=2, next=Node(data=3, next=None)))
    """

    data: int
    next: Node | None = None


class SortedLinkedList:
    """This class  represents a sorted linked list."""

    def __init__(self) -> None:
        """
        Create and initialize LinkedList class instance.
        >>> linked_list = SortedLinkedList()
        >>> linked_list.head is None
        True
        """
        self.head: Node | None = None
        self.tail: Node | None = None

    def __iter__(self) -> Iterator[int]:
        """Iterate over the data of the nodes in the linked list.

        >>> linked_list = SortedLinkedList()
        >>> linked_list.insert(3)
        >>> linked_list.insert(1)
        >>> linked_list.insert(2)
        >>> tuple(linked_list)
        (1, 2, 3)
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self) -> int:
        """Return the number of nodes in the linked list.

        >>> linked_list = SortedLinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.insert(3)
        >>> len(linked_list)
        1
        >>> linked_list.insert(1)
        >>> linked_list.insert(2)
        >>> len(linked_list)
        3
        """
        return len(tuple(self))

    def __contains__(self, data: int) -> bool:
        """Check if a node with the given data exists in the linked list.

        >>> linked_list = SortedLinkedList()
        >>> linked_list.insert(3)
        >>> 3 in linked_list
        True
        >>> 1 in linked_list
        False
        """
        return data in tuple(self)

    def insert(self, data: int) -> None:
        """Inserts a node in its sorted position
        This function can be rewritten for any data type, but
        the comparator here must be changed

        Args:
            data (int): the data of the linked list

        Doctests
        >>> linked_list = SortedLinkedList()
        >>> linked_list.insert(32)
        >>> linked_list.insert(57)
        >>> linked_list.insert(45)
        >>> tuple(linked_list)
        (32, 45, 57)
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif new_node < self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node: Node | None = self.head
            if temp_node:
                while temp_node.next and temp_node.next.data < data:
                    temp_node = temp_node.next
                new_node.next = temp_node.next
                temp_node.next = new_node
                if new_node.next is None:
                    self.tail = new_node

    def delete(self, data: int) -> bool:
        """This Function deletes first appearance of node with
        data from it's sorted position

        This function can be re written for any data type but
        the comparator her must have to be changed

        Args:
            data (int): the data of the node that is needed to be deleted

        Returns:
            bool: status whether the node got deleted or not

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> tuple(linkedList)
        (32, 45, 57)
        >>> linkedList.delete(45)
        True
        >>> tuple(linkedList)
        (32, 57)
        """
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        temp_node: Node | None = self.head
        if temp_node:
            while temp_node.next:
                if temp_node.next.data == data:
                    temp_node.next = temp_node.next.next
                    if temp_node.next is None:
                        self.tail = temp_node
                    return True
                temp_node = temp_node.next

        return False

    def search(self, data: int) -> bool:
        """This function searches the data given input from user
        and return whether the data exists or not

        Args:
            data (int): Data to be searched

        Returns:
            bool: flag indicating whether data exists or not

        Doctests
        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> tuple(linkedList)
        (32, 45, 57)
        >>> linkedList.search(45)
        True
        >>> linkedList.search(90)
        False
        """
        return data in self

    def is_empty(self) -> bool:
        """This function will check whether the list is empty or not

        Returns:
            bool: flag indicating whether list is empty or not

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.is_empty()
        True
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList.is_empty()
        False
        """
        return not self

    def min_value(self) -> int | None:
        """This function will return minimum value

        Returns:
            int | None: min value or None if list is empty

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.min_value() is None
        True
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList.min_value()
        32
        """
        return min(self) if self.head else None

    def max_value(self) -> int | None:
        """This function  will return maximum value


        Returns:
            int | None: max value or None if list is empty

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.max_value() is None
        True
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList.max_value()
        57
        """
        return max(self) if self.head else None

    def remove_duplicates(self) -> None:
        """
        This Function will remove the duplicates from the list

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList.insert(45)
        >>> tuple(linkedList)
        (32, 45, 45, 57)
        >>> linkedList.remove_duplicates()
        >>> tuple(linkedList)
        (32, 45, 57)
        """

        temp: Node | None = self.head
        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next

    def merge(self, other_list: SortedLinkedList) -> None:
        """This Function will merge the input list with current list

        Args:
            other_list (SortedLinkedList): The list to be merged

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> tuple(linkedList)
        (32, 45, 57)
        >>> linkedList2=SortedLinkedList()
        >>> linkedList2.insert(23)
        >>> linkedList2.insert(47)
        >>> linkedList2.insert(95)
        >>> tuple(linkedList2)
        (23, 47, 95)
        >>> linkedList.merge(linkedList2)
        >>> tuple(linkedList)
        (23, 32, 45, 47, 57, 95)
        """
        if other_list.head is None:
            return
        elif self.head is None:
            self.head = other_list.head
            self.tail = other_list.tail
            return
        else:
            temp: Node | None = other_list.head

            while temp:
                self.insert(temp.data)
                temp = temp.next


if __name__ == "__main__":
    linked_list = SortedLinkedList()
    while True:
        print("Enter")
        print("1.  Insert")
        print("2.  Display")
        print("3.  Delete")
        print("4.  Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            node_data = int(input("Enter a number: "))
            linked_list.insert(node_data)
        elif choice == "2":
            linked_list.display()
        elif choice == "3":
            node_data = int(input("Enter the data to delete: "))
            if linked_list.delete(node_data):
                print(f"Node with data {node_data} deleted successfully")
            else:
                print(f"Node with data {node_data} not found in the list")
        elif choice == "4":
            break
        else:
            print("Wrong input")
