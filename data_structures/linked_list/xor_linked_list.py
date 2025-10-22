"""
XOR Linked List implementation
A memory-efficient doubly linked list using XOR of node addresses.
Each node stores one pointer that is the XOR of previous and next node addresses.
Example:
>>> xor_list = XORLinkedList()
>>> xor_list.insert(10)
>>> xor_list.insert(20)
>>> xor_list.insert(30)
>>> xor_list.to_list()
[10, 20, 30]
"""

# Note: 'from typing import Optional' is removed as we use the modern '|' syntax.


class Node:
    def __init__(self, value: int) -> None:
        """Initializes a Node with a value and a null pointer."""
        self.value = value
        self.both: int = 0  # XOR of prev and next node ids


class XORLinkedList:
    def __init__(self) -> None:
        """Initializes an empty XOR Linked List."""
        # Use 'Node | None' instead of 'Optional[Node]' (per ruff UP045)
        self.head: Node | None = None
        self.tail: Node | None = None
        # id -> node map to simulate pointer references
        self._nodes: dict[int, Node] = {}

    def _xor(self, node_a: Node | None, node_b: Node | None) -> int:
        """
        Helper function to get the XOR of two node IDs (simulated addresses).
        Names 'node_a' and 'node_b' are used for descriptive parameters.
        """
        id_a = id(node_a) if node_a else 0
        id_b = id(node_b) if node_b else 0
        return id_a ^ id_b

    def insert(self, value: int) -> None:
        """Inserts a value at the end of the list."""
        node = Node(value)
        self._nodes[id(node)] = node
        node_id = id(node)

        if self.head is None:
            # If the list is empty, head and tail are the new node
            self.head = self.tail = node
        else:
            # If the list is not empty, append to the tail
            # The new node's pointer is just the ID of the old tail
            node.both = id(self.tail)
            if self.tail:  # Type checker guard
                # The old tail's pointer must be updated to XOR
                # its previous node ID with the new node's ID.
                # self.tail.both was (prev_id ^ 0)
                # self.tail.both becomes (prev_id ^ new_node_id)
                self.tail.both ^= node_id
            self.tail = node

    def to_list(self) -> list[int]:
        """Converts the XOR list to a standard Python list (forward traversal)."""
        result = []
        prev_id = 0
        current = self.head
        while current:
            result.append(current.value)
            # Find next node's ID:
            # current.both = prev_id ^ next_id
            # so, next_id = prev_id ^ current.both
            current_id = id(current)
            next_id = prev_id ^ current.both

            # Move forward
            prev_id = current_id
            current = self._nodes.get(next_id)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
