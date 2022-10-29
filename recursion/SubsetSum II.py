class Solution:
    def subsetSums(self, arr, N):

        res = []

        def helper(idx, total):

            # base case
            if idx >= N:
                res.append(total)
                return

            helper(idx + 1, total + arr[idx])
            helper(idx + 1, total)

            return res

        return helper(0, 0)
