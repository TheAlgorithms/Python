from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    # adding nodes
    def push(self, new_data: Any):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # swapping nodes
    def swap_nodes(self, node_data_1, node_data_2):
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
    ll = LinkedList()
    for i in range(5, 0, -1):
        ll.push(i)

    ll.print_list()

    ll.swap_nodes(1, 4)
    print("After swapping")
    ll.print_list()
