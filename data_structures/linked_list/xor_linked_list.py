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

from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.both: int = 0  # XOR of prev and next node ids


class XORLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._nodes = {}  # id → node map to simulate pointer references


    def _xor(self, a: Optional[Node], b: Optional[Node]) -> int:
        return (id(a) if a else 0) ^ (id(b) if b else 0)

    def insert(self, value: int) -> None:
        node = Node(value)
        self._nodes[id(node)] = node
        if self.head is None:
            self.head = self.tail = node
        else:
            node.both = id(self.tail)
            self.tail.both ^= id(node)
            self.tail = node

    def to_list(self) -> list[int]:
        result = []
        prev_id = 0
        current = self.head
        while current:
            result.append(current.value)
            next_id = prev_id ^ current.both
            prev_id = id(current)
            current = self._nodes.get(next_id)
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
