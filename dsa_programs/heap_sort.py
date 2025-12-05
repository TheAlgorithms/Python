"""Heap sort implemented with Python's heapq."""

from heapq import heappop, heappush
from typing import MutableSequence, TypeVar

T = TypeVar("T")


def heap_sort(items: MutableSequence[T]) -> MutableSequence[T]:
    heap: list[T] = []
    for value in items:
        heappush(heap, value)
    for idx in range(len(items)):
        items[idx] = heappop(heap)
    return items
