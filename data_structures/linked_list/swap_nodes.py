from doctest import testmod
from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        """
        pretty prints a linked list to the console
        >>> linkedList = LinkedList()
        >>> linkedList.push(10)
        >>> linkedList.push(20)
        >>> linkedList.push(30)
        >>> linkedList.print_list()
        <HEAD>
        30
        20
        10
        <TAIL>
        """
        temp = self.head
        print("<HEAD>")
        while temp is not None:
            print(temp.data)
            temp = temp.next
        print("<TAIL>")

    # adding nodes
    def push(self, new_data: Any):
        """
        adds a new node to a linked list
        >>> linkedList = LinkedList()
        >>> linkedList.push(30)
        >>> linkedList.head.data
        30
        >>> linkedList.push(20)
        >>> linkedList.head.data
        20
        >>> linkedList.push(10)
        >>> linkedList.head.data
        10
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # swapping nodes
    def swap_nodes(self, node_data_1, node_data_2):
        """
        swaps nodes with different data
        >>> linkedList = LinkedList()
        >>> linkedList.push(30)
        >>> linkedList.push(10)
        >>> linkedList.swap_nodes(30, 10)
        >>> linkedList.head.data
        30
        >>> linkedList.head.next.data
        10
        >>> linkedList = LinkedList()
        >>> linkedList.push(10)
        >>> linkedList.swap_nodes(10, 11)
        >>> linkedList.head.data
        10
        >>> linkedList = LinkedList()
        >>> linkedList.push(10)
        >>> linkedList.push(20)
        >>> linkedList.push(10)
        >>> linkedList.swap_nodes(10, 10)
        >>> linkedList.head.data
        10
        >>> linkedList.head.next.data
        20
        >>> linkedList.head.next.next.data
        10
        """
        if node_data_1 == node_data_2:
            return
        else:
            node_1 = self.head
            while node_1 is not None and node_1.data != node_data_1:
                node_1 = node_1.next

            node_2 = self.head
            while node_2 is not None and node_2.data != node_data_2:
                node_2 = node_2.next

            if node_1 is None or node_2 is None:
                return

            node_1.data, node_2.data = node_2.data, node_1.data


if __name__ == "__main__":
    testmod()
