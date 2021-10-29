class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        # arr = list(map(int,input().split()))
        # arr = list(map(int,input().split()))
        # arr = list(map(int,input().split()))
        start,end = -1,-1
        flag = 0
        arr2 = sorted(arr)
        k=0
        for i,j in zip(arr,arr2):
            if i!=j and flag==0:
                start = k
                flag=1
            if i!=j and flag==1:
                end = k
            k+=1
        if flag==1 and end!=-1:
            # print(end-start+1)
            return end-start+1
        else:
            return 0