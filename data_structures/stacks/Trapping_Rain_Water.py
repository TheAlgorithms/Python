"""
	Every element represents the height of the block. The width of the block can be considered 1.
	Find the volume of trapped rainwater between these block.
"""

height = [34, 2, 5, 2, 3, 23, 18, 23, 45]
answer = 162


def max_water(height):

    """
    Get the maximum unit of water trapped between the blocks

    >>> max_water(height) == answer
    True

    """

    stack = []
    n = len(height)
    answer = 0

    for i in range(n):

        while len(stack) != 0 and (height[stack[-1]] < height[i]):

            pop_height = height[stack[-1]]
            stack.pop()

            if len(stack) == 0:
                break

            distance = i - stack[-1] - 1

            min_height = min(height[stack[-1]], height[i]) - pop_height

            answer += distance * min_height

        stack.append(i)

    return answer


if __name__ == "__main__":

    from doctest import testmod

    testmod()

    print("For the block structure of heights : ", height)
    print("Maximum Volume of Water Trappped : " + str(max_water(height)))
