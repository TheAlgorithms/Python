"""
The two heaps method is used to efficiently maintain and retrieve the median of a
stream of numbers (array of integers).  It uses max_heap and min_heap where the
max_heap is used to store the smaller half of the numbers while min_heap is used to
store larger numbers.

This arrangement helps us to easliy retrieve the median of a stream of numbers and the
time complexity of algorithm is constant [O(1)].  In brute-force method time complexity
of this medianfinder algorithm would be O(n logn)

A medium article to better understand this algorithm
https://stephenjoel2k.medium.com/two-heaps-min-heap-max-heap-c3d32cbb671d
"""
import heapq
from dataclasses import dataclass, field
from typing import Self


@dataclass
class MedianFinder:
    """
    A class for finding the median of a stream of numbers using two heaps.

    Examples:
        >>> median_finder = MedianFinder()
        >>> median_finder
        MedianFinder(max_heap=[], min_heap=[])
        >>> median_finder.insert_many((5, 8, 2, 10, 1, 7, 6))
        MedianFinder(max_heap=[-5, -2, -1], min_heap=[6, 7, 8, 10])
    """

    max_heap: list[float] = field(default_factory=list)
    min_heap: list[float] = field(default_factory=list)

    def insert(self, value: float) -> Self:
        """
        Insert a value into the max and min heaps.

        Args:
            value: A number to be inserted in the heap.

        Examples:
            >>> median_finder = MedianFinder()
            >>> median_finder
            MedianFinder(max_heap=[], min_heap=[])
            >>> median_finder.insert(5)
            MedianFinder(max_heap=[-5], min_heap=[])
            >>> median_finder.insert(8)
            MedianFinder(max_heap=[-5], min_heap=[8])
        """
        if not self.max_heap or value <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -value)
        else:
            heapq.heappush(self.min_heap, value)

        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        return self

    def insert_many(self, values: list[float] | tuple[float, ...]) -> Self:
        """
        Insert multiple values into the max and min heaps.

        Args:
            values: A list of numbers to be inserted in the heap.

        Examples:
            >>> MedianFinder().insert_many((5, 8, 2, 10, 1, 7, 6))
            MedianFinder(max_heap=[-5, -2, -1], min_heap=[6, 7, 8, 10])
        """
        for value in values:
            self.insert(value)
        return self

    def find_median(self) -> float:
        """
        Find the median of the stream of numbers.

        Returns:
            int | float: The median of the stream.

        Examples:
            >>> MedianFinder().find_median()
            Traceback (most recent call last):
                ...
            IndexError: list index out of range
            >>> MedianFinder().insert_many((5, 8, 2, 10, 1, 7, 6)).find_median()
            6
        """
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return self.min_heap[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    median_finder = MedianFinder().insert_many((5, 8, 2, 10, 1, 7, 6))
    print(f"{median_finder}.find_median() = {median_finder.find_median()}")
    # MedianFinder(max_heap=[-5, -2, -1], min_heap=[6, 7, 8, 10]).find_median() = 6
