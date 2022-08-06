class MaxFenwickTree:
    """
    Maximum Fenwick Tree
    ---------
    >>> ft = MaxFenwickTree(5)
    >>> ft.query(0, 5)
    0
    >>> ft.update(2, 20)
    >>> ft.query(0, 5)
    20
    >>> ft.update(5, 10)
    >>> ft.query(2, 5)
    10
    >>> ft.update(2, 0)
    >>> ft.query(0, 5)
    10
    """

    def __init__(self, size: int) -> None:  # Create Fenwick tree with specified size
        self.size = size
        self.arr = [0] * (size + 1)
        self.tree = [0] * (size + 1)

    def update(
        self, index: int, value: int
    ) -> None:  # Set index (1-Based) to value in O(lg^2 N)
        self.arr[index] = value
        while index < self.size:
            self.tree[index] = max(value, self.query(index, index - index & -index))
            index += index & (-index)

    def query(
        self, left: int, right: int
    ) -> int:  # Query maximum value from range (left, right] (1-Based) in O(lg N)
        res = 0
        while left < right:
            x = right - right & -right
            if left < x:
                res = max(res, self.tree[right])
                right = x
            else:
                res = max(res, self.arr[right])
                right -= 1
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
