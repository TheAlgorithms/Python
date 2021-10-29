class Solution:
    def arraySortedOrNot(self, arr, n):
        ans=1
        for i in range(1,n):
            if arr[i]>=arr[i-1]:
                continue
            else:
                ans=0
                break
        if ans==1:
            return ans
        for i in range(1,n):
            if arr[i]<=arr[i-1]:
                continue
            else:
                ans=0
                break
        return ans
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ob=Solution()
    ans=ob.arraySortedOrNot(a,n)
    print(ans)  #1 for true and 0 for false