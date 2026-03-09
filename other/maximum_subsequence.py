from collections.abc import Sequence


def max_subsequence_sum(nums: Sequence[int] | None = None) -> int:
    """Return the maximum possible sum amongst all non - empty subsequences.

    Raises:
      ValueError: when nums is empty.

    >>> max_subsequence_sum([1,2,3,4,-2])
    10
    >>> max_subsequence_sum([-2, -3, -1, -4, -6])
    -1
    >>> max_subsequence_sum([])
    Traceback (most recent call last):
        . . .
    ValueError: Input sequence should not be empty
    >>> max_subsequence_sum()
    Traceback (most recent call last):
        . . .
    ValueError: Input sequence should not be empty
    """
    if nums is None or not nums:
        raise ValueError("Input sequence should not be empty")

    ans = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        ans = max(ans, ans + num, num)

    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Try on a sample input from the user
    n = int(input("Enter number of elements : ").strip())
    array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    print(max_subsequence_sum(array))
