def largest_Rectangle_Area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Add a zero height to pop all remaining heights in stack.

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    heights.pop()  # Restore the original heights of array.
    return max_area

# Get input from the user
user_input = input()
heights = list(map(int, user_input.split()))

print(largestRectangleArea(heights))
