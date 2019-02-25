"""This module tests deterministic in-place sorting algorithms in a generic
fashion by having them sort a few different kinds of lists.

An in-place sorting algorithm is expected to sort the input list in-place (i.e.
mutate the input). For example, the built-in `list.sort` method is in-place:

    >>> lst = [5, 2, 1]
    lst.sort()
    >>> print(lst)
    [1, 2, 4]

If you implement an in-place sorting algorithm, you can run all the tests
in this test suite on it by simply adding the function to the SORTS list.
Note that you must import the module in which the sorting algorithm is located
as well.

Please only add deterministic algorithms here. Random algorithms (e.g.
bogosort) shouldn't be run on lists this large, as they may never terminate.
"""
from functools import partial

import pytest

# add an absoulute import here to the module
import sorts.insertion_sort
import sorts.bubble_sort
import sorts.cocktail_shaker_sort
import sorts.comb_sort
import sorts.cyclesort
import sorts.gnome_sort
import sorts.heap_sort
import sorts.merge_sort
import sorts.quick_sort_3_partition
import sorts.radix_sort
import sorts.selection_sort
import sorts.shell_sort

# add an absolute reference to the function to be tested here
SORTS = [
    sorts.bubble_sort.bubble_sort,
    sorts.cocktail_shaker_sort.cocktail_shaker_sort,
    sorts.comb_sort.comb_sort,
    sorts.cyclesort.cycle_sort,
    sorts.gnome_sort.gnome_sort,
    sorts.heap_sort.heap_sort,
    sorts.insertion_sort.insertion_sort,
    sorts.merge_sort.merge_sort,
    sorts.quick_sort_3_partition.quick_sort,
    sorts.radix_sort.radixsort,
    sorts.selection_sort.selection_sort,
    sorts.shell_sort.shell_sort,
]

# Constants applying to most lists in the tests
# note that abs(MIN) + abs(MAX) < NUM_ELEMENTS, which
# guarantees duplicates in test cases.
NUM_ELEMENTS = 500
MIN = -int(NUM_ELEMENTS / 3)
MAX = int(NUM_ELEMENTS / 3)


@pytest.mark.parametrize("sort", SORTS)
class TestInPlaceSort:
    """Test class for in-place sorting algorithms. Note that the class is just
    for grouping.

    Note that the built-in ``sorted`` returns a copy, and does not mutate the
    input. It's very important to assert against a _copy_ of the list the
    algorithm sorts, so as not to assert that a list is equal to itself.

    Note that all test cases, except that for the empty list, have lists
    containing at least some duplicates.
    """

    @staticmethod
    def test_sort_random_list(sort, randlist):
        """Test sorting a list with random elements in random order."""
        lst = randlist(num_elems=NUM_ELEMENTS, min_=MIN, max_=MAX)
        expected = list(lst)

        sort(lst)

        assert lst == sorted(expected)

    @staticmethod
    def test_sort_sorted_list(sort, randlist):
        """Test sorting a list of random elements which is already sorted in
        ascending order.
        """
        lst = sorted(randlist(num_elems=NUM_ELEMENTS, min_=MIN, max_=MAX))
        expected = list(lst)

        sort(lst)

        assert lst == expected

    @staticmethod
    def test_sort_reversed_list(sort, randlist):
        """Test sorting a list of random elements which is sorted in descending
        order (reversed).
        """
        lst = list(reversed(randlist(num_elems=NUM_ELEMENTS, min_=MIN, max_=MAX)))
        expected = sorted(lst)

        sort(lst)

        assert lst == expected

    @staticmethod
    def test_sort_equal_list(sort):
        """Test sorting a list containing duplicates of a single element."""
        elem = 37
        lst = [elem for _ in range(NUM_ELEMENTS)]
        expected = list(lst)

        sort(lst)

        assert lst == expected

    @staticmethod
    def test_sort_negative_numbers(sort, randlist):
        """Test sorting a list containing only negative numbers.

        NOTE: LEGACY TEST
        At the time of writing this, I don't see why this test would be
        important, but it was frequent in the original doctests that this test
        suite replaces, so we keep it. It can very likely be removed with
        negligible impact on test performance.
        """
        lst = randlist(num_elems=NUM_ELEMENTS, min_=MIN, max_=0)
        expected = sorted(lst)

        sort(lst)

        assert lst == expected

    @staticmethod
    def test_sort_empty_list(sort):
        """Test sorting an empty list."""
        empty_list = []
        sort(empty_list)
        assert empty_list == []
