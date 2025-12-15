def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge all overlapping intervals.

    Each interval is represented as a list of two integers [start, end].
    The function merges overlapping intervals and returns a list of
    non-overlapping intervals sorted by start time.

    Parameters:
    intervals (List[List[int]]): A list of intervals.

    Returns:
    List[List[int]]: A list of merged non-overlapping intervals.

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
    O(n log n), where n is the number of intervals (sorting step).

    Space Complexity:
    O(n), for storing the merged intervals.
    """

    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda interval: interval[0])

    merged: List[List[int]] = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # If current interval overlaps with the last merged interval
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
