def bubble_sort(nums: list[int]) -> list[int]:
    """
    param nums: the array of integers(int) because this application does not use decimal numbers, but if needed, use float type.
    :return: the same nums list ordered by ascending

    Examples:
    >>> bubble_sort([8, 2, 4, 5, 7, 0])
    [0, 2, 4, 5, 7, 8]

    step 01: create the nums array
    step 02: collect the dimension of array
    step 03: defines the number of times your array will be traversed according to the number of elements
    step 04: for each pair of elements in the array, starting from the Index, reorder them.
    Elements already in the correct order will not be modified in the Loop -> (0, n - 1 - i)
    step 05: the numbers are compared to arrive at the required order
    step 06: the nuns list is returned in ascending order! :)
    """
    n = len(nums)  # 02
    for i in range(n):  # 03
        for j in range(0, n - 1 - i):  # 04
            if nums[j] > nums[j + 1]:  # 05
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


nums = [65, 66, 12, 4, 9, 10, 32, 2]  # 01
ordered_nums = bubble_sort(nums)  # 06
print("The result:", ordered_nums)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
