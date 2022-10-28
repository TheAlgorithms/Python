from collections.abc import Sequence


def max_subarray_sum(nums: Sequence[int]) -> int:
    """Return the maximum possible sum amongst all non - empty subarrays.

    Raises:
      ValueError: when nums is empty.

    >>> max_subarray_sum([1,2,3,4,-2])
    10
    >>> max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])
    6
    """
    if not nums:
        raise ValueError("Input sequence should not be empty")

    curr_max = ans = nums[0]
    nums_len = len(nums)

    for i in range(1, nums_len):
        num = nums[i]
        curr_max = max(curr_max + num, num)
        ans = max(curr_max, ans)

    return ans


if __name__ == "__main__":
    n = int(input("Enter number of elements : ").strip())
    array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    print(max_subarray_sum(array))
