def max_subarray(nums: list[int]) -> int:
    """
    Returns the subarray with maximum sum
    >>> max_subarray([1,2,3,4,-2])
    10
    >>> max_subarray([-2,1,-3,4,-1,2,1,-5,4])
    6
    """

    curr_max = ans = nums[0]

    for i in range(1, len(nums)):
        if curr_max >= 0:
            curr_max = curr_max + nums[i]
        else:
            curr_max = nums[i]

        ans = max(curr_max, ans)

    return ans


if __name__ == "__main__":
    n = int(input("Enter number of elements : ").strip())
    array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    print(max_subarray(array))
