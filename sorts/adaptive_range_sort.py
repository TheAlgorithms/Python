def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    count = [0] * (max_val - min_val + 1)
    for num in arr:
        count[num - min_val] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])
    return sorted_arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return quick_sort(left) + [pivot] + quick_sort(right)


def adaptive_range_sort(unsorted):
    """
    Adaptive Range Sort using Counting Sort and Quick Sort algorithms in Python.
    Sorts a list of integers by choosing an appropriate sorting algorithm based on the range of values.
    If the range is small, Counting Sort is used otherwise, Quick Sort is used.
    :param unsorted: A list of integers to be sorted.
    :return: A new sorted list containing the same integers in ascending order.

    Examples:
    >>> adaptive_range_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> adaptive_range_sort([])
    []

    >>> adaptive_range_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # Step 1: Identify the Range
    min_val, max_val = min(unsorted), max(unsorted)
    # Step 2: Choose Sorting Strategy
    if max_val - min_val <= 100:  # Threshold for choosing counting sort
        # Use Counting Sort for small range of values
        return counting_sort(unsorted)
    else:
        # Use Quick Sort for larger range of values
        return quick_sort(unsorted)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(adaptive_range_sort(unsorted))
