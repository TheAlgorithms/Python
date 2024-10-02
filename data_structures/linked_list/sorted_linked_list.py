from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    """THis class represents  a node in the linked list."""

    def __init__(self, data: int) -> None:
        """Constructor of Node class

        Args:
            data (int): Data of node

        Doctests

        >>> Node(20)
        Node(20)
        >>> Node(27)
        Node(27)
        >>> Node(None)
        Node(None)
        """
        self.data: int = data
        self.next_node: Node | None = None

    def __repr__(self) -> str:
        """
        Get the string representation of this node.
        >>> Node(10).__repr__()
        'Node(10)'
        >>> repr(Node(10))
        'Node(10)'
        >>> str(Node(10))
        'Node(10)'
        >>> Node(10)
        Node(10)
        """
        return f"Node({self.data})"


class SortedLinkedList:
    """This class  represents a sorted linked list."""

    def __init__(self) -> None:
        """
        Create and initialize LinkedList class instance.
        >>> linked_list = SortedLinkedList()
        >>> linked_list.head is None
        True
        """
        self.num_nodes: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def __repr__(self) -> str:
        """
        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(2)
        >>> linkedList.insert(12)
        >>> linkedList.insert(21)
        >>> linkedList.insert(23)
        >>> linkedList.insert(72)
        >>> linkedList.__repr__()
        '2, 12, 21, 23, 72'
        """
        nodes = []
        temp: Node | None = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next_node
        return f"{', '.join(nodes)}"

    def insert(self, data: int) -> None:
        """This Function inserts node in it's sorted position
        This function can be re written for any data type but
        the comparator her must have to be changed

        Args:
            data (int): the data of linked list

        Doctests
        >>> linked_list = SortedLinkedList()
        >>> linked_list.insert(32)
        >>> linked_list.insert(57)
        >>> linked_list.insert(45)
        >>> linked_list
        32, 45, 57
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif data < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            temp_node: Node | None = self.head
            if temp_node:
                while temp_node.next_node and temp_node.next_node.data < data:
                    temp_node = temp_node.next_node
                new_node.next_node = temp_node.next_node
                temp_node.next_node = new_node
                if new_node.next_node is None:
                    self.tail = new_node
        self.num_nodes += 1

    def display(self) -> None:
        """
        This function displays whole list

        Doctests


        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList.display()
        32, 45, 57
        """
        print(repr(self))

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
        >>> linkedList.display()
        32, 45, 57
        >>> linkedList.delete(45)
        True
        >>> linkedList.display()
        32, 57
        """
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return True

        temp_node: Node | None = self.head
        if temp_node:
            while temp_node.next_node:
                if temp_node.next_node.data == data:
                    temp_node.next_node = temp_node.next_node.next_node
                    if temp_node.next_node is None:
                        self.tail = temp_node
                    self.num_nodes -= 1
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

        Doctests
        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList.search(45)
        True
        >>> linkedList.search(90)
        False
        """
        temp: Node | None = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next_node
        return False

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

        return self.head is None

    def length(self) -> int:
        """This function returns the length of the linked list


        Returns:
            int: The length of linked list

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.length()
        0
        >>> linkedList.insert(32)
        >>> linkedList.length()
        1
        >>> linkedList.insert(57)
        >>> linkedList.length()
        2
        >>> linkedList.insert(45)
        >>> linkedList.length()
        3
        >>> linkedList.delete(45)
        True
        >>> linkedList.length()
        2
        """
        return self.num_nodes

    def min_value(self) -> int | None:
        """This function will return minimum value

        Returns:
            int | None: min value or None if list is empty

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList.min_value()
        32
        """
        if self.head is None:
            return None
        return self.head.data

    def max_value(self) -> int | None:
        """This function  will return maximum value


        Returns:
            int | None: max value or None if list is empty

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList.max_value()
        57
        """
        if self.tail is None:
            return None
        return self.tail.data

    def remove_duplicates(self) -> None:
        """
        This Function will remove the duplicates from the list

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList.insert(45)
        >>> linkedList.display()
        32, 45, 45, 57
        >>> linkedList.remove_duplicates()
        >>> linkedList.display()
        32, 45, 57
        """

        temp: Node | None = self.head
        while temp and temp.next_node:
            if temp.data == temp.next_node.data:
                temp.next_node = temp.next_node.next_node
            else:
                temp = temp.next_node

    def merge(self, other_list: SortedLinkedList) -> None:
        """This Function will merge the input list with current list

        Args:
            other_list (SortedLinkedList): The list to be merged

        Doctests

        >>> linkedList=SortedLinkedList()
        >>> linkedList.insert(32)
        >>> linkedList.insert(57)
        >>> linkedList.insert(45)
        >>> linkedList2=SortedLinkedList()
        >>> linkedList2.insert(23)
        >>> linkedList2.insert(47)
        >>> linkedList2.insert(95)
        >>> linkedList.merge(linkedList2)
        >>> linkedList.display()
        23, 32, 45, 47, 57, 95
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
                temp = temp.next_node


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
