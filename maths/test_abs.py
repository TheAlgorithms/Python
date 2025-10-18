# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///

import pytest

from maths.abs import abs_val, abs_min, abs_max, abs_max_sort


class TestAbsVal:
    """Test cases for abs_val function."""

    def test_positive_numbers(self):
        """Test abs_val with positive numbers."""
        assert abs_val(5) == 5
        assert abs_val(10.5) == 10.5
        assert abs_val(0.1) == 0.1

    def test_negative_numbers(self):
        """Test abs_val with negative numbers."""
        assert abs_val(-5) == 5
        assert abs_val(-10.5) == 10.5
        assert abs_val(-0.1) == 0.1

    def test_zero(self):
        """Test abs_val with zero."""
        assert abs_val(0) == 0
        assert abs_val(0.0) == 0.0

    def test_large_numbers(self):
        """Test abs_val with large numbers."""
        assert abs_val(-100000000000) == 100000000000
        assert abs_val(100000000000) == 100000000000


class TestAbsMin:
    """Test cases for abs_min function."""

    def test_positive_numbers(self):
        """Test abs_min with positive numbers."""
        assert abs_min([1, 2, 3, 4, 5]) == 1
        assert abs_min([5, 1, 3, 4, 2]) == 1

    def test_negative_numbers(self):
        """Test abs_min with negative numbers."""
        assert abs_min([-5, -1, -3, -4, -2]) == -1
        assert abs_min([-10, -2, -8]) == -2

    def test_mixed_numbers(self):
        """Test abs_min with mixed positive and negative numbers."""
        assert abs_min([3, -10, -2]) == -2
        assert abs_min([0, 5, 1, 11]) == 0
        assert abs_min([-3, -1, 2, -11]) == -1

    def test_single_element(self):
        """Test abs_min with single element list."""
        assert abs_min([5]) == 5
        assert abs_min([-5]) == -5

    def test_empty_list(self):
        """Test abs_min with empty list."""
        with pytest.raises(ValueError, match="abs_min\\(\\) arg is an empty sequence"):
            abs_min([])


class TestAbsMax:
    """Test cases for abs_max function."""

    def test_positive_numbers(self):
        """Test abs_max with positive numbers."""
        assert abs_max([1, 2, 3, 4, 5]) == 5
        assert abs_max([0, 5, 1, 11]) == 11

    def test_negative_numbers(self):
        """Test abs_max with negative numbers."""
        assert abs_max([-5, -1, -3, -4, -2]) == -5
        assert abs_max([-10, -2, -8]) == -10

    def test_mixed_numbers(self):
        """Test abs_max with mixed positive and negative numbers."""
        assert abs_max([3, -10, -2]) == -10
        assert abs_max([-3, -1, 2, -11]) == -11

    def test_single_element(self):
        """Test abs_max with single element list."""
        assert abs_max([5]) == 5
        assert abs_max([-5]) == -5

    def test_empty_list(self):
        """Test abs_max with empty list."""
        with pytest.raises(ValueError, match="abs_max\\(\\) arg is an empty sequence"):
            abs_max([])


class TestAbsMaxSort:
    """Test cases for abs_max_sort function."""

    def test_positive_numbers(self):
        """Test abs_max_sort with positive numbers."""
        assert abs_max_sort([1, 2, 3, 4, 5]) == 5
        assert abs_max_sort([0, 5, 1, 11]) == 11

    def test_negative_numbers(self):
        """Test abs_max_sort with negative numbers."""
        assert abs_max_sort([-5, -1, -3, -4, -2]) == -5
        assert abs_max_sort([-10, -2, -8]) == -10

    def test_mixed_numbers(self):
        """Test abs_max_sort with mixed positive and negative numbers."""
        assert abs_max_sort([3, -10, -2]) == -10
        assert abs_max_sort([-3, -1, 2, -11]) == -11

    def test_single_element(self):
        """Test abs_max_sort with single element list."""
        assert abs_max_sort([5]) == 5
        assert abs_max_sort([-5]) == -5

    def test_empty_list(self):
        """Test abs_max_sort with empty list."""
        with pytest.raises(
            ValueError, match="abs_max_sort\\(\\) arg is an empty sequence"
        ):
            abs_max_sort([])

    def test_consistency_with_abs_max(self):
        """Test that abs_max_sort gives same results as abs_max."""
        test_cases = [
            [1, 2, 3, 4, 5],
            [-5, -1, -3, -4, -2],
            [3, -10, -2],
            [0, 5, 1, 11],
            [-3, -1, 2, -11],
            [42],
            [-42],
        ]

        for test_case in test_cases:
            assert abs_max_sort(test_case) == abs_max(test_case)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
