def duplicate_array(arr: list[int]) -> int:
    """
    Find the duplicate item in an integer Array
    consisting [1, n] items and one repeated item
    Args:
        arr :array of integers

    Examples:
        >>> duplicate_array([4,2,3,1, 5,6,4])
        4
        >>> duplicate_array([1,2,2])
        2
        >>> duplicate_array([5,4,3,2,1,3])
        3
    """

    slow_ptr = arr[0]
    fast_ptr = arr[arr[0]]
    while slow_ptr != fast_ptr:
        fast_ptr = arr[arr[fast_ptr]]
        slow_ptr = arr[slow_ptr]

    slow_ptr = 0
    while fast_ptr != slow_ptr:
        fast_ptr = arr[fast_ptr]
        slow_ptr = arr[slow_ptr]
    return slow_ptr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
