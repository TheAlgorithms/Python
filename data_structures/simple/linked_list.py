from typing import Any, Optional


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, value: Any) -> None:
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def prepend(self, value: Any) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node

    def find(self, value: Any) -> Optional[Node]:
        cur = self.head
        while cur:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def delete(self, value: Any) -> bool:
        cur = self.head
        prev = None
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def to_list(self) -> list:
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out
