# Given an array of N non-negative integers arr[] representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
# Input: arr[] = {2, 0, 2}
# Output: 2
# Input: arr[]   = {3, 0, 2, 0, 4}
# Output: 7

# Function to return the maximum
# water that can be stored
def maxWater(height):
    # Stores the indices of the bars
    stack = []

    # size of the array
    n = len(height)

    # Stores the final result
    ans = 0

    # Loop through the each bar
    for i in range(n):

        # Remove bars from the stack
        # until the condition holds
        while len(stack) != 0 and (height[stack[-1]] < height[i]):

            # store the height of the top
            # and pop it.
            pop_height = height[stack[-1]]
            stack.pop()

            # If the stack does not have any
            # bars or the popped bar
            # has no left boundary
            if len(stack) == 0:
                break

            # Get the distance between the
            # left and right boundary of
            # popped bar
            distance = i - stack[-1] - 1

            # Calculate the min. height
            min_height = min(height[stack[-1]], height[i]) - pop_height

            ans += distance * min_height

        # If the stack is either empty or
        # height of the current bar is less than
        # or equal to the top bar of stack
        stack.append(i)
    return ans


arr = [3, 0, 2, 0, 4]
print(maxWater(arr))
