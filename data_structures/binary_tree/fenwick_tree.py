from copy import deepcopy


class FenwickTree:
    """
    Fenwick Tree

    More info: https://en.wikipedia.org/wiki/Fenwick_tree
    """

    def __init__(self, arr: list[int] = None, size: int = None) -> None:
        """
        Constructor for the Fenwick tree

        Parameters:
            arr (list): list of elements to initialize the tree with (optional)
            size (int): size of the Fenwick tree (if arr is None)
        """

        if arr is None and size is not None:
            self.size = size
            self.tree = [0] * size
        elif arr is not None:
            self.init(arr)
        else:
            raise ValueError("Either arr or size must be specified")

    def init(self, arr: list[int]) -> None:
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
        self.tree = deepcopy(arr)
        for i in range(1, self.size):
            j = self.next(i)
            if j < self.size:
                self.tree[j] += self.tree[i]

    def get_array(self) -> list[int]:
        """
        Get the Normal Array of the Fenwick tree in O(N)

        Returns:
            list: Normal Array of the Fenwick tree

        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> f.get_array() == a
        True
        """
        arr = self.tree[:]
        for i in range(self.size - 1, 0, -1):
            j = self.next(i)
            if j < self.size:
                arr[j] -= arr[i]
        return arr

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

        >>> f = FenwickTree([1, 2, 3, 4, 5])
        >>> f.add(0, 1)
        >>> f.add(1, 2)
        >>> f.add(2, 3)
        >>> f.add(3, 4)
        >>> f.add(4, 5)
        >>> f.get_array()
        [2, 4, 6, 8, 10]
        """
        if index == 0:
            self.tree[0] += value
            return
        while index < self.size:
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

        >>> f = FenwickTree([5, 4, 3, 2, 1])
        >>> f.update(0, 1)
        >>> f.update(1, 2)
        >>> f.update(2, 3)
        >>> f.update(3, 4)
        >>> f.update(4, 5)
        >>> f.get_array()
        [1, 2, 3, 4, 5]
        """
        self.add(index, value - self.get(index))

    def prefix(self, right: int) -> int:
        """
        Prefix sum of all elements in [0, right) in O(lg N)

        Parameters:
            right (int): right bound of the query (exclusive)

        Returns:
            int: sum of all elements in [0, right)

        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     res = res and f.prefix(i) == sum(a[:i])
        >>> res
        True
        """
        if right == 0:
            return 0
        result = self.tree[0]
        right -= 1  # make right inclusive
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

        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     for j in range(i + 1, len(a)):
        ...         res = res and f.query(i, j) == sum(a[i:j])
        >>> res
        True
        """
        return self.prefix(right) - self.prefix(left)

    def get(self, index: int) -> int:
        """
        Get value at index in O(lg N)

        Parameters:
            index (int): index to get the value

        Returns:
            int: Value of element at index

        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     res = res and f.get(i) == a[i]
        >>> res
        True
        """
        return self.query(index, index + 1)

    def rank_query(self, value: int) -> int:
        """
        Find the largest index with prefix(i) <= value in O(lg N)
        NOTE: Requires that all values are non-negative!

        Parameters:
            value (int): value to find the largest index of

        Returns:
            -1: if value is smaller than all elements in prefix sum
            int: largest index with prefix(i) <= value

        >>> f = FenwickTree([1, 2, 0, 3, 0, 5])
        >>> f.rank_query(0)
        -1
        >>> f.rank_query(2)
        0
        >>> f.rank_query(1)
        0
        >>> f.rank_query(3)
        2
        >>> f.rank_query(5)
        2
        >>> f.rank_query(6)
        4
        >>> f.rank_query(11)
        5
        """
        value -= self.tree[0]
        if value < 0:
            return -1

        j = 1  # Largest power of 2 <= size
        while j * 2 < self.size:
            j *= 2

        i = 0

        while j > 0:
            if i + j < self.size and self.tree[i + j] <= value:
                value -= self.tree[i + j]
                i += j
            j //= 2
        return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
