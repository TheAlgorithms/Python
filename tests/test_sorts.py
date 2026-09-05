"""
Tests for the general-purpose comparison sorts in ``sorts/``.

Every algorithm exercised here implements the same contract: given a list of
mutually comparable items it returns a new list with the same items in
non-decreasing order (i.e. it agrees with the built-in ``sorted``).  Rather than
repeat a hand-written test per file we run each sort against a shared battery of
inputs with :func:`pytest.mark.parametrize`.

Specialised sorts that only accept a restricted domain are intentionally left
out (e.g. ``counting_sort``/``radix_sort``/``pigeon_sort`` are integer-only,
``bead_sort`` needs non-negative integers, ``dutch_national_flag_sort`` expects
0/1/2, ``bitonic_sort`` needs a power-of-two length, ``topological_sort`` works
on a graph, and ``stalin_sort``/``wiggle_sort`` deliberately do not fully sort).
"""

import pytest

from sorts.binary_insertion_sort import binary_insertion_sort
from sorts.bubble_sort import bubble_sort_iterative
from sorts.circle_sort import circle_sort
from sorts.cocktail_shaker_sort import cocktail_shaker_sort
from sorts.comb_sort import comb_sort
from sorts.cycle_sort import cycle_sort
from sorts.double_sort import double_sort
from sorts.exchange_sort import exchange_sort
from sorts.gnome_sort import gnome_sort
from sorts.heap_sort import heap_sort
from sorts.insertion_sort import insertion_sort
from sorts.iterative_merge_sort import iter_merge_sort
from sorts.merge_sort import merge_sort
from sorts.odd_even_sort import odd_even_sort
from sorts.patience_sort import patience_sort
from sorts.quick_sort import quick_sort
from sorts.selection_sort import selection_sort
from sorts.shell_sort import shell_sort
from sorts.stooge_sort import stooge_sort
from sorts.strand_sort import strand_sort


def test_heap_sort():
    assert heap_sort([]) == []
    assert heap_sort([1]) == [1]
    assert heap_sort([5, 2, 5, 1]) == [1, 2, 5, 5]
    assert heap_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


SORTS = (
    binary_insertion_sort,
    bubble_sort_iterative,
    circle_sort,
    cocktail_shaker_sort,
    comb_sort,
    cycle_sort,
    double_sort,
    exchange_sort,
    gnome_sort,
    heap_sort,
    insertion_sort,
    iter_merge_sort,
    merge_sort,
    odd_even_sort,
    patience_sort,
    quick_sort,
    selection_sort,
    shell_sort,
    stooge_sort,
    strand_sort,
)

CASES = (
    [],
    [1],
    [10, -10, -1, 1, 0],
    [1.1, -1.1, -1, 1, 0],
    list("Python!"),
    [3, 3, 1, 2, 2, 1],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [-2, -2, 0, 0, 7, 7],
)


@pytest.mark.parametrize("sort", SORTS, ids=lambda f: f.__name__)
@pytest.mark.parametrize("case", CASES, ids=repr)
def test_sort_matches_builtin(sort, case):
    """Each sort must reproduce the ordering of the built-in ``sorted``."""
    assert list(sort(list(case))) == sorted(case)
