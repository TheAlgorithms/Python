from collections import deque
from typing import Any, Optional


class Queue:
    def __init__(self):
        self._dq = deque()

    def enqueue(self, v: Any) -> None:
        self._dq.append(v)

    def dequeue(self) -> Any:
        return self._dq.popleft()

    def peek(self) -> Optional[Any]:
        return self._dq[0] if self._dq else None
