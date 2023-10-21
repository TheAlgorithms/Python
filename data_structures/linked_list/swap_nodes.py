from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        """
        Initialize a new Node with the given data.

        Args:
            data: The data to be stored in the node.

        """
        self.data = data
        self.next: Node | None = None  # Reference to the next node


class LinkedList:
    def __init__(self) -> None:
        """
        Initialize an empty Linked List.
        """
        self.head: Node | None = None  # Reference to the head (first node)

    def print_list(self):
        """
        Print the elements of the Linked List in order.

        Examples:
            >>> new_list = LinkedList()
            >>> new_list.push(0)
            >>> new_list.push(2)
            >>> new_list.push(2)
            >>> new_list.push(3)
            >>> new_list.push(4)
            >>> new_list.print_list()
            4 3 2 2 0

        Args:
            No arguments.

        Returns:
            None
        """
        temp = self.head
        while temp is not None:
            if not temp.next:
                print(temp.data)
            else:
                print(temp.data, end=" ")
            temp = temp.next

    def push(self, new_data: Any) -> None:
        """
        Add a new node with the given data to the beginning of the Linked List.

        Args:
            new_data (Any): The data to be added to the new node.

        Examples:
            >>> new_list = LinkedList()
            >>> new_list.push(5)
            >>> new_list.push(4)
            >>> new_list.push(3)
            >>> new_list.push(2)
            >>> new_list.push(1)
            >>> new_list.print_list()
            1 2 3 4 5

        Returns:
            None

        Raises:
            None
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def swap_nodes(self, node_data_1, node_data_2) -> None:
        """
        Swap the positions of two nodes in the Linked List based on their data values.

        Args:
            node_data_1: Data value of the first node to be swapped.
            node_data_2: Data value of the second node to be swapped.


        Note:
            If either of the specified data values isn't found then, no swapping occurs.

        Examples:
        When both values are present in a linkedlist.
            >>> new_list = LinkedList()
            >>> new_list.push(5)
            >>> new_list.push(4)
            >>> new_list.push(3)
            >>> new_list.push(2)
            >>> new_list.push(1)
            >>> new_list.print_list()
            1 2 3 4 5
            >>> new_list.swap_nodes(1, 5)
            >>> new_list.print_list()
            5 2 3 4 1

        When just a single value is present in the linkedlist.
            >>> second_list = LinkedList()
            >>> second_list.push(6)
            >>> second_list.push(7)
            >>> second_list.push(8)
            >>> second_list.push(9)
            >>> second_list.swap_nodes(1, 6) is None
            True

        When both values are absent in the linkedlist.
            >>> second_list = LinkedList()
            >>> second_list.push(10)
            >>> second_list.push(9)
            >>> second_list.push(8)
            >>> second_list.push(7)
            >>> second_list.swap_nodes(1, 3) is None
            True

        When linkedlist is empty.
            >>> second_list = LinkedList()
            >>> second_list.swap_nodes(1, 3) is None
            True

        Returns:
            None
        
        Raises:
            None
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

            # Swap the data values of the two nodes
            node_1.data, node_2.data = node_2.data, node_1.data


if __name__ == "__main__":
    """
    Python script that outputs the swap of nodes in a linkedlist.
    """
    ll = LinkedList()
    for i in range(5, 0, -1):
        ll.push(i)

    print("Original Linked List:")
    ll.print_list()

    ll.swap_nodes(1, 4)
    print("After swapping the nodes whose data is 1 and 4:")

    ll.print_list()
