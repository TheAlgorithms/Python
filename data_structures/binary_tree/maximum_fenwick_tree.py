class MaxFenwickTree:
    """
    Maximum Fenwick Tree

    More info: https://cp-algorithms.com/data_structures/fenwick.html
    ---------
    >>> ft = MaxFenwickTree(5)
    >>> ft.query(0, 5)
    0
    >>> ft.update(4, 100)
    >>> ft.query(0, 5)
    100
    >>> ft.update(4, 0)
    >>> ft.update(2, 20)
    >>> ft.query(0, 5)
    20
    >>> ft.update(4, 10)
    >>> ft.query(2, 5)
    20
    >>> ft.query(1, 5)
    20
    >>> ft.update(2, 0)
    >>> ft.query(0, 5)
    10
    >>> ft = MaxFenwickTree(10000)
    >>> ft.update(255, 30)
    >>> ft.query(0, 10000)
    30
    >>> ft = MaxFenwickTree(6)
    >>> ft.update(5, 1)
    >>> ft.query(5, 6)
    1
    >>> ft = MaxFenwickTree(6)
    >>> ft.update(0, 1000)
    >>> ft.query(0, 1)
    1000

    Updating a smaller sibling preserves the maximum, including after decreases.
    >>> ft = MaxFenwickTree(8)
    >>> ft.update(4, 20)
    >>> ft.update(5, 1)
    >>> ft.query(0, 6)
    20
    >>> ft.update(4, 0)
    >>> ft.query(0, 6)
    1
    >>> ft.update(5, 0)
    >>> ft.query(0, 6)
    0

    Updating a child must also preserve the ancestor's own array value.
    >>> ft = MaxFenwickTree(8)
    >>> ft.update(5, 100)
    >>> ft.update(4, 0)
    >>> ft.query(0, 6)
    100
    """

    def __init__(self, size: int) -> None:
        """
        Create empty Maximum Fenwick Tree with specified size

        Parameters:
            size: size of Array

        Returns:
            None
        """
        self.size = size
        self.arr = [0] * size
        self.tree = [0] * size

    @staticmethod
    def get_next(index: int) -> int:
        """
        Get next index in O(1)
        """
        return index | (index + 1)

    @staticmethod
    def get_prev(index: int) -> int:
        """
        Get previous index in O(1)
        """
        return (index & (index + 1)) - 1

    def update(self, index: int, value: int) -> None:
        """
        Set index to value in O(lg^2 N)

        Parameters:
            index: index to update
            value: value to set

        Returns:
            None
        """
        old_value = self.arr[index]
        if value == old_value:
            return
        self.arr[index] = value
        while index < self.size:
            old_maximum = self.tree[index]
            if value > old_maximum:
                self.tree[index] = value
            elif old_value == old_maximum:
                current_left_border = self.get_prev(index) + 1
                maximum = self.arr[index]
                if current_left_border != index:
                    maximum = max(0, maximum)
                child = index - 1
                # These disjoint child buckets cover the rest of this bucket.
                while child >= current_left_border:
                    maximum = max(maximum, self.tree[child])
                    if maximum == old_maximum:
                        break
                    child = self.get_prev(child)
                self.tree[index] = maximum
                if maximum == old_maximum:
                    break
            else:
                # An unchanged bucket maximum leaves all its ancestors unchanged.
                break
            index = self.get_next(index)

    def query(self, left: int, right: int) -> int:
        """
        Answer the query of maximum range [l, r) in O(lg^2 N)

        Parameters:
            left: left index of query range (inclusive)
            right: right index of query range (exclusive)

        Returns:
            Maximum value of range [left, right)
        """
        right -= 1  # Because of right is exclusive
        result = 0
        while left <= right:
            current_left = self.get_prev(right)
            if left <= current_left:
                result = max(result, self.tree[right])
                right = current_left
            else:
                result = max(result, self.arr[right])
                right -= 1
        return result


if __name__ == "__main__":
    import doctest
    import sys
    from timeit import repeat

    doctest.testmod()

    # Run with --benchmark on each revision to compare the same 2,000-item workload.
    if "--benchmark" in sys.argv:
        size = 2000
        values = [(index * 97) % size for index in range(size)]
        updates = [(index, (index * 37) % size) for index in range(size)]
        updates += [(index, values[index]) for index in reversed(range(size))]
        queries = [(left, size) for left in range(size)]

        # Build correct query buckets outside the timer, even on the buggy revision.
        query_setup = """
tree = MaxFenwickTree(size)
tree.arr = values[:]
tree.tree = [
    max(values[tree.get_prev(index) + 1 : index + 1])
    for index in range(size)
]
"""
        for operation, statement, setup in (
            (
                "4000 updates",
                "for index, value in updates: tree.update(index, value)",
                "tree = MaxFenwickTree(size)",
            ),
            (
                "2000 queries",
                "for left, right in queries: tree.query(left, right)",
                query_setup,
            ),
        ):
            timings = repeat(
                statement, setup=setup, repeat=5, number=1, globals=globals()
            )
            print(f"{size} items, {operation}: {min(timings):.6f} seconds (best of 5)")
