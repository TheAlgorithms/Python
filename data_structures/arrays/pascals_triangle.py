"""
Generate Pascal's Triangle.

Reference: https://en.wikipedia.org/wiki/Pascal%27s_triangle

Python doctest can be run with the following command:
python -m doctest -v pascals_triangle.py

Given a non-negative integer num_rows, generate the first num_rows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""


class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        """
        Generate the first num_rows of Pascal's triangle.

        Args:
            num_rows (int): The number of rows to generate.

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
        ans: list[list[int]] = []
        for i in range(num_rows):
            # Initialize the row with 1s
            row = [1] * (i + 1)
            # Compute inner elements by summing elements from the previous row
            for j in range(1, i):
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            ans.append(row)
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
