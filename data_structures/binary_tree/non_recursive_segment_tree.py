"""
A non-recursive Segment Tree implementation with range query and single element update,
works virtually with any list of the same type of elements with a "commutative"
combiner.

Explanation:
https://www.geeksforgeeks.org/iterative-segment-tree-range-minimum-query/
https://www.geeksforgeeks.org/segment-tree-efficient-implementation/

>>> SegmentTree([1, 2, 3], lambda a, b: a + b).query(0, 2)
6
>>> SegmentTree([3, 1, 2], min).query(0, 2)
1
>>> SegmentTree([2, 3, 1], max).query(0, 2)
3
>>> st = SegmentTree([1, 5, 7, -1, 6], lambda a, b: a + b)
>>> st.update(1, -1)
>>> st.update(2, 3)
>>> st.query(1, 2)
2
>>> st.query(1, 1)
-1
>>> st.update(4, 1)
>>> st.query(3, 4)
0
>>> st = SegmentTree([[1, 2, 3], [3, 2, 1], [1, 1, 1]], lambda a, b: [a[i] + b[i] for i
...                                                                   in range(len(a))])
>>> st.query(0, 1)
[4, 4, 4]
>>> st.query(1, 2)
[4, 3, 2]
>>> st.update(1, [-1, -1, -1])
>>> st.query(1, 2)
[0, 0, 0]
>>> st.query(0, 2)
[1, 2, 3]
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")


class SegmentTree[T]:
    def __init__(self, arr: list[T], fnc: Callable[[T, T], T]) -> None:
        """
        Segment Tree constructor, it works just with commutative combiner.
        :param arr: list of elements for the segment tree
        :param fnc: commutative function for combine two elements

        >>> SegmentTree(['a', 'b', 'c'], lambda a, b: f'{a}{b}').query(0, 2)
        'abc'
        >>> SegmentTree([(1, 2), (2, 3), (3, 4)],
        ...             lambda a, b: (a[0] + b[0], a[1] + b[1])).query(0, 2)
        (6, 9)
        """
        any_type: Any | T = None

        self.N: int = len(arr)
        self.st: list[T] = [any_type for _ in range(self.N)] + arr
        self.fn = fnc
        self.build()

    def build(self) -> None:
        for p in range(self.N - 1, 0, -1):
            self.st[p] = self.fn(self.st[p * 2], self.st[p * 2 + 1])

    def update(self, p: int, v: T) -> None:
        """
        Update an element in log(N) time
        :param p: position to be update
        :param v: new value

        >>> st = SegmentTree([3, 1, 2, 4], min)
        >>> st.query(0, 3)
        1
        >>> st.update(2, -1)
        >>> st.query(0, 3)
        -1
        """
        p += self.N
        self.st[p] = v
        while p > 1:
            p = p // 2
            self.st[p] = self.fn(self.st[p * 2], self.st[p * 2 + 1])

    def query(self, left: int, right: int) -> T | None:
        """
        Get range query value in log(N) time
        :param left: left element index
        :param right: right element index
        :return: element combined in the range [left, right]

        >>> st = SegmentTree([1, 2, 3, 4], lambda a, b: a + b)
        >>> st.query(0, 2)
        6
        >>> st.query(1, 2)
        5
        >>> st.query(0, 3)
        10
        >>> st.query(2, 3)
        7
        """
        left, right = left + self.N, right + self.N

        res: T | None = None
        while left <= right:
            if left % 2 == 1:
                res = self.st[left] if res is None else self.fn(res, self.st[left])
            if right % 2 == 0:
                res = self.st[right] if res is None else self.fn(res, self.st[right])
            left, right = (left + 1) // 2, (right - 1) // 2
        return res


if __name__ == "__main__":
    from functools import reduce

    test_array = [1, 10, -2, 9, -3, 8, 4, -7, 5, 6, 11, -12]

    test_updates = {
        0: 7,
        1: 2,
        2: 6,
        3: -14,
        4: 5,
        5: 4,
        6: 7,
        7: -10,
        8: 9,
        9: 10,
        10: 12,
        11: 1,
    }

    min_segment_tree = SegmentTree(test_array, min)
    max_segment_tree = SegmentTree(test_array, max)
    sum_segment_tree = SegmentTree(test_array, lambda a, b: a + b)

    def test_all_segments() -> None:
        """
        Test all possible segments
        """
        for i in range(len(test_array)):
            for j in range(i, len(test_array)):
                min_range = reduce(min, test_array[i : j + 1])
                max_range = reduce(max, test_array[i : j + 1])
                sum_range = reduce(lambda a, b: a + b, test_array[i : j + 1])
                assert min_range == min_segment_tree.query(i, j)
                assert max_range == max_segment_tree.query(i, j)
                assert sum_range == sum_segment_tree.query(i, j)

    test_all_segments()

    for index, value in test_updates.items():
        test_array[index] = value
        min_segment_tree.update(index, value)
        max_segment_tree.update(index, value)
        sum_segment_tree.update(index, value)
        test_all_segments()
