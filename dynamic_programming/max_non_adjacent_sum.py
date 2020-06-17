from typing import List

def max_non_adj_sum(nums: List[int]) -> int:
    '''
    Function to find the maximum non-adjacent sum of the elements in the input list

    Parameters
    ----------
    nums : List[int]
        List of integers for the maximum non-adjacent sum computation

    Returns
    -------
    int
        maximum non-adjacent sum

    Examples
    --------
    These are written in doctest format, and should illustrate how to use the function

    >>> print(max_non_adj_sum([1, 2, 3]))
    4

    >>> max_non_adj_sum([1, 5, 3, 7, 2, 2, 6])
    18

    >>> max_non_adj_sum([-1, -5, -3, -7, -2, -2, -6])
    0

    >>> max_non_adj_sum([499, 500, -3, -7, -2, -2, -6])
    500
    '''

    if (len(nums) == 0):
        return 0

    max_including = nums[0]
    max_excluding = 0

    for num in nums[1:]:
        temp = max_including
        max_including = max_excluding + num
        max_excluding = max(temp, max_excluding)
    
    return max(max_excluding, max_including)

if __name__ == "__main__":
    import doctest

    doctest.testmod()