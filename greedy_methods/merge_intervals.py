"""
Given a collection of intervals, merge all overlapping intervals.

This is a classic greedy algorithm problem. The key insight is that after sorting
the intervals by their start time, we can merge overlapping intervals in a single
pass by comparing each interval's start with the previous interval's end.

Reference: https://en.wikipedia.org/wiki/Interval_scheduling#Interval_Partitioning

For doctests run the following command:
python -m doctest -v merge_intervals.py
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge all overlapping intervals and return the non-overlapping intervals
    that cover all the intervals in the input.

    Args:
        intervals: A list of intervals where each interval is [start, end].

    Returns:
        A list of merged non-overlapping intervals sorted by start time.

    Examples:
    >>> merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge_intervals([[1, 4], [4, 5]])
    [[1, 5]]
    >>> merge_intervals([[1, 4], [0, 4]])
    [[0, 4]]
    >>> merge_intervals([[1, 10], [2, 3], [4, 5], [6, 7]])
    [[1, 10]]
    >>> merge_intervals([[1, 2]])
    [[1, 2]]
    >>> merge_intervals([])
    []
    >>> merge_intervals([[3, 5], [1, 2], [6, 8], [2, 4]])
    [[1, 5], [6, 8]]
    >>> merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18], [17, 20]])
    [[1, 6], [8, 10], [15, 20]]
    >>> merge_intervals([[1, 1]])
    [[1, 1]]
    >>> merge_intervals("not a list")
    Traceback (most recent call last):
        ...
    TypeError: intervals must be a list of intervals
    >>> merge_intervals([[1, 2], "not an interval"])
    Traceback (most recent call last):
        ...
    TypeError: each interval must be a list of two integers
    >>> merge_intervals([[1, 2], [3]])
    Traceback (most recent call last):
        ...
    TypeError: each interval must be a list of two integers
    >>> merge_intervals([[2, 1]])
    Traceback (most recent call last):
        ...
    ValueError: interval start must not exceed end: [2, 1]
    """
    if not isinstance(intervals, list):
        raise TypeError("intervals must be a list of intervals")

    for interval in intervals:
        if not isinstance(interval, list) or len(interval) != 2:
            raise TypeError("each interval must be a list of two integers")
        if interval[0] > interval[1]:
            msg = f"interval start must not exceed end: {interval}"
            raise ValueError(msg)

    intervals.sort(key=lambda x: x[0])

    merged: list[list[int]] = []
    for interval in intervals:
        # If merged is empty or current interval does not overlap with previous
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is overlap, so merge the current and previous intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    example = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Intervals: {example}")
    print(f"Merged: {merge_intervals(example)}")
