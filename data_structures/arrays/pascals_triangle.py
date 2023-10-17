from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        ans = [[1], [1, 1]]

        for i in range(2, numRows):
            current_row = [1]
            for j in range(1, i):
                current_row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            current_row.append(1)
            ans.append(current_row)

        return ans


# Example usage
s = Solution()
print(s.generate(5))
