"""
Retrieves the value of an 0-indexed 1D index from a 2D array.
There are two ways to retrieve value(s):

1. index_2d_array_in_1d(array: list[int], index: int) -> int
This function allows you to provide a 2D array and a 0-indexed 1D integer index,
and retrieves the integer value at that index.

2. Index2DArrayIterator(array) -> Iterator[int]
This iterator allows you to iterate through a 2D array by passing in the array and
calling __next__() on your iterator. You can also use the iterator in a loop.
Example:
[value for value in Index2DArrayIterator(array)]

Python doctests can be run using this command:
python3 -m doctest -v index_2d_array_in_1d.py
"""

from collections.abc import Iterator


class Index2DArrayIterator:
    """
    Creates an iterator to iterate through the values in the given 2D array.

    Args:
        array (List[int]): A 2D array of integers where all rows are the same size
        and all columns are the same size.
    """

    def __init__(self, array: list[list[int]]) -> None:
        self.array = array
        self.cols = len(array[0])
        self.n = len(array) * len(array[0])
        self.i = 0

    def __iter__(self) -> Iterator[int]:
        """
        >>> t = Index2DArrayIterator([[5],[-523],[-1],[34],[0]])
        >>> t.__iter__() is not None
        True
        """
        return self

    def __next__(self) -> int:
        """
        Returns the next item in the array.

        Returns:
            int: Value in array.

        >>> t = Index2DArrayIterator([[5],[-523],[-1],[34],[0]])
        >>> t.__next__()
        5
        >>> t.__next__()
        -523
        >>> u = Index2DArrayIterator([[5, 2, 25], [23, 14, 5], [324, -1, 0]])
        >>> [val for val in u]
        [5, 2, 25, 23, 14, 5, 324, -1, 0]
        """
        if self.i < self.n:
            x = self.array[self.i // self.cols][self.i % self.cols]
            self.i += 1
            return x
        else:
            raise StopIteration


def index_2d_array_in_1d(array: list[list[int]], index: int) -> int:
    """
    Retrieves the value of the one-dimensional index from a two-dimensional array.

    Args:
        array (List[int]): A 2D array of integers where all rows are the same size and
        all columns are the same size.
        index: A 1D index.

    Returns:
        int: The 0-indexed value of the 1D index in the array.

    Examples:
        >>> index_2d_array_in_1d([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], 5)
        5
        >>> index_2d_array_in_1d([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], -1)
        Traceback (most recent call last):
        ...
        ValueError: index out of range
        >>> index_2d_array_in_1d([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], 12)
        Traceback (most recent call last):
        ...
        ValueError: index out of range
        >>> index_2d_array_in_1d([[]], 0)
        Traceback (most recent call last):
        ...
        ValueError: no items in array
    """
    rows = len(array)
    cols = len(array[0])

    if rows == 0 or cols == 0:
        raise ValueError("no items in array")

    if index < 0 or index >= rows * cols:
        raise ValueError("index out of range")

    return array[index // cols][index % cols]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
