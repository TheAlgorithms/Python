class FenwickTree:
    """
    Fenwick Tree

    More info: https://en.wikipedia.org/wiki/Fenwick_tree

    >>> f = FenwickTree(10)
    >>> f.query(10)
    0
    >>> f.update(1, 20)
    >>> f.query(1)
    0
    >>> f.query(2)
    20
    >>> f.query(3)
    20
    >>> f.update(2, 10)
    >>> f.query(2)
    20
    >>> f.query(3)
    30
    >>> f.query(10)
    30
    """

    def __init__(self, size: int):
        """
        Initialize a Fenwick tree with size elements
        """
        self.size = size
        self.tree = [0] * (size + 1)

    @staticmethod
    def next(index: int):
        return index + (index & (-index))

    @staticmethod
    def prev(index: int):
        return index - (index & (-index))

    def update(self, index: int, value: int):
        """
        Add a value to index in O(lg N)
        """
        index += 1  # 1-indexed
        while index < self.size:
            self.tree[index] += value
            index = self.next(index)

    def query(self, right: int):
        """
        Query the sum of all elements in [0, right) in O(lg N)
        """
        result = 0
        while right > 0:
            result += self.tree[right]
            right = self.prev(right)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
