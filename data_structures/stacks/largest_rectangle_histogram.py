"""
Author: Ansh Dulewale
GitHub: github.com/ansh-dulewale

Explanation:  http://www.codingdrills.com/tutorial/stack-data-structure/largest-rectangle-in-histogram

THESE ARE THE ALGORITHM'S RULES:
RULE 1: Scan `heights` array in left to right direction
        if the height at this index is greater than the height at the top position of `stack`
        we push the index at `stack`.

RULE 2: If the `height` at the current `index` is smaller than the `height` at the top of the `stack`
        process the stack now. Pop top `index` from `stack`.
        The `height` of the rectangle = `height` at popped `index`.
        Calculate `width` of the rectangle:
        if the `stack` is not empty.
        Then the `width` extends from `begin` of the `histogram` till current `index`.
        If the stack is not empty, the width stretches from a current index to an index that immediately comes after new stack top

RULE 3: area = height width if it is greater than max_area so far
                update max_area.

RULE 4: Repeat Rules 2 and 3 until the current height is no longer less than the height at the top index of the `stack`.
        Push the current index onto the `stack`.

RULE 5: After the entire `heights` array has been traversed, the maximum area found, stored in `max_area`,
        represents the area of the largest rectangle in the histogram.

NOTE:   It only works with whole numbers.
"""

__author__ = "Ansh Dulewale"


def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Add a zero height to pop all remaining heights in stack.

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    heights.pop()  # Restore the original heights array.
    return max_area


# Get input from the user
user_input = input()
heights = list(map(int, user_input.split()))

print(largestRectangleArea(heights))
