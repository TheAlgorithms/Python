"""
Given an array of non-negative integers representing an elevation map where the width
of each bar is 1, this program calculates how much rainwater can be trapped.

Example - height = (0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1)
Output: 6
This problem can be solved using the concept of "DYNAMIC PROGRAMMING".

We calculate the maximum height of bars on the left and right of every bar in array.
Then iterate over the width of structure and at each index.
The amount of water that will be stored is equal to minimum of maximum height of bars
on both sides minus height of bar at current position.
"""


def trapped_rainwater(heights: tuple[int, ...]) -> int:
    """
    The trapped_rainwater function calculates the total amount of rainwater that can be
    trapped given an array of bar heights.
    It uses a dynamic programming approach, determining the maximum height of bars on
    both sides for each bar, and then computing the trapped water above each bar.
    The function returns the total trapped water.

    >>> trapped_rainwater((0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1))
    6
    >>> trapped_rainwater((7, 1, 5, 3, 6, 4))
    9
    >>> trapped_rainwater((7, 1, 5, 3, 6, -1))
    Traceback (most recent call last):
        ...
    ValueError: No height can be negative
    """
    if not heights:
        return 0
    if any(h < 0 for h in heights):
        raise ValueError("No height can be negative")
    left, right = 0, len(heights) - 1
    leftmax, rightmax = 0, 0
    water = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= leftmax:
                leftmax = heights[left]
            else:
                water += leftmax - heights[left]
            left += 1
        else:
            if heights[right] >= rightmax:
                rightmax = heights[right]
            else:
                water += rightmax - heights[right]
            right -= 1
    return water


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{trapped_rainwater((0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1)) = }")
    print(f"{trapped_rainwater((7, 1, 5, 3, 6, 4)) = }")
