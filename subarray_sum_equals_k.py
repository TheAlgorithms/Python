from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_sums = 0
        dic = defaultdict(int)
        dic[0] =1
        cnt =0
        for i in nums:
            num_sums += i
            cnt+=dic[num_sums-k]
            dic[num_sums]+=1
        return(cnt)
