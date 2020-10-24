"""
Minimum number of jumps to reach end using DYNAMIC PROGRAMMING approach
Time Complexity: O(n)
Space Complexity: O(1)
For Example:
            Input:  arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
            Output: 3 (1-> 3 -> 8 -> 9)
"""


def min_jump_to_reach_end(arr: list) -> int:
    """
    >>> min_jump_to_reach_end([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])
    3
    """

    n = len(arr)

    # The number of jumps needed to reach the starting index is 0
    if n <= 1:
        return 0

    # Return -1 if not possible to jump
    if arr[0] == 0:
        return -1

    # initialization
    # stores all time the maximal reachable index in the array
    maxReach = arr[0]
    # stores the amount of steps we can still take
    step = arr[0]
    # stores the jumps required to reach maximal reachable position
    jump = 1

    # Start traversing array

    for i in range(1, n):
        # Check if we have reached the end of the array
        if i == n - 1:
            return jump

        # updating maxReach
        maxReach = max(maxReach, i + arr[i])

        # we use a step to get to the current index
        step -= 1

        # If no further steps left
        if step == 0:
            # we must have used a jump
            jump += 1

            # Check if the current index / position or lesser index
            # is the maximum reach point from the previous indexes
            if i >= maxReach:
                return -1

            # re-initialize the steps to the amount
            # of steps to reach maxReach from position i.
            step = maxReach - i
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    assert min_jump_to_reach_end([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]) == 3
    assert min_jump_to_reach_end([0, 1, 10, 15, 2, 2]) == -1
    assert min_jump_to_reach_end([]) == 0
