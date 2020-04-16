"""Find mean of a list of numbers."""


def average(nums):
    """Find mean of a list of numbers."""
    return sum(nums) / len(nums)


def test_average():
    """
    >>> test_average()
    """
    assert 12.0 == average([3, 6, 9, 12, 15, 18, 21])
    assert 20 == average([5, 10, 15, 20, 25, 30, 35])
    assert 4.5 == average([1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == "__main__":
    """Call average module to find mean of a specific list of numbers."""
    print(average([2, 4, 6, 8, 20, 50, 70]))
