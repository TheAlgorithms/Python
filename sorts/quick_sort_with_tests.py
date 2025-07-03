def quick_sort(arr: list[int]) -> list[int]:
    """
    Classic quick sort implementation using list comprehensions.

    Args:
        arr (list[int]): List of integers to sort.

    Returns:
        list[int]: New sorted list.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def quick_sort_3way(arr: list[int], low: int = 0, high: int | None = None) -> list[int]:
    """
    In-place 3-way partitioning quick sort.

    Args:
        arr (list[int]): List of integers to sort.
        low (int): Starting index of the sublist to sort.
        high (int | None): Ending index of the sublist to sort.

    Returns:
        list[int]: The same list sorted in-place.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        lt, gt = low, high
        pivot = arr[low]
        i = low + 1

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1

        quick_sort_3way(arr, low, lt - 1)
        quick_sort_3way(arr, gt + 1, high)

    return arr


def test_quick_sorts():
    """
    Simple test cases for quick_sort and quick_sort_3way functions.
    """
    test_cases = [
        ([3, 6, 8, 10, 1, 2, 1], [1, 1, 2, 3, 6, 8, 10]),
        ([4, 5, 4, 3, 4, 2, 1, 4], [1, 2, 3, 4, 4, 4, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
    ]

    for i, (input_arr, expected) in enumerate(test_cases):
        assert quick_sort(input_arr) == expected, f"quick_sort failed on test case {i + 1}"
        assert quick_sort_3way(input_arr.copy()) == expected, f"quick_sort_3way failed on test case {i + 1}"

    print("All tests passed!")


if __name__ == "__main__":
    test_quick_sorts()
