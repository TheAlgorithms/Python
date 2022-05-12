def average_absolute_deviation(nums: list[int]) -> float:
    """
    Return the average absolute deviation of a list of numbers.
    Wiki: https://en.wikipedia.org/wiki/Average_absolute_deviation

    >>> average_absolute_deviation([0])
    0.0
    >>> average_absolute_deviation([4, 1, 3, 2])
    1.0
    >>> average_absolute_deviation([2, 70, 6, 50, 20, 8, 4, 0])
    20.0
    >>> average_absolute_deviation([-20, 0, 30, 15])
    16.25
    >>> average_absolute_deviation([])
    Traceback (most recent call last):
        ...
    ValueError: List is empty
    """
    if not nums:  # Makes sure that the list is not empty
        raise ValueError("List is empty")

    average = sum(nums) / len(nums)  # Calculate the average
    return sum(abs(x - average) for x in nums) / len(nums)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
