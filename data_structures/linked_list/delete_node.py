from typing import Any


class CannotDeleteTailError(Exception):
    pass


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next_node: Node | None = None

    def __iter__(self):
        node = self
        while node:
            yield node.data
            node = node.next_node

    def delete(self) -> None:
        """
        Deletes the current node from the linked list by copying the data from the next node
        and bypassing the next node.

        It is assumed that the node to be deleted is not the tail node.

        >>> root_node = Node(1)
        >>> root_node.next_node = Node(2)
        >>> root_node.next_node.next_node = Node(3)
        >>> root_node.next_node.delete()  # delete node with value 2
        >>> list(root_node)
        [1, 3]
        """
        if self.next_node is None:
            raise CannotDeleteTailError("Cannot delete the tail node with this method.")

        # Copy data from the next node to the current node
        self.data = self.next_node.data
        # Bypass the next node
        self.next_node = self.next_node.next_node


if __name__ == "__main__":
    # Example 1
    root_node = Node(1)
    root_node.next_node = Node(2)
    root_node.next_node.next_node = Node(3)
    root_node.next_node.next_node.next_node = Node(4)

    # Delete node with value 3
    node_to_delete = root_node.next_node.next_node
    node_to_delete.delete()  # deletes node 3

    print(list(root_node))  # [1, 2, 4]

    # Example 2: Deleting the second node
    root_node = Node(10)
    root_node.next_node = Node(20)
    root_node.next_node.next_node = Node(30)

    # Delete node with value 20
    node_to_delete = root_node.next_node
    node_to_delete.delete()  # deletes node 20

    print(list(root_node))  # [10, 30]

    # Example 3: Trying to delete the tail node should raise an error
    root_node = Node(5)
    root_node.next_node = Node(6)
    tail_node = root_node.next_node

    try:
        tail_node.delete()  # Cannot delete the tail node
    except CannotDeleteTailError as e:
        print(e)  # Cannot delete the tail node with this method
