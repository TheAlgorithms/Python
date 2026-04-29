def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge all overlapping intervals.

    Each interval is represented as a list of two integers [start, end].
    The function merges overlapping intervals and returns a list of
    non-overlapping intervals sorted by start time.

    Parameters:
    intervals (list[list[int]]): A list of intervals.

    Returns:
    list[list[int]]: A list of merged non-overlapping intervals.

    Edge Cases Handled:
    - Empty list: returns []
    - Single interval: returns the interval itself
    - Intervals already sorted or unsorted
    - Fully overlapping intervals
    - Invalid intervals (e.g., [[]] or intervals not having exactly
      2 integers) raise ValueError

    Examples:
    >>> merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge_intervals([[1, 4], [4, 5]])
    [[1, 5]]
    >>> merge_intervals([[6, 8], [1, 3], [2, 4]])
    [[1, 4], [6, 8]]
    >>> merge_intervals([])
    []
    >>> merge_intervals([[1, 4]])
    [[1, 4]]

    Time Complexity:
    O(n log n) - sorting the intervals, where n is the number of intervals.

    Space Complexity:
    O(n) - storing the merged intervals.
    """

    if not intervals:
        return []

    for interval in intervals:
        msg = f"Each interval must have exactly 2 integers, got {interval}"
        if len(interval) != 2:
            raise ValueError(msg)

    # Sort intervals based on the start time
    intervals.sort(key=lambda interval: interval[0])

    merged: list[list[int]] = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # If current interval overlaps with the last merged interval
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
