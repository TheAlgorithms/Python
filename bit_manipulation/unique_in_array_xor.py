def find_non_duplicate(nums: list) -> int:
    '''
    >>> find_non_duplicate([1, 2, 1, 2, 3, 4, 3])
    4
    This occurs as:
    1. Any number xor itself is 0.
    2. Any number xor 0 is itself.
    See more: https://en.wikipedia.org/wiki/XOR_gate#:~:text=XOR%20gate%20(sometimes%20EOR%2C%20or,to%20the%20gate%20is%20true.
    '''
    x = 0
    for num in nums:
        x ^= num
    return x
