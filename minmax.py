# Min-Max probelem solved using Divide and Conquer
def find_min_max(arr, left, right):
    """
    Finds the minimum and maximum elements in an array using divide and conquer method.

    Args:
        arr (list): The input array.
        left (int): The left index of the subarray.
        right (int): The right index of the subarray.

    Returns:
        tuple: A tuple containing the minimum and maximum elements.

    Examples:
        >>> arr = [3, 1, 9, 5, 7, 2, 8, 4]
        >>> find_min_max(arr, 0, len(arr) - 1)
        (1, 9)

        >>> arr = [3, 3, 3, 3, 3]
        >>> find_min_max(arr, 0, len(arr) - 1)
        (3, 3)

        >>> arr = [99]
        >>> find_min_max(arr, 0, 0)
        (99, 99)

        >>> arr = []
        >>> find_min_max(arr, 0, -1)
        (None, None)
    """
    # Base case: If the array has no elements, return None for both minimum and maximum.
    if left > right:
        return None, None

    # Base case: If the array has only one element, it is both the minimum and maximum.
    if left == right:
        return arr[left], arr[left]

    # For an array with two elements, compare and return the minimum and maximum.
    if right - left == 1:
        return min(arr[left], arr[right]), max(arr[left], arr[right])

    # Divide the array into two halves and recursively find min and max in each half.
    mid = (left + right) // 2
    min1, max1 = find_min_max(arr, left, mid)
    min2, max2 = find_min_max(arr, mid + 1, right)

    # Combine the results from the two halves to find the overall minimum and maximum.
    return min(min1, min2), max(max1, max2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
