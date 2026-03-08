from __future__ import annotations

from searches.binary_search import binary_search
from sorts.bubble_sort import bubble_sort_iterative


def test_binary_search_edge_cases() -> None:
    assert binary_search([], 10) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 10) == -1


def test_binary_search_large_array() -> None:
    data = list(range(200_000))
    assert binary_search(data, 199_999) == 199_999


def test_binary_search_with_duplicates_finds_valid_index() -> None:
    data = [1, 2, 2, 2, 3, 4]
    index = binary_search(data, 2)
    assert index in {1, 2, 3}


def test_bubble_sort_handles_basic_cases() -> None:
    assert bubble_sort_iterative([]) == []
    assert bubble_sort_iterative([1]) == [1]
    assert bubble_sort_iterative([3, 1, 2, 1]) == [1, 1, 2, 3]


def test_bubble_sort_large_reverse_input() -> None:
    data = list(range(2000, -1, -1))
    assert bubble_sort_iterative(data) == sorted(data)
