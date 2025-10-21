import heapq
from typing import Any, List, Optional


class MinHeap:
    def __init__(self):
        self._data: List[Any] = []

    def push(self, v: Any) -> None:
        heapq.heappush(self._data, v)

    def pop(self) -> Any:
        return heapq.heappop(self._data)

    def peek(self) -> Optional[Any]:
        return self._data[0] if self._data else None
