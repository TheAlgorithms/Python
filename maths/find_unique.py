def find_unique_xor(nums: list) -> float:
    """
    Find unique from a given list of numbers with 2n+1 entries of which n element appears twice and there is one unique element.
    >>> find_unique_xor([1,2,3,2,1])
    3
    >>> find_unique_xor([25,27,26,27,25])
    26
    >>> find_unique_xor([1,2,1,2])
    -1
    """
    if len(nums) % 2 == 0:
        return -1
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
