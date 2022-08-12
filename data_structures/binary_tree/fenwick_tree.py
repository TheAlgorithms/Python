from typing import List


class FenwickTree:
    """
    Fenwick Tree

    More info: https://en.wikipedia.org/wiki/Fenwick_tree

    >>> f = FenwickTree(size=10)
    >>> f.query(0, 10)
    0
    >>> f.add(9, 10)
    >>> f.prefix(10)
    10
    >>> f.add(9, -10)
    >>> f.add(1, 20)
    >>> f.query(0, 1)
    0
    >>> f.query(1, 10)
    20
    >>> f.query(0, 10)
    20
    >>> f.update(2, 10)
    >>> f.query(0, 2)
    20
    >>> f.query(2, 3)
    10
    >>> f.query(0, 10)
    30
    """

    def __init__(self, arr: List[int] = None, size: int = None):
        """
        Constructor for the Fenwick tree

        Parameters:
            arr (list): list of elements to initialize the tree with (optional)
            size (int): size of the Fenwick tree (if arr is None)
        """

        if arr is None and size is not None:
            self.size = size
            self.tree = [0] * (size + 1)
        elif arr is not None:
            self.init(arr)
        else:
            raise ValueError("Either arr or size must be specified")

    def init(self, arr: List[int]) -> None:
        """
        Initialize the Fenwick tree with arr in O(N)

        Parameters:
            arr (list): list of elements to initialize the tree with

        Returns:
            None

        >>> a = [1, 2, 3, 4, 5]
        >>> f1 = FenwickTree(a)
        >>> f2 = FenwickTree(size=len(a))
        >>> for index, value in enumerate(a):
        ...     f2.add(index, value)
        >>> f1.tree == f2.tree
        True
        """
        self.size = len(arr)
        self.tree = [0] + arr
        for i in range(1, self.size + 1):
            j = self.next(i)
            if j < self.size + 1:
                self.tree[j] += self.tree[i]

    @staticmethod
    def next(index: int) -> int:
        return index + (index & (-index))

    @staticmethod
    def prev(index: int) -> int:
        return index - (index & (-index))

    def add(self, index: int, value: int) -> None:
        """
        Add a value to index in O(lg N)

        Parameters:
            index (int): index to add value to
            value (int): value to add to index

        Returns:
            None
        """
        index += 1  # 1-indexed
        while index < self.size + 1:
            self.tree[index] += value
            index = self.next(index)

    def update(self, index: int, value: int) -> None:
        """
        Set the value of index in O(lg N)

        Parameters:
            index (int): index to set value to
            value (int): value to set in index

        Returns:
            None
        """
        self.add(index, value - self.get(index))

    def prefix(self, right: int) -> int:
        """
        Prefix sum of all elements in [0, right) in O(lg N)

        Parameters:
            right (int): right bound of the query (exclusive)

        Returns:
            int: sum of all elements in [0, right)
        """
        result = 0
        while right > 0:
            result += self.tree[right]
            right = self.prev(right)
        return result

    def query(self, left: int, right: int) -> int:
        """
        Query the sum of all elements in [left, right) in O(lg N)

        Parameters:
            left (int): left bound of the query (inclusive)
            right (int): right bound of the query (exclusive)

        Returns:
            int: sum of all elements in [left, right)
        """
        return self.prefix(right) - self.prefix(left)

    def get(self, index: int) -> int:
        """
        Get value at index in O(lg N)

        Parameters:
            index (int): index to get the value

        Returns:
            int: Value of element at index
        """
        return self.query(index, index + 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
