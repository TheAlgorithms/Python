class FenwickTree:
    """
    >>> f = FenwickTree(100)
    >>> f.update(1, 20)
    >>> f.update(4, 4)
    >>> f.query(1)
    20
    >>> f.query(3)
    20
    >>> f.query(4)
    24
    >>> f.update(2, -5)
    >>> f.query(1)
    20
    >>> f.query(3)
    15
    """

    def __init__(self, SIZE: int):  # create fenwick tree with size SIZE
        self.Size = SIZE
        self.ft = [0] * SIZE

    def __lowbit(self, i: int) -> int:
        return i & (-i)

    def update(self, i: int, val):  # update data (adding) in index i in O(lg N)
        while i < self.Size:
            self.ft[i] += val
            i += self.__lowbit(i)

    def query(self, i: int):  # query cumulative data from index 0 to i in O(lg N)
        ret = 0
        while i > 0:
            ret += self.ft[i]
            i -= self.__lowbit(i)
        return ret


if __name__ == "__main__":
    from doctest import testmod

    testmod()
