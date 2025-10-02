def max_subarray_sum(arr: list[int]) -> int:
    """
    Find the maximum sum of a subarray.

    Args:
        arr: array of numbers.

    Returns:
        Maximum sum possible in a subarray
    """
    ans = arr[0]

    for i in range(len(arr)):
        current_sum = 0

        for j in range(i, len(arr)):
            current_sum = current_sum + arr[j]
            ans = max(ans, current_sum)

    return ans


if __name__ == "__main__":
    arr = list(map(int, input().split(" ")))
    print(max_subarray_sum(arr))
    import doctest

    doctest.testmod()
