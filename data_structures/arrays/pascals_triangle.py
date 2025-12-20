""" Generate Pascal's Triangle.

Python doctest can be run with the following command: python -m doctest -v pascals_triangle.py

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example Input: numRows = 5 Output: [ [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1] ] """

class Solution(object): def generate(self, numRows): """ Generate the first numRows of Pascal's triangle.

    Args:
        numRows (int): The number of rows to generate.

    Returns:
        list[list[int]]: Pascal's triangle as a list of lists.

    Examples:
        >>> solution = Solution()
        >>> solution.generate(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        >>> solution.generate(1)
        [[1]]
        >>> solution.generate(0)
        []
    """
    ans = []
    for i in range(numRows):
        # Initialize the row with 1s
        row = [1] * (i + 1)
        
        # Compute inner elements by summing elements from the previous row
        for j in range(1, i):
            row[j] = ans[i-1][j-1] + ans[i-1][j]
            
        ans.append(row)
    return ans
if name == "main": 
  import doctest

doctest.testmod()
