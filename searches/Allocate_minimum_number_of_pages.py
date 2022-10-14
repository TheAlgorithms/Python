# One of the most important question of searching algorithm

class Solution:
    def ispossible(self,A,M,mid):
        stu=1
        page=0
        for k in A:
            if page+k<=mid:
                page+=k
            else:
                stu+=1
                if stu>M or k>mid:
                   return False
                else:
                    page=k
        return True
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        if len(A)<M:
            return -1
        s=0
        su=0
        for i in A:
            su+=i
        e=su
        ans=-1
        while s<=e:
            mid=s+(e-s)//2
            if self.ispossible(A,M,mid):
                ans=mid
                e=mid-1
            else:
                s=mid+1
        return ans
