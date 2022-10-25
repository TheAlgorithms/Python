import doctest


# The function returns maximum circular contiguous sum in a[]
def max_circular_sum(arr: list[int], size: int) -> int:
    """
    Input: arr[] = {8, -7, 9, -9, 10, -11, 12}
    Output: 23
    Explanation: Subarray 12, 8, -7, 9, -9, 10 gives the maximum sum, that is 23.

    >>> max_circular_sum([8, -7, 9, -9, 10, -11, 12], 7)
    23

    >>> max_circular_sum([8, -7, 10, -9, 10, -11, 12], 7)
    24

    >>> max_circular_sum([-5], 1)
    -5
    """

    # Edge Case
    if size == 1:
        return arr[0]

    # Sum variable which store total arr_sum of the array.
    arr_sum = sum(arr)

    # Every variable stores first value of the array.
    current_max = max_so_far = current_min = min_so_far = arr[0]

    # Concept of Kadane's Algorithm
    for i in range(1, size):
        # Kadane's Algorithm to find Maximum subarray arr_sum.
        current_max = max(current_max + arr[i], arr[i])
        max_so_far = max(max_so_far, current_max)

        # Kadane's Algorithm to find Minimum subarray arr_sum.
        current_min = min(current_min + arr[i], arr[i])
        min_so_far = min(min_so_far, current_min)

    if min_so_far == arr_sum:
        return max_so_far

    # returning the maximum value
    return max(max_so_far, arr_sum - min_so_far)


if __name__ == "__main__":
    doctest.testmod()
    size = int(input("Enter size of array:\t"))
    arr = list(map(int, input("Enter the elements of the array: ").strip().split()))
    print(f"Maximum circular sum is {max_circular_sum(arr, size)}")
