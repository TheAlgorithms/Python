"""
Coordinate Compression Algorithm

Coordinate compression reduces the range of numeric values while
preserving their relative order. Useful in ranking, coordinate
mapping, or segment trees.

Example:
    >>> compressor = CoordinateCompressor([100, 200, 300])
    >>> compressor.compress(200)
    1
    >>> compressor.decompress(1)
    200
    >>> compressor.compress(400)
    Traceback (most recent call last):
        ...
    ValueError: Value 400 not found in original data.

Reference:
    https://en.wikipedia.org/wiki/Coordinate_compression
"""

from bisect import bisect_left
from typing import List


class CoordinateCompressor:
    """
    Class for coordinate compression and decompression.

    Attributes:
        values (List[int]): Sorted list of unique input values.
    """

    def __init__(self, values: List[int]) -> None:
        """
        Initialize the compressor with a list of values.

        Args:
            values: List of integers to compress.

        Raises:
            ValueError: If input list is empty.

        >>> CoordinateCompressor([5, 3, 8, 3]).values
        [3, 5, 8]
        """
        if not values:
            raise ValueError("Input list cannot be empty.")
        self.values = sorted(set(values))

    def compress(self, value: int) -> int:
        """
        Compress a value to its index in the sorted unique list.

        Args:
            value: Value to compress.

        Returns:
            Index of value in the sorted list.

        Raises:
            ValueError: If value is not present.

        >>> comp = CoordinateCompressor([10, 20, 30])
        >>> comp.compress(20)
        1
        >>> comp.compress(40)
        Traceback (most recent call last):
            ...
        ValueError: Value 40 not found in original data.
        """
        index = bisect_left(self.values, value)
        if index < len(self.values) and self.values[index] == value:
            return index
        raise ValueError(f"Value {value} not found in original data.")

    def decompress(self, index: int) -> int:
        """
        Decompress an index back to its original value.

        Args:
            index: Compressed index.

        Returns:
            Original value.

        Raises:
            ValueError: If index is out of bounds.

        >>> comp = CoordinateCompressor([1, 2, 3])
        >>> comp.decompress(0)
        1
        >>> comp.decompress(3)
        Traceback (most recent call last):
            ...
        ValueError: Invalid index: 3. Must be between 0 and 2.
        """
        if not 0 <= index < len(self.values):
            raise ValueError(
                f"Invalid index: {index}. Must be between 0 and {len(self.values) - 1}."
            )
        return self.values[index]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("✅ All doctests passed!")
