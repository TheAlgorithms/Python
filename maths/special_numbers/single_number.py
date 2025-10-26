def single_number(nums: list[int]) -> int:
    """
    Find the element that appears only once in a list where every other element appears twice.

    This algorithm uses bitwise XOR to cancel out duplicate numbers.

    >>> single_number([2, 2, 1])
    1
    >>> single_number([4, 1, 2, 1, 2])
    4
    >>> single_number([1])
    1
    """
    res = 0
    for n in nums:
        res ^= n
    return res


if __name__ == "__main__":
    example = [4, 1, 2, 1, 2]
    print(single_number(example))  # Output: 4
