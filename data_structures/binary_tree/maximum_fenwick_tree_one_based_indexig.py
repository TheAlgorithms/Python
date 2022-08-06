class MaxFenwickTreeOneBasedIndexing:
    """
    Maximum Fenwick Tree with One-Based Indexing
    ---------
    >>> ft = MaxFenwickTreeOneBasedIndexing(5)
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
    >>> ft = MaxFenwickTreeOneBasedIndexing(10000)
    >>> ft.update(255, 30)
    >>> ft.query(0, 10000)
    30
    """

    def __init__(self, size: int) -> None:
        """
        Create empty One-Based indexing Maximum Fenwick Tree with specified size

        Parameters:
            size: size of Array

        Returns:
            None
        """
        self.size = size
        self.arr = [0] * (size + 1)
        self.tree = [0] * (size + 1)

    def update(self, index: int, value: int) -> None:
        """
        Set index to value in O(lg^2 N)

        Parameters:
            index: index to update
            value: value to set

        Returns:
            None
        """
        self.arr[index] = value
        while index < self.size:
            self.tree[index] = max(value, self.query(index - index & -index, index))
            index += index & (-index)

    def query(self, left: int, right: int) -> int:
        """
        Answer the query of maximum range (l, r] in O(lg^2 N)

        Parameters:
            left: left index of query range (exclusive)
            right: right index of query range (inclusive)

        Returns:
            Maximum value of range (left, right]
        """
        result = 0
        while left < right:
            current_left = right - right & -right
            if left < current_left:
                result = max(result, self.tree[right])
                right = current_left
            else:
                result = max(result, self.arr[right])
                right -= 1
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
