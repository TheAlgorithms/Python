from typing import Any


class Node:
    """
    A class that represents a node in a singly linked list.
    Each node contains a data attribute and a next attribute
    that points to the next node in the list.
    """

    def __init__(self, data: Any):
        self.data = data
        self.next = None


class LinkedList:
    """
    A class that represents a singly linked list.
    The class has a head attribute that points to the first node in the list.
    """

    def __init__(self):
        self.head = None

    def print_list(self):
        """
        A method that prints all the nodes in the linked list.
        """
        # start from the head node
        temp = self.head
        # traverse the list until the end is reached
        while temp is not None:
            # print the data of the current node and move to the next node
            print(temp.data, end=" ")
            temp = temp.next
        # print a newline character after printing all the nodes
        print()

    def push(self, new_data: Any):
        """
        A method that adds a new node to the beginning of the linked list.
        """
        # create a new node with the given data
        new_node = Node(new_data)
        # set the next attribute of the new node to the current head node
        new_node.next = self.head
        # set the head attribute of the linked list to the new node
        self.head = new_node

    def swap_nodes(self, node_data_1, node_data_2):
        """
        A method that swaps the nodes with data values
        node_data_1 and node_data_2 in the linked list.
        If either node is not found, the method simply returns.
        """
        # if the two data values are the same, no swapping is needed
        if node_data_1 == node_data_2:
            return

        # find the first node
        node_1 = self.head
        while node_1 is not None and node_1.data != node_data_1:
            node_1 = node_1.next

        # find the second node
        node_2 = self.head
        while node_2 is not None and node_2.data != node_data_2:
            node_2 = node_2.next

        # if either node is not found, return
        if node_1 is None or node_2 is None:
            return

        # swap the data of the two nodes
        node_1.data, node_2.data = node_2.data, node_1.data


if __name__ == "__main__":
    # create an instance of the LinkedList class
    ll = LinkedList()
    # add five nodes to the beginning of the linked list using the push method
    for i in range(5, 0, -1):
        ll.push(i)

    # print the linked list using the print_list method
    ll.print_list()

    # swap nodes with data values of 1 and 4
    ll.swap_nodes(1, 4)

    # print the modified linked list
    print("After swapping")
    ll.print_list()
