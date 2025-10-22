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

# Note: 'from typing import Optional' is no longer needed
# as we use the modern 'Node | None' syntax.


class Node:
    def __init__(self, value: int) -> None:
        """Initializes a Node with a value and a null pointer."""
        self.value = value
        self.both: int = 0  # XOR of prev and next node ids


class XORLinkedList:
    def __init__(self) -> None:
        """Initializes an empty XOR Linked List."""
        self.head: Node | None = None
        self.tail: Node | None = None
        # id -> node map to simulate pointer references
        self._nodes: dict[int, Node] = {}

    def _xor(self, a: Node | None, b: Node | None) -> int:
        """Helper function to get the XOR of two node IDs."""
        return (id(a) if a else 0) ^ (id(b) if b else 0)

    def insert(self, value: int) -> None:
        """Inserts a value at the end of the list."""
        node = Node(value)
        self._nodes[id(node)] = node

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
                self.tail.both ^= id(node)
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
            next_id = prev_id ^ current.both

            # Move forward
            prev_id = id(current)
            current = self._nodes.get(next_id)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()