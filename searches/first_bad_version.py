class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if isBadVersion(mid) == True:
                end = mid
            else:
                start = mid
        
        if isBadVersion(start):
            return start
        else:
            return end
