"""Kadane's algorithm to find maximum subarray sum."""

from typing import Iterable


def kadane_max_subarray(values: Iterable[int]) -> int:
    iterator = iter(values)
    try:
        first = next(iterator)
    except StopIteration as exc:  # pragma: no cover - defensive
        raise ValueError("Iterable is empty") from exc
    max_ending_here = max_so_far = first
    for value in iterator:
        max_ending_here = max(value, max_ending_here + value)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
