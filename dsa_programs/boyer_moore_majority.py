"""Boyer-Moore majority vote algorithm."""

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def boyer_moore_majority(items: Iterable[T]) -> T:
    data: List[T] = list(items)
    if not data:
        raise ValueError("Sequence is empty")
    candidate: T | None = None
    count = 0
    for value in data:
        if count == 0:
            candidate = value
            count = 1
        elif value == candidate:
            count += 1
        else:
            count -= 1
    assert candidate is not None  # mypy helper
    if data.count(candidate) <= len(data) // 2:
        raise ValueError("No majority element present")
    return candidate
