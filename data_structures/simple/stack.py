from typing import Any, Optional
from .linked_list import LinkedList


class ListStack:
    def __init__(self):
        self._data = []

    def push(self, v: Any) -> None:
        self._data.append(v)

    def pop(self) -> Any:
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        return self._data[-1] if self._data else None


class LinkedStack:
    def __init__(self):
        self._list = LinkedList()

    def push(self, v: Any) -> None:
        self._list.prepend(v)

    def pop(self) -> Any:
        if not self._list.head:
            raise IndexError("pop from empty stack")
        val = self._list.head.value
        self._list.head = self._list.head.next
        return val

    def peek(self) -> Optional[Any]:
        return self._list.head.value if self._list.head else None
