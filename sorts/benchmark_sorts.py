#!/usr/bin/env -S uv run --script

"""
Benchmark several sorting algorithms on the same random datasets.

This is a *reference* benchmark, not a rigorous one: it times each algorithm on a
few shared, randomly generated integer datasets and prints a small comparison
table.  It exists so that visitors can see the practical cost of the different
strategies in this directory side by side, without embedding timing code inside
the individual algorithm modules (which keeps those files clean, import-cheap,
and focused on being readable reference implementations).

Run it from the repository root:

    python -m sorts.benchmark_sorts

The individual algorithms are imported from their own modules, so this file never
re-implements a sort.
"""


import random
import sys
from collections.abc import Sequence
from itertools import pairwise
from timeit import timeit
from typing import Protocol

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


class SortFunction(Protocol):
    def __call__[T](self, collection: list[T], /) -> Sequence[T]:
        ...


# Store sorting algorithms in a dictionary
SORTS: dict[str, SortFunction] = {
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
    """Check whether the collection is sorted."""
    return all(a <= b for a, b in pairwise(collection))


def all_sorts_agree(data: list[int]) -> bool:
    """Check whether all sorting algorithms produce correct results."""
    expected = sorted(data)

    for sort_fn in SORTS.values():
        result = list(sort_fn(data.copy()))

        if result != expected:
            return False

    return True


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool:
        ...


def benchmark[T: Comparable](
    data: list[T], number: int = 1
) -> dict[str, float]:

    if not data:
        raise ValueError("Please provide a non-empty dataset")

    if number <= 0:
        raise ValueError("Number of repetitions must be positive")

    timings = {}

    for name, sort_fn in SORTS.items():
        elapsed = timeit(
            lambda fn=sort_fn: fn(data.copy()),
            number=number
        )

        timings[name] = elapsed

    return timings


def main() -> None:
    sys.setrecursionlimit(10000)

    sizes = (100, 1000, 3000)

    random.seed(0)

    datasets = {
        size: [random.randint(0, size) for _ in range(size)]
        for size in sizes
    }

    header = "Algorithm".ljust(22)

    for size in sizes:
        header += f"{size:>12}"

    print(header)
    print("-" * len(header))

    results = {
        size: benchmark(data)
        for size, data in datasets.items()
    }

    for name in SORTS:
        row = name.ljust(22)

        for size in sizes:
            row += f"{results[size][name]:>12.4f}"

        print(row)

    print("\nExecution time in seconds (lower is better)")
    print("Dataset: Random integers")


if __name__ == "__main__":
    main()

