def rotate_array(arr: list[int], steps: int) -> list[int]:
    """
    Rotates a list to the right by steps positions.

    Parameters:
    arr (List[int]): The list of integers to rotate.
    steps (int): Number of positions to rotate. Can be negative for left rotation.

    Returns:
    List[int]: Rotated list.

    Examples:
    >>> rotate_array([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    >>> rotate_array([1, 2, 3, 4, 5], -2)
    [3, 4, 5, 1, 2]
    >>> rotate_array([1, 2, 3, 4, 5], 7)
    [4, 5, 1, 2, 3]
    >>> rotate_array([], 3)
    []
    """

    n = len(arr)
    if n == 0:
        return arr

    steps = steps % n

    if steps < 0:
        steps += n

    def reverse(start: int, end: int) -> None:
        """
        Reverses a portion of the list in place from index start to end.

        Parameters:
        start (int): Starting index of the portion to reverse.
        end (int): Ending index of the portion to reverse.

        Returns:
        None

        Examples:
        >>> example = [1, 2, 3, 4, 5]
        >>> def reverse_test(arr, start, end):
        ...     while start < end:
        ...         arr[start], arr[end] = arr[end], arr[start]
        ...         start += 1
        ...         end -= 1
        >>> reverse_test(example, 0, 2)
        >>> example
        [3, 2, 1, 4, 5]
        >>> reverse_test(example, 2, 4)
        >>> example
        [3, 2, 5, 4, 1]
        """

        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, steps - 1)
    reverse(steps, n - 1)

    return arr


if __name__ == "__main__":
    examples = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], -2),
        ([1, 2, 3, 4, 5], 7),
        ([], 3),
    ]

    for arr, steps in examples:
        rotated = rotate_array(arr.copy(), steps)
        print(f"Rotate {arr} by {steps}: {rotated}")
