from collections import deque


def sliding_window_maximum(numbers: list[int], window_size: int) -> list[int]:
    """
    Return a list containing the maximum of each sliding window of size window_size.

    This implementation uses a monotonic deque to achieve O(n) time complexity.

    Args:
        numbers: List of integers representing the input array.
        window_size: Size of the sliding window (must be positive).

    Returns:
        List of maximum values for each valid window.

    Raises:
        ValueError: If window_size is not a positive integer.

    Time Complexity: O(n) - each element is added and removed at most once
    Space Complexity: O(k) - deque stores at most window_size indices

    Examples:
    >>> sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
    [3, 3, 5, 5, 6, 7]
    >>> sliding_window_maximum([9, 11], 2)
    [11]
    >>> sliding_window_maximum([], 3)
    []
    >>> sliding_window_maximum([4, 2, 12, 3], 1)
    [4, 2, 12, 3]
    >>> sliding_window_maximum([1], 1)
    [1]
    """
    if window_size <= 0:
        raise ValueError("Window size must be a positive integer")
    if not numbers:
        return []

    result: list[int] = []
    index_deque: deque[int] = deque()

    for current_index, current_value in enumerate(numbers):
        # Remove the element which is out of this window
        if index_deque and index_deque[0] == current_index - window_size:
            index_deque.popleft()

        # Remove useless elements (smaller than current) from back
        while index_deque and numbers[index_deque[-1]] < current_value:
            index_deque.pop()

        index_deque.append(current_index)

        # Start adding to result once we have a full window
        if current_index >= window_size - 1:
            result.append(numbers[index_deque[0]])

    return result
