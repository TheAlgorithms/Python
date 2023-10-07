"""
Given an array of non-negative integers representing an elevation map where
the width of each bar is 1,this program calculates how much rainwater can be trapped.

Example - height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
This problem can be solved using the concept of "DYNAMIC PROGRAMMING".

We calculate the maximum height of bars on the left and right of every bar in array.
Then iterate over the width of structure and at each index.
The amount of water that will be stored is equal to minimum of maximum height of bars
on both sides minus height of bar at current position.
"""


def trapped_rainwater(height : list[int]) -> int:
    """
    The trapped_rainwater function calculates the total amount of rainwater
    that can be trapped given an array of bar heights.
    It uses a dynamic programming approach, determining the maximum height of bars
    on both sides for each bar, and then computing the trapped water above each bar.
    The function returns the total trapped water.

    trapped_rainwater([0,1,0,2,1,0,1,3,2,1,2,1])
    >>> 6
    trapped_rainwater([7,1,5,3,6,4])
    >>> 9    
    """
    if height is None:
        height = []
        return 0
    length = len(height)

    left_max = [0] * length
    left_max[0] = height[0]
    for i in range(1, length):
        left_max[i] = max(height[i], left_max[i - 1])

    right_max = [0] * length
    right_max[length - 1] = height[length - 1]
    for i in range(length - 2, -1, -1):
        right_max[i] = max(height[i], right_max[i + 1])

    trapped_water: int = 0

    for i in range(length):
        water_level = min(left_max[i], right_max[i])
        trapped_water += water_level - height[i]

    return trapped_water


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{trapped_rainwater([0,1,0,2,1,0,1,3,2,1,2,1])}")
