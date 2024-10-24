
"""
  Intuition
The problem involves finding the largest rectangle that can be formed in a histogram of different heights. The approach is to iteratively process the histogram's bars while keeping track of the maximum area found so far.

Approach
Initialize a variable maxArea to store the maximum area found, and a stack to keep track of the indices and heights of the histogram bars.

Iterate through the histogram using an enumeration to access both the index and height of each bar.

For each bar, calculate the width of the potential rectangle by subtracting the starting index (retrieved from the stack) from the current index.

While the stack is not empty and the height of the current bar is less than the height of the bar at the top of the stack, pop elements from the stack to calculate the area of rectangles that can be formed.

Update maxArea with the maximum of its current value and the area calculated in step 4.

Push the current bar's index and height onto the stack to continue processing.

After processing all bars, there may still be bars left in the stack. For each remaining bar in the stack, calculate the area using the height of the bar and the difference between the current index and the index at the top of the stack.

Return maxArea as the result, which represents the largest rectangle area.

Complexity
Time complexity: O(n), where n is the number of bars in the histogram. We process each bar once.
Space complexity: O(n), as the stack can contain up to n elements in the worst case when the bars are in increasing order (monotonic).



Step-by-Step Diagram Creation
Draw the Histogram:

Use vertical bars to represent the heights of the histogram.
Highlight the Largest Rectangle:

Shade or color the area of the largest rectangle.
Example Diagram
plaintext
Copy code
   6 |         #
     |         #
   5 |         # #
     |         # #
   4 |         # #
     |         # #
   3 |   #     # #
     |   #     # #
   2 |   # # # # # #
     |   # # # # # #
   1 | # # # # # # # #
     |_____________________
     0  1  2  3  4  5
Highlight the Largest Rectangle
Now, let's highlight the largest rectangle:

The largest rectangle has a height of 6 and spans from index 0 to 3.
plaintext
Copy code
   6 |         #
     |         #
   5 |         # #
     |         # #
   4 |         # #
     |         # #
   3 | ██████████
     | ██████████
   2 | ██████████
     | ██████████
   1 | # # # # # # # #
     |_____________________
     0  1  2  3  4  5
Final Summary
The shaded area represents the largest rectangle in the histogram.
Area: 24 (Height = 6, Width = 4)
Indices Covered: 0 to 3



"""

def largestRectangleArea(self, heights: List[int]) -> int:
    # Initialize the maximum area to 0
    max_area = 0
    
    # Create a stack to store pairs of (index, height)
    stack = []  
    
    # Iterate over each bar in the histogram with its index
    for i, h in enumerate(heights):
        # Set the starting index for the rectangle to the current index
        start = i  

        # While the stack is not empty and the height of the bar at the top of the stack is greater than the current height
        while stack and stack[-1][-1] > h:
            # Pop the top element from the stack to get the index and height of that bar
            index, ph = stack.pop()
            
            # Calculate the area with the height of the popped bar and the width from the current index to the popped index
            max_area = max(max_area, ph * (i - index))
            
            # Update the starting index to the index of the popped bar
            start = index  

        # Push the current height and the starting index onto the stack
        stack.append([start, h])

    # After processing all bars, calculate areas for remaining bars in the stack
    for i, h in stack:
        # Calculate area with the height of the remaining bars and width from their index to the end of the heights list
        max_area = max(max_area, h * (len(heights) - i))
    
    # Return the maximum area found
    return max_area

heights = [2,4]

largest_Rectangle_Area=largestRectangleArea(heights)

print(largest_Rectangle_Area)  ## answer will be 4 for current input