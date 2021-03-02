from typing import List


class FenwickTree:
    """
    A Fenwick tree or binary indexed tree.

    https://en.wikipedia.org/wiki/Fenwick_tree
    """

    def __init__(self, size: int, data: List[int] = None) -> None:
        """
        Init Fenwick Tree of the fixed size.

        If `data` is provided the tree builds on it in O(NlogN).

        >>> data = [x ** 2 for x in range(10)] # [0, 1, 4, 9, ..., 81]
        >>> tree = FenwickTree(10, data)
        >>> tree.query(1, 4) # sum of [1, 4, 9]
        14
        """

        self.size = size
        self.ft = [0] * size
        if data is not None:
            for i, value in enumerate(data):
                self.add(i, value)

    def add(self, ind: int, value: int) -> None:
        """
        Add `value` in index `ind` in O(logN).

        >>> tree = FenwickTree(10)
        >>> tree.add(3, 7)
        >>> tree.add(3, 7)
        >>> tree.query(3, 4)
        14
        """

        while ind < self.size:
            self.ft[ind] += value
            ind = ind | (ind + 1)

    def set(self, ind: int, value: int) -> None:
        """
        Set `value` in index `ind` in O(logN).

        >>> tree = FenwickTree(10)
        >>> tree.set(3, 7)
        >>> tree.set(3, 7)
        >>> tree.query(3, 4)
        7
        """

        delta = value - self.ft[ind]
        self.add(ind, delta)

    def __query(self, ind: int) -> int:
        """
        Query data in [0, i] in O(logN).
        """

        ret = 0
        while ind > 0:
            ret += self.ft[ind]
            ind = (ind & (ind + 1)) - 1
        return ret

    def query(self, left: int, right: int = None) -> int:
        """
        Query data in [left, right) or in [0, left) if right is not provided in
        O(logN).

        >>> data = [x ** 2 for x in range(10)] # [0, 1, 4, 9, ..., 81]
        >>> tree = FenwickTree(10, data)
        >>> tree.query(4) # sum of [0, 1, 4, 9]
        14
        >>> tree.query(0, 4) == tree.query(4)
        True
        """

        left = left - 1
        if right is None:
            return self.__query(left)
        right = right - 1
        return self.__query(right) - self.__query(left)


if __name__ == "__main__":
    fenwick_tree = FenwickTree(100)
    fenwick_tree.add(3, 7)
    fenwick_tree.add(3, 7)
    fenwick_tree.add(3, 7)
    fenwick_tree.add(4, 10)
    print(fenwick_tree.query(3, 10))
    fenwick_tree.add(3, -21)
    fenwick_tree.set(1, 1234)
    print(fenwick_tree.query(10))
