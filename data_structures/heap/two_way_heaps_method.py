"""
two way heaps method is a technique used to efficiently maintain and retrieve the median of a stream of numbers (array of integers).

this method uses both max and min heap , max heap is used to store the smaller half of the numbers while min heap is used to store
larger number.

this arrangement helps us in retrieving the median of a stream of numbers easily and the time complexity of algorithm is constant [O(1)].
In brute-force method time complexity of this medianfinder algorithm would be O(n logn)

a medium article to better understand this algorithm

https://stephenjoel2k.medium.com/two-heaps-min-heap-max-heap-c3d32cbb671d

"""


import heapq
from typing import Union


class MedianFinder:
    def __init__(self) -> None:
        """
        Initialize the MedianFinder with empty max and min heaps.
        
        Examples:
            >>> median_finder = MedianFinder()
        """
        self.maxheap = []
        self.minheap = []

    def insert(self, value: Union[int, float]) -> None:
        """
        Insert a value into the max and min heaps.

        Args:
            value (int | float): A number to be inserted in the heap.

        Examples:
            >>> median_finder = MedianFinder()
            >>> median_finder.insert(10)
            >>> median_finder.insert(20)
        """
        if not self.maxheap or value <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -value)
        else:
            heapq.heappush(self.minheap, value)

        if len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def find_median(self) -> Union[int, float]:
        """
        Find the median of the stream of numbers.

        Returns:
            int | float: The median of the stream.

        Examples:
            >>> median_finder = MedianFinder()
            >>> median_finder.insert(5)
            >>> median_finder.insert(8)
            >>> median_finder.insert(2)
            >>> median_finder.insert(10)
            >>> median_finder.insert(1)
            >>> median_finder.insert(7)
            >>> median_finder.insert(6)
            >>> median_finder.find_median()
            6
        """
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        return self.minheap[0]

def main() -> None:
    """
    Run the example with a stream of numbers.

    Returns:
        None
    """
    median_finder = MedianFinder()

    stream_of_numbers = [5, 8, 2, 10, 1, 7, 6]

    for value in stream_of_numbers:
        median_finder.insert(value)

    median = median_finder.find_median()
    print("Median:", median)  # Median = 6.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
