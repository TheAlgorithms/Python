from __future__ import print_function
# Time:  O(n)
# Space: O(n)
#
# Given n non-negative integers representing the histogram's bar
# height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        increasing, area, i = [], 0, 0
        while i <= len(height):
            if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if not increasing:
                    area = max(area, height[last] * i)
                else:
                    area = max(area, height[last] * (i - increasing[-1] - 1 ))
        return area

if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 0, 2]))
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
