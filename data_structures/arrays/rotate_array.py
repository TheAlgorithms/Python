def rotate_array(arr: list[int], steps: int) -> list[int]:
    """
    Rotates the array to the right by a given number of steps

    Args:
        arr (list[int]): The input array.
        k (int): Number of steps to rotate.

    Returns:
        list[int]: Rotated array.

    Examples:
        >>> rotate_array([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
        >>> rotate_array([1, 2, 3], 0)
        [1, 2, 3]
        >>> rotate_array([], 3)
        []
    """
    n = len(arr)
    k = steps % n if n else 0

    arr.reverse()  # Reverse the entire array
    arr[:k] = reversed(arr[:k])  # Reverse the first k elements
    arr[k:] = reversed(arr[k:])  # Reverse the last (n-k) elements

    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    steps = 3
    print("Rotated array: ", rotate_array(arr, steps))
