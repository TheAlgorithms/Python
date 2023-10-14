import ast


def find_missing_number(nums: list[int]) -> int:
    """
    Finds the missing number in a list of consecutive integers.

    Args:
        nums: A list of integers.

    Returns:
        The missing number.

    Example:
        >>> find_missing_number([0, 1, 3, 4])
        2
    """

    n = len(nums)
    # missing_number = n

    # Debug
    # Finding the starting number entered
    start = min(nums)
    missing_number = start + n

    for i in range(n):
        # missing_number ^= i ^ nums[i]
        # Debug
        missing_number ^= (start + i) ^ nums[i]

    return missing_number


# Calling the function
num = ast.literal_eval(input("Enter a list:"))
print(find_missing_number(num))
