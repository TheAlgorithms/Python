from __future__ import annotations

from dataclasses import dataclass

"""
This is a sorted linked list class that
creates a sorted linked list of integer datatype
"""


@dataclass
class Node:
    def __init__(self, data) -> None:
        self.data: int = data
        self.next_node: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.data}, {self.next_node})"


class SortedLinkedList:
    def __init__(self) -> None:
        self.numNodes: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def __repr__(self) -> str:
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next_node
        return f"SortedLinkedList({', '.join(nodes)})"

    def insert(self, data: int) -> None:
        """This Function inserts node in it's sorted position
        This function can be re written for any data type but
        the comparator her must have to be changed

        Args:
            data (int): the data of linked list
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif data < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next_node and temp_node.next_node.data < data:
                temp_node = temp_node.next_node
            new_node.next_node = temp_node.next_node
            temp_node.next_node = new_node
            if new_node.next_node is None:
                self.tail = new_node
        self.numNodes += 1

    def display(self) -> None:
        """This function displays whole list"""
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next_node
        print()

    def delete(self, data: int) -> bool:
        """This Function deletes first appearance of node with
        data from it's sorted position

        This function can be re written for any data type but
        the comparator her must have to be changed

        Args:
            data (int): the data of the node that is needed to be deleted

        Returns:
            bool: status whether the node got deleted or not
        """
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return True

        temp_node = self.head
        while temp_node.next_node:
            if temp_node.next_node.data == data:
                temp_node.next_node = temp_node.next_node.next_node
                if temp_node.next_node is None:
                    self.tail = temp_node
                return True
            temp_node = temp_node.next_node

        return False

    def search(self, data: int) -> bool:
        """This function searches the data given input from user
        and return whether the data exists or not

        Args:
            data (int): Data to be searched

        Returns:
            bool: flag indicating whether data exists or not
        """
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next_node
        return False

    def is_empty(self) -> bool:
        """This function will check whether the list is empty or not

        Returns:
            bool: flag indicating whether list is empty or not
        """
        return self.head is None

    def length(self) -> int:
        """This function returns the length of the linked list


        Returns:
            int: The length of linked list
        """
        return self.numNodes

    def min_value(self) -> int | None:
        """This function will return minimum value

        Returns:
            int | None: min value or None if list is empty
        """
        if self.head is None:
            return None
        return self.head.data

    def max_value(self) -> int | None:
        """This function  will return maximum value


        Returns:
            int | None: max value or None if list is empty
        """
        if self.tail is None:
            return None
        return self.tail.data

    def remove_duplicates(self) -> None:
        """This Function will remove the duplicates from the list"""
        temp = self.head
        while temp and temp.next_node:
            if temp.data == temp.next_node.data:
                temp.next_node = temp.next_node.next_node
            else:
                temp = temp.next_node

    def reverse(self) -> None:
        """This function will reveres the list"""
        prev = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head

    def merge(self, other_list: SortedLinkedList) -> None:
        """This Function will merge the input list with current list

        Args:
            other_list (SortedLinkedList): The list to be merged
        """
        if other_list.head is None:
            return
        if self.head is None:
            self.head = other_list.head
            self.tail = other_list.tail
            return
        self.tail.next_node = other_list.head
        self.tail = other_list.tail


if __name__ == "__main__":
    linked_list = SortedLinedList()
    while True:
        print("Enter")
        print("1.  Insert")
        print("2.  Display")
        print("3.  Delete")
        print("4.  Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            data = int(input("Enter a number: "))
            linked_list.insert(data)
        elif choice == "2":
            linked_list.display()
        elif choice == "3":
            data = int(input("Enter the data to delete: "))
            if linked_list.delete(data):
                print(f"Node with data {data} deleted successfully")
            else:
                print(f"Node with data {data} not found in the list")
        elif choice == "4":
            break
        else:
            print("Wrong input")
