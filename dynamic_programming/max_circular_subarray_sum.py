import doctest


def max_circular_subarray_sum(arr: list[int], size: int) -> int:
    """
    Input: arr[] = {8, -7, 9, -9, 10, -11, 12}
    Output: 23
    Explanation: Subarray 12, 8, -7, 9, -9, 10 gives the maximum sum, which is 23.

    >>> max_circular_subarray_sum([8, -7, 9, -9, 10, -11, 12], 7)
    23
    >>> max_circular_subarray_sum([8, -7, 10, -9, 10, -11, 12], 7)
    24
    >>> max_circular_subarray_sum([8, -7, 10, -9, 10, -11, 12], 1)
    12
    >>> max_circular_subarray_sum([8, -7, 10, -9, 10, -11, 12], 0)
    0
    >>> max_circular_subarray_sum([], 0)
    0
    >>> max_circular_subarray_sum([-5], -1)
    Traceback (most recent call last):
    ...
    ValueError: Subarray size can't be negative
    >>> max_circular_subarray_sum([-5], 2)
    Traceback (most recent call last):
    ...
    ValueError: Subarray size can't exceed array size
    """
    if size < 0:
        raise ValueError("Subarray size can't be negative")
    if size > len(arr):
        raise ValueError("Subarray size can't exceed array size")
    if len(arr) == 0 or size == 0:
        return 0

    arr_sum = sum(arr)
    current_max = max_so_far = current_min = min_so_far = arr[0]

    for i in range(1, size):
        # Kadane's algorithm to find maximum subarray arr_sum
        current_max = max(current_max + arr[i], arr[i])
        max_so_far = max(max_so_far, current_max)

        # Kadane's algorithm to find minimum subarray arr_sum
        current_min = min(current_min + arr[i], arr[i])
        min_so_far = min(min_so_far, current_min)

    if min_so_far == arr_sum:
        return max_so_far

    # returning the maximum value
    return max(max_so_far, arr_sum - min_so_far)


if __name__ == "__main__":
    doctest.testmod()

    size = int(input("Enter size of array:\t"))
    arr = [int(x) for x in input("Enter the elements of the array: ").strip().split()]
    print(f"Maximum circular sum is {max_circular_subarray_sum(arr, size)}")
