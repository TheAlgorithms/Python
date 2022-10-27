from collections.abc import Iterable


def max_subarray_sum(nums: Iterable[int]) -> int:
    """
    Raises:
      ValueError: when nums is empty.

    Returns the maximum possible sum amongst all non - empty subarrays
    >>> max_subarray_sum([1,2,3,4,-2])
    10
    >>> max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])
    6
    """
    if not nums:
        raise ValueError('Input iterable should not be empty')

    curr_max = ans = nums[0]

    for num in nums[1:]:
        curr_max = max(curr_max + num, num)
        ans = max(curr_max, ans)

    return ans


if __name__ == "__main__":
    n = int(input("Enter number of elements : ").strip())
    array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    print(max_subarray_sum(array))
