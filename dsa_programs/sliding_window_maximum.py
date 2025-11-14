"""Sliding window maximum using a deque."""

from collections import deque
from typing import Deque, Iterable, List


def sliding_window_maximum(values: Iterable[int], window: int) -> List[int]:
    if window <= 0:
        raise ValueError("Window size must be positive")
    data = list(values)
    if window > len(data):
        raise ValueError("Window larger than data length")
    max_indices: Deque[int] = deque()
    result: List[int] = []
    for idx, value in enumerate(data):
        while max_indices and max_indices[0] <= idx - window:
            max_indices.popleft()
        while max_indices and data[max_indices[-1]] <= value:
            max_indices.pop()
        max_indices.append(idx)
        if idx >= window - 1:
            result.append(data[max_indices[0]])
    return result
