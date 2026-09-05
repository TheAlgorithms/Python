def largest_rectangle_area(heights: list[int]) -> int:
    """
    Inputs an array of integers representing the heights of bars,
    and returns the area of the largest rectangle that can be formed

    >>> largest_rectangle_area([2, 1, 5, 6, 2, 3])
    10

    >>> largest_rectangle_area([2, 4])
    4

    >>> largest_rectangle_area([6, 2, 5, 4, 5, 1, 6])
    12

    >>> largest_rectangle_area([1])
    1
    """
    stack: list[int] = []
    max_area = 0
    heights = [*heights, 0]  # make a new list by appending the sentinel 0
    n = len(heights)

    for i in range(n):
        # make sure the stack remains in increasing order
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]  # height of the bar
            # if stack is empty, it means entire width can be taken from index 0 to i-1
            w = i if not stack else i - stack[-1] - 1  # calculate width
            max_area = max(max_area, h * w)

        stack.append(i)

    return max_area


if __name__ == "__main__":
    import doctest

    doctest.testmod()
