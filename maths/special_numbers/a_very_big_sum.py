def a_very_big_sum(arr: list[int]) -> int:
    """
    Return the sum of all integers in the input array.

    >>> a_very_big_sum([2, 4, 6])
    12
    >>> a_very_big_sum([])
    0
    """
    total = 0
    for i in arr:
        total += i
    return total


if __name__ == "__main__":
    # Example usage
    arr = [2, 4, 6, 2, 4, 6, 3]
    result = a_very_big_sum(arr)
    print(f"Sum of {arr} is {result}")
