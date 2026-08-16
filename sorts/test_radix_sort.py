import pytest

from sorts.radix_sort import radix_sort


def test_radix_sort_basic():
    assert radix_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]


def test_radix_sort_already_sorted():
    values = [1, 2, 3, 4, 5]
    assert radix_sort(values) == [1, 2, 3, 4, 5]


def test_radix_sort_reverse_sorted():
    values = [5, 4, 3, 2, 1]
    assert radix_sort(values) == [1, 2, 3, 4, 5]


def test_radix_sort_duplicates():
    values = [4, 2, 4, 1, 2, 4]
    assert radix_sort(values) == [1, 2, 2, 4, 4, 4]


def test_radix_sort_zero():
    assert radix_sort([0]) == [0]


def test_radix_sort_multiple_zeros():
    assert radix_sort([0, 5, 0, 2, 3]) == [0, 0, 2, 3, 5]


def test_radix_sort_different_digit_lengths():
    values = [1, 1000, 10, 100, 10000]
    assert radix_sort(values) == [1, 10, 100, 1000, 10000]


def test_radix_sort_large_numbers():
    values = [999999, 123456, 1000000, 42]
    assert radix_sort(values) == [42, 123456, 999999, 1000000]


def test_radix_sort_negative_number():
    with pytest.raises(ValueError):
        radix_sort([-1, 5, 3])


def test_radix_sort_multiple_negative_numbers():
    with pytest.raises(ValueError):
        radix_sort([-10, -5, 0, 5])


def test_radix_sort_matches_sorted():
    values = [170, 45, 75, 90, 802, 24, 2, 66]
    assert radix_sort(values) == sorted(values)