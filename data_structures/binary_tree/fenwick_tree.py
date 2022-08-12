class FenwickTree:
    """
    Fenwick Tree

    More info: https://en.wikipedia.org/wiki/Fenwick_tree

    >>> f = FenwickTree(10)
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

    def __init__(self, size: int):
        """
        Initialize a Fenwick tree with size elements

        Parameters:
            size (int): size of the Fenwick tree
        """
        self.size = size
        self.tree = [0] * (size + 1)

    @staticmethod
    def next(index: int):
        return index + (index & (-index))

    @staticmethod
    def prev(index: int):
        return index - (index & (-index))

    def add(self, index: int, value: int):
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

    def update(self, index: int, value: int):
        """
        Set the value of index in O(lg N)

        Parameters:
            index (int): index to set value to
            value (int): value to set in index

        Returns:
            None
        """
        self.add(index, value - self.query(index, index + 1))

    def prefix(self, right: int):
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

    def query(self, left: int, right: int):
        """
        Query the sum of all elements in [left, right) in O(lg N)

        Parameters:
            left (int): left bound of the query (inclusive)
            right (int): right bound of the query (exclusive)

        Returns:
            int: sum of all elements in [left, right)
        """
        return self.prefix(right) - self.prefix(left)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
