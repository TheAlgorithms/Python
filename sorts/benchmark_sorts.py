"""
Benchmark several sorting algorithms on the same random datasets.

This is a *reference* benchmark, not a rigorous one: it times each algorithm on a
few shared, randomly generated integer datasets and prints a small comparison
table.  It exists so that visitors can see the practical cost of the different
strategies in this directory side by side, without embedding timing code inside
the individual algorithm modules (which keeps those files clean, import-cheap and
focused on being readable reference implementations).

Run it from the repository root:

    python -m sorts.benchmark_sorts

The individual algorithms are imported from their own modules, so this file never
re-implements a sort.
"""

from __future__ import annotations

import random
import sys
from collections.abc import Callable, Sequence
from itertools import pairwise
from timeit import timeit

from sorts.bubble_sort import bubble_sort_iterative
from sorts.cocktail_shaker_sort import cocktail_shaker_sort
from sorts.comb_sort import comb_sort
from sorts.gnome_sort import gnome_sort
from sorts.heap_sort import heap_sort
from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort
from sorts.selection_sort import selection_sort
from sorts.shell_sort import shell_sort
from sorts.tim_sort import tim_sort

# name -> callable.  Every callable accepts a list and returns the sorted list.
SORTS: dict[str, Callable[[list[int]], Sequence[int]]] = {
    "bubble_sort": bubble_sort_iterative,
    "cocktail_shaker_sort": cocktail_shaker_sort,
    "comb_sort": comb_sort,
    "gnome_sort": gnome_sort,
    "heap_sort": heap_sort,
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort,
    "quick_sort": quick_sort,
    "selection_sort": selection_sort,
    "shell_sort": shell_sort,
    "tim_sort": tim_sort,
}


def is_sorted(collection: Sequence[int]) -> bool:
    """
    Return True if every element is less than or equal to the next one.

    >>> is_sorted([1, 2, 2, 3])
    True
    >>> is_sorted([1, 3, 2])
    False
    >>> is_sorted([])
    True
    """
    return all(a <= b for a, b in pairwise(collection))


def all_sorts_agree(data: list[int]) -> bool:
    """
    Return True if every algorithm in ``SORTS`` sorts ``data`` correctly.

    Each algorithm is given a fresh copy of the data (some sort in place), and its
    result is checked against Python's built-in ``sorted`` as the ground truth.

    >>> all_sorts_agree([5, 1, 4, 2, 8, 0, 2])
    True
    >>> all_sorts_agree([])
    True
    >>> all_sorts_agree([42])
    True
    """
    expected = sorted(data)
    return all(list(sort_fn(data.copy())) == expected for sort_fn in SORTS.values())


def benchmark(data: list[int], number: int = 1) -> dict[str, float]:
    """
    Time every algorithm in ``SORTS`` on a copy of ``data``.

    Returns a mapping of algorithm name to the elapsed seconds for ``number``
    repetitions.  Each timed call receives its own fresh copy so in-place sorts do
    not hand an already-sorted list to the next repetition.
    """
    timings: dict[str, float] = {}
    for name, sort_fn in SORTS.items():
        timings[name] = timeit(lambda fn=sort_fn: fn(data.copy()), number=number)
    return timings


def main() -> None:
    # A couple of the imported algorithms (e.g. tim_sort) merge recursively, so
    # give them head-room to sort the largest dataset without hitting the limit.
    sys.setrecursionlimit(10_000)
    sizes = (100, 1_000, 3_000)
    random.seed(0)
    datasets = {size: [random.randint(0, size) for _ in range(size)] for size in sizes}

    header = "algorithm".ljust(22) + "".join(f"{size:>12}" for size in sizes)
    print(header)
    print("-" * len(header))

    per_size = {size: benchmark(data) for size, data in datasets.items()}
    for name in SORTS:
        row = name.ljust(22)
        row += "".join(f"{per_size[size][name]:>12.4f}" for size in sizes)
        print(row)

    print("\nseconds per sort (lower is better); dataset = uniform random ints")


if __name__ == "__main__":
    main()
