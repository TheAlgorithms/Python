class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)
        freq = defaultdict(int)
        mn = float('inf')
        for i in range(n):
            freq[basket1[i]] += 1
            freq[basket2[i]] -= 1
            mn = min(mn, basket1[i], basket2[i])
        
        to_swap = []
        for j,k in freq.items():
            if k % 2 != 0:
                return -1
            to_swap += [j] * (abs(k) // 2)
        
        to_swap.sort()
        res = 0
        for i in range(len(to_swap) // 2):
            res += min(to_swap[i], 2 * mn)
        
        return res
