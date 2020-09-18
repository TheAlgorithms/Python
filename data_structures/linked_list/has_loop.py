from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next_node = None
 
    def __iter__(self):
        node = self
        while node:
            yield node.data
            node = node.next_node
     
    def has_loop(self) -> bool:
        >>> node1 = Node(1)
        >>> node1.next_node = Node(2)
        >>> node1.next_node.next_node = Node(3)
        >>> node1.next_node.next_node.next_node = Node(4)
        >>> node1.next_node.next_node.next_node = node1.next_node
        >>> has_loop(node1)
        True

        >>> node2 = Node(1)
        >>> node2.next_node = Node(2)
        >>> node2.next_node.next_node = Node(1)
        >>> node2.next_node.next_node.next_node = Node(2)
        >>> contains_loop(node2)
        False
        """
        return len(list(self)) != len(set(self))


if __name__ == "__main__":
    node1 = Node(1)
    node1.next_node = Node(2)
    node1.next_node.next_node = Node(3)
    node1.next_node.next_node.next_node = Node(4)
    node1.next_node.next_node.next_node = node1.next_node
    print(has_loop(node1))

    node2 = Node(5)
    node2.next_node = Node(6)
    node2.next_node.next_node = Node(5)
    node2.next_node.next_node.next_node = Node(6)
    print(has_loop(node2))

    node3 = Node(1)
    # node3.next_node = Node(2)
    # node3.next_node.next_node = node3
    print(has_loop(node3))
