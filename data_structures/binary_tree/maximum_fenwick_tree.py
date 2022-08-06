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

    def __init__(self, n: int):  # Create Fenwick tree with size n
        self.n = n
        self.arr = [0] * (n + 1)
        self.tree = [0] * (n + 1)

    def update(
        self, i, val
    ) -> None:  # Set value of index i (1-Based) to val in O(lg^2 N)
        self.arr[i] = val
        while i < self.n:
            self.tree[i] = max(val, self.query(i, i - i & -i))
            i += i & (-i)

    def query(
        self, l, r
    ) -> int:  # Query maximum value from range (l, r] (1-Based) in O(lg N)
        res = 0
        while l < r:
            ll = r - r & -r
            if l < ll:
                res = max(res, self.tree[r])
                r = ll
            else:
                res = max(res, self.arr[r])
                r -= 1
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
