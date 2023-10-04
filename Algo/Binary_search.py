
python
1.

import math
k= [1,45,12,6,9,4,8,10,18,19,20]
k=sorted(k)
print(k)
no=len(k)
maxi=k.index(max(k))
mini=k.index(min(k))
mid=(no//2)
noOfSwaps=1
isFind=False
def binarySearch(n):
    global noOfSwaps,isFind, mini, mid, maxi
    while(not isFind):
        if(k[mid]==n):
            return
        if(k[mid]<n):
            mini=mid+1
            mid=math.floor((maxi+mini)/2)
            noOfSwaps+=1
            if(k[mini]==k[maxi]==n):
                isFind=True
            print(k[mini],k[mid],k[maxi],noOfSwaps)
            continue
        if(k[mid]>n):
            print('k')
            maxi=mid-1
            mid=math.floor((maxi+mini)/2)
            noOfSwaps+=1
            print(k[mini],k[mid],k[maxi],noOfSwaps)
            if(k[maxi]==k[mini]==n):
                isFind=True
            print(k[mini],k[mid],k[maxi],noOfSwaps)
            continue
binarySearch(20)


