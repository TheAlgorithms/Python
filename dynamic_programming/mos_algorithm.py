"""
A method for answering a series of range queries on the same array.

Running time and space complexity of this method are:
 * Preprocess - O(n)
 * Answering m queries - O((n + m) * sqrt(n) * f) where f is the time complexity
                         of changing one of the range boundaries by +/- 1
 * Space complexity is O(n + m)


For more explanations :
 * https://www.hackerearth.com/practice/notes/mos-algorithm/
"""

import math
from abc import ABC, abstractmethod
from functools import cmp_to_key
from typing import List, Tuple, Union, Type

START = 0
END = 1
QUERY = 0


class MosOperation:
    """
    A template class for operations used by Mo's algorithm.
    It provides methods for moving both boundaries of the query's range
    See examples of specific operations below

    Parameters
    ---------

    arr: list/tuple, array of items to perform queries on.
    first_start_id: int, the id of the first query's left boundary

    """
    def __init__(self, arr: Union[List, Tuple], first_start_id: int) -> None:
        if first_start_id < 0 or first_start_id >= len(arr):
            raise ValueError("Invalid first start id {0}".format(
                first_start_id))

        self.arr = arr
        self.len = len(arr)
        self.cur_start = first_start_id
        self.cur_end = self.cur_start
        self.init_first_position()

    def init_first_position(self) -> None:
        """
        init first position

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = MosOperation(input_array, first_start_id=0)
        >>> sir_operation.init_first_position()
        """
        pass

    def move_start(self, new_loc: int) -> None:
        """
        Since it's a skelaton class only checks the validity of new_loc

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = MosOperation(input_array, first_start_id=2)
        >>> sir_operation.move_start(0)
        >>> sir_operation.move_start(100)
        Traceback (most recent call last):
            ...
        ValueError: Invalid location of start: 100
        """
        if new_loc < 0 or new_loc >= self.len:
            raise ValueError(f"Invalid location of start: {new_loc}")

    def move_end(self, new_loc: int) -> None:
        """
        Since it's a skelaton class only checks the validity of new_loc

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = MosOperation(input_array, first_start_id=2)
        >>> sir_operation.move_end(4)
        >>> sir_operation.move_end(100)
        Traceback (most recent call last):
            ...
        ValueError: Invalid location of end: 100
        """
        if new_loc < 0 or new_loc >= self.len:
            raise ValueError(f"Invalid location of end: {new_loc}")


class UniqueItemsInRange(MosOperation):
    """
    An operation for calculating number of unique items in range.
    This operation can be used in Mo's algorithm.
    It provides methods for moving both boundaries of the query's range
    See examples of specific operations below

    Parameters
    ---------

    arr: list/tuple, array of items to perform queries on.
    first_start_id: int, the id of the first query's left boundary

    """
    def __init__(self, arr: Union[List, Tuple], first_start_id: int) -> None:
        self.num_unique_items = 0
        self.unique_items_count = dict()
        super().__init__(arr, first_start_id)

    def _enlarge_range(self, added_id: int) -> None:
        """
        process range enlarged by 1 element

        Parameters
        ---------

        added_id: int, the id of the added item

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = UniqueItemsInRange(input_array, first_start_id=0)
        >>> sir_operation.move_end(3)
        2
        >>> sir_operation._enlarge_range(4)
        >>> sir_operation.num_unique_items
        3
        """

        new_value = self.arr[added_id]
        if new_value in self.unique_items_count.keys():
            self.unique_items_count[new_value] += 1
        else:
            self.unique_items_count[new_value] = 1

        if self.unique_items_count[new_value] == 1:
            self.num_unique_items += 1

    def _reduce_range(self, reduced_id: int) -> None:
        """
        process range reduced by 1 elemnt

        Parameters
        ---------

        reduced_id: int, the id of the reduced item

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = UniqueItemsInRange(input_array, first_start_id=0)
        >>> sir_operation.move_end(2)
        2
        >>> sir_operation._reduce_range(2)
        >>> sir_operation.num_unique_items
        1
        """
        reduced_value = self.arr[reduced_id]
        self.unique_items_count[reduced_value] -= 1

        if self.unique_items_count[reduced_value] == 0:
            self.num_unique_items -= 1

    def init_first_position(self) -> None:
        """
        init the first position

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = UniqueItemsInRange(input_array, first_start_id=4)
        >>> sir_operation.cur_start
        4
        >>> sir_operation.cur_end
        4
        >>> sir_operation.num_unique_items
        1
        """
        self.num_unique_items = 1
        first_value = self.arr[self.cur_start]
        self.unique_items_count[first_value] = 1

    def move_start(self, new_loc: int) -> int:
        """
        set the range's left boundary

        Parameters
        ---------

        new_loc: int, the id of the new location of the range's left boundary

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = UniqueItemsInRange(input_array, first_start_id=2)
        >>> sir_operation.move_start(new_loc=0)
        2
        >>> sir_operation.num_unique_items
        2
        >>> sir_operation.cur_start
        0
        """
        super().move_start(new_loc)
        step = new_loc - self.cur_start
        if step < 0:
            for _ in range(-step):
                self.cur_start -= 1
                self._enlarge_range(self.cur_start)

        elif step > 0:
            for _ in range(step):
                self._reduce_range(self.cur_start)
                self.cur_start += 1

        return self.num_unique_items

    def move_end(self, new_loc: int) -> int:
        """
        set the range's right boundary

        Parameters
        ---------

        new_loc: int, the id of the new location of the range's right boundary

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = UniqueItemsInRange(input_array, first_start_id=0)
        >>> sir_operation.move_end(new_loc=2)
        2
        >>> sir_operation.num_unique_items
        2
        >>> sir_operation.cur_end
        2
        """
        super().move_end(new_loc)
        step = new_loc - self.cur_end
        if step < 0:
            for _ in range(-step):
                self._reduce_range(self.cur_end)
                self.cur_end -= 1

        elif step > 0:
            for _ in range(step):
                self.cur_end += 1
                self._enlarge_range(self.cur_end)

        return self.num_unique_items


class SumInRange(MosOperation):
    """
    An operation for sum elements in range.
    This operation can be used in Mo's algorithm.
    It provides methods for moving both boundaries of the query's range
    See examples of specific operations below

    Parameters
    ---------

    arr: list/tuple, array of items to perform queries on.
    first_start_id: int, the id of the first query's left boundary

    """
    def __init__(self, arr: Union[List, Tuple], first_start_id: int) -> None:
        self.cur_sum = 0
        super().__init__(arr, first_start_id)

    def init_first_position(self) -> None:
        """
        init the first position

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = SumInRange(input_array, first_start_id=4)
        >>> sir_operation.cur_start
        4
        >>> sir_operation.cur_end
        4
        >>> sir_operation.cur_sum
        3
        """
        self.cur_sum = self.arr[self.cur_start]

    def move_start(self, new_loc: int) -> int:
        """
        set the range's left boundary

        Parameters
        ---------

        new_loc: int, the id of the new location of the range's left boundary

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = SumInRange(input_array, first_start_id=2)
        >>> sir_operation.move_start(new_loc=0)
        4
        >>> sir_operation.cur_sum
        4
        >>> sir_operation.cur_start
        0
        """
        super().move_start(new_loc)
        step = new_loc - self.cur_start
        if step < 0:
            for _ in range(-step):
                self.cur_start -= 1
                self.cur_sum += self.arr[self.cur_start]

        elif step > 0:
            for _ in range(step):
                self.cur_sum -= self.arr[self.cur_start]
                self.cur_start += 1

        return self.cur_sum

    def move_end(self, new_loc: int) -> int:
        """
        set the range's right boundary

        Parameters
        ---------

        new_loc: int, the id of the new location of the range's right boundary

        Examples
        -------
        >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
        >>> sir_operation = SumInRange(input_array, first_start_id=0)
        >>> sir_operation.move_end(new_loc=2)
        4
        >>> sir_operation.cur_sum
        4
        >>> sir_operation.cur_end
        2
        """
        super().move_end(new_loc)
        step = new_loc - self.cur_end
        if step < 0:
            for _ in range(-step):
                self.cur_sum -= self.arr[self.cur_end]
                self.cur_end -= 1

        elif step > 0:
            for _ in range(step):
                self.cur_end += 1
                self.cur_sum += self.arr[self.cur_end]

        return self.cur_sum


class MosAlgorithm:
    """
    A generic algorithm/idea for answering multiple range queries on the same
    array efficiently. It does so by performing the queries in a way which
    maximizes the relevance of each query to the one answered right after it.

    Parameters
    ---------

    arr: list/tuple, array of items to perform queries on.
    queries: tuple of ints, (start, end) defines ranges to query on

    Examples
    -------
    >>> input_array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    >>> queries = [(0, 4), (1, 3), (2, 4)]
    >>> case1 = MosAlgorithm(input_array, queries)
    >>> case1.run_queries(UniqueItemsInRange)
    [3, 2, 3]
    >>> case1.run_queries(SumInRange)
    [8, 4, 6]

    """
    def __init__(self, arr: Union[List, Tuple], queries: List[Tuple[int, int]])\
            -> None:
        self.len, self.len_sqrt = len(arr), int(math.ceil(math.sqrt(len(arr))))
        self.num_queries = len(queries)
        self.arr = arr

        if any([(q[START] < 0) or (q[END] >= self.len) or (q[START] > q[END])
                for q in queries]):
            raise ValueError("At least one of the queries is invalid")

        self.comparator = cmp_to_key(self._compartor_processed)

        # process queries to maintain original order mapping which will
        # be used to return results in the original order of the queries
        processed_queries = [[queries[i], i] for i in range(self.num_queries)]
        processed_queries = sorted(processed_queries, key=self.comparator)
        self.sorted_queries, self.inverse_map = list(zip(*processed_queries))

    def _compartor_processed(self, left: List, right: List) -> int:
        left_start_block = math.floor(left[QUERY][START] / self.len_sqrt)
        right_start_block = math.floor(right[QUERY][START] / self.len_sqrt)

        if left_start_block == right_start_block:
            if left[QUERY][END] > right[QUERY][END]:
                return 1
            elif left[QUERY][END] < right[QUERY][END]:
                return -1
            else:
                if left[QUERY][START] == right[QUERY][START]:
                    return 0
                elif left[QUERY][START] < right[QUERY][START]:
                    return -1
                else:
                    return 1

        elif left_start_block > right_start_block:
            return 1

        else:
            return -1

    def run_queries(self, operation: Type[MosOperation]) -> List:
        first_start = self.sorted_queries[0][START]
        op = operation(self.arr, first_start)

        results = [None for _ in range(self.num_queries)]

        for i, cur_query in enumerate(self.sorted_queries):
            op.move_end(cur_query[END])
            results[self.inverse_map[i]] = op.move_start(cur_query[START])

        return results
