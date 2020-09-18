from typing import Any


class Node:
    """
    Class to represent a single node in a singly linked list.
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next_node = None


def contains_loop(root: Node) -> bool:
    """
    A linked list contains a loop when traversing through a loop, no null is reached.

    Given a node, returns true if linked list contains a loop
    returns false otherwise

    >>> node1 = Node(1)
    >>> node1.next_node = Node(2)
    >>> node1.next_node.next_node = Node(3)
    >>> node1.next_node.next_node.next_node = Node(4)
    >>> node1.next_node.next_node.next_node = node1.next_node
    >>> contains_loop(node1)
    True

    >>> node2 = Node(1)
    >>> node2.next_node = Node(2)
    >>> node2.next_node.next_node = Node(1)
    >>> node2.next_node.next_node.next_node = Node(2)
    >>> contains_loop(node2)
    False
    """

    counter1 = root
    counter2 = root

    while counter1.next_node and counter2.next_node and counter2.next_node.next_node:
        counter1 = counter1.next_node
        counter2 = counter2.next_node.next_node

        if counter1 is counter2:
            return True

    return False


if __name__ == "__main__":
    node1 = Node(1)
    node1.next_node = Node(2)
    node1.next_node.next_node = Node(3)
    node1.next_node.next_node.next_node = Node(4)
    node1.next_node.next_node.next_node = node1.next_node
    print(contains_loop(node1))

    node2 = Node(5)
    node2.next_node = Node(6)
    node2.next_node.next_node = Node(5)
    node2.next_node.next_node.next_node = Node(6)
    print(contains_loop(node2))

    node3 = Node(1)
    # node3.next_node = Node(2)
    # node3.next_node.next_node = node3
    print(contains_loop(node3))
