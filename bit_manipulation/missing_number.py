def find_missing_number(nums: list[int]) -> int:
    """
    Finds the missing number in a list of consecutive integers.
    Uses XOR to find the missing number efficiently. XOR has the property that:
    - a ^ a = 0 (any number XORed with itself is 0)
    - a ^ 0 = a (any number XORed with 0 is itself)
    - XOR is commutative and associative
    Therefore, XORing all numbers with all indices will cancel out the existing
    numbers, leaving only the missing number.
    Algorithm:
    1. Initialize result with the maximum value from the list
    2. For each position i and corresponding value nums[i]:
       a. XOR result with the position index i
       b. XOR result with the value nums[i]
    3. The result will be the missing number (all others cancel out)
    Why it works:
    If list is [0,1,3,4], we need to find 2
    - Low = 0, High = 4
    - XOR all values and indices: result = 4 ^ 0 ^ 1 ^ 3 ^ 4 ^ 0 ^ 1 ^ 3
    - When simplified: all numbers except 2 appear twice, so they cancel
    - Result: 2
    >>> find_missing_number([0, 1, 3, 4])
    2
    >>> find_missing_number([4, 3, 1, 0])
    2
    >>> find_missing_number([-4, -3, -1, 0])
    -2
    >>> find_missing_number([-2, 2, 1, 3, 0])
    -1
    >>> find_missing_number([1, 3, 4, 5, 6])
    2
    >>> find_missing_number([6, 5, 4, 2, 1])
    3
    >>> find_missing_number([6, 1, 5, 3, 4])
    2
    """
    low = min(nums)
    high = max(nums)
    missing_number = high

    for i in range(low, high):
        missing_number ^= i ^ nums[i - low]

    return missing_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
