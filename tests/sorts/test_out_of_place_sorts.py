"""This module tests deterministic out-of-place sorting algorithms in a generic
fashion by having them sort a few different kinds of lists.

An out-of-place sorting algorithm is expected to return a sorted copy of the
input. In general, it should not mutate the input. The tests in this module
expects this generic behavior. The built-in ``sorted`` function is an example
of an out-of-place sorting algorithm:

    >>> lst = [5, 2, 1]
    >>> sorted_lst = sorted(lst)
    >>> print(lst)
    [5, 2, 1] # not mutated
    >>> print(sorted_lst)
    [1, 2, 5]

If you implement an out-of-place sorting algorithm, you can run all the tests
in this test suite on it by simply adding the function to the SORTS list. Note
that you must import the module in which the sorting algorithm is located as
well.

Please only add deterministic algorithms here. Random algorithms (e.g.
bogosort) shouldn't be run on lists this large, as they may never terminate.
"""
import pytest

import sorts.bucket_sort
import sorts.counting_sort
import sorts.merge_sort_fastest
import sorts.pancake_sort
import sorts.timsort
import sorts.tree_sort
import sorts.quick_sort

SORTS = [
    sorts.bucket_sort.bucketSort,
    sorts.counting_sort.counting_sort,
    sorts.merge_sort_fastest.merge_sort,
    sorts.pancake_sort.pancakesort,
    sorts.timsort.timsort,
    sorts.tree_sort.treesort,
    sorts.quick_sort.quick_sort,
]

# Constants applying to most lists in the tests
# note that abs(MIN) + abs(MAX) < NUM_ELEMENTS, which
# guarantees duplicates in test cases.
NUM_ELEMENTS = 500
MIN = -int(NUM_ELEMENTS / 3)
MAX = -int(NUM_ELEMENTS / 3)


@pytest.mark.parametrize("sort", SORTS)
class TestOutOfPlaceSort:
    """Test class for out-of-place sorting algorithms. Note that the class is just
    for grouping.
    
    Note that the built-in ``sorted`` returns a copy, and does not mutate the
    input. It's very important to assert against a _copy_ of the list the
    algorithm sorts, so as not to assert that a list is equal to itself.

    Note that all test cases, except that for the empty list, have lists
    containing at least some duplicates.
    """

    @staticmethod
    def test_does_not_mutate_input(sort, randlist):
        """Test that the out-of-place sorting algorithm does not mutate the
        input.
        """
        lst = randlist(num_elems=NUM_ELEMENTS, min_=MIN, max_=MAX)
        expected = list(lst)  # expect lst to be unchanged

        sort(lst)

        assert lst == expected

    @staticmethod
    def test_sort_random_list(sort, randlist):
        """Test sorting a list with random elements in random order."""
        lst = randlist(num_elems=NUM_ELEMENTS, min_=MIN, max_=MAX)
        expected = sorted(lst)

        actual = sort(lst)

        assert actual == expected

    @staticmethod
    def test_sort_sorted_list(sort, randlist):
        """Test sorting a list of random elements which is already sorted in
        ascending order.
        """
        lst = sorted(randlist(num_elems=NUM_ELEMENTS, min_=MIN, max_=MAX))
        expected = list(lst)

        actual = sort(lst)

        assert actual == expected

    @staticmethod
    def test_sort_reversed_list(sort, randlist):
        """Test sorting a list of random elements which is sorted in descending
        order (reversed).
        """
        lst = list(reversed(randlist(num_elems=NUM_ELEMENTS, min_=MIN, max_=MAX)))
        expected = sorted(lst)

        actual = sort(lst)

        assert actual == expected

    @staticmethod
    def test_sort_equal_list(sort):
        """Test sorting a list containing duplicates of a single element."""
        elem = 37
        lst = [37 for _ in range(NUM_ELEMENTS)]
        expected = list(lst)

        actual = sort(lst)

        assert actual == expected

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

        actual = sort(lst)

        assert actual == expected

    @staticmethod
    def test_sort_empty_list(sort):
        """Test sorting an empty list."""
        empty_list = []
        actual = sort(empty_list)
        assert actual == empty_list
