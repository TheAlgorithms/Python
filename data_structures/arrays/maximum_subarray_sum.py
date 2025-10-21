def maximum_subarray_sum(arr):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm

    Args:
        arr (list of int): The input array

    Returns:
        int: The maximum subarray sum
    """

    if not arr:
        return 0

    current_max_sum = max_sum = arr[0]

    for i in arr[1:]:
        current_max_sum = max(i, current_max_sum + i)
        max_sum = max(max_sum, current_max_sum)

    return max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("maximum subarray sum is: ", maximum_subarray_sum(arr))
