from typing import List


def shell_sort(arr: List[int]) -> None:
    """
    Perform Shell Sort on the given list 'arr' in place.

    :param arr: List of integers to be sorted.
    :return: None
    >>> arr = [12, 34, 54, 2, 3]
    >>> shell_sort(arr)
    >>> arr
    [2, 3, 12, 34, 54]
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i -= gap
            j += 1
        gap = gap // 2


if __name__ == "__main__":
    arr2 = [12, 34, 54, 2, 3]
    print("input array:", arr2)
    shell_sort(arr2)
    print("sorted array", arr2)
