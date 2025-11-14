"""In-place Dutch national flag partitioning for values 0, 1, and 2."""

from typing import MutableSequence


def dutch_national_flag(items: MutableSequence[int]) -> None:
    low = mid = 0
    high = len(items) - 1
    while mid <= high:
        value = items[mid]
        if value == 0:
            items[low], items[mid] = items[mid], items[low]
            low += 1
            mid += 1
        elif value == 1:
            mid += 1
        elif value == 2:
            items[mid], items[high] = items[high], items[mid]
            high -= 1
        else:
            raise ValueError("Items must be 0, 1, or 2 only")
