# A special type of Data Structure for Range Minimum Query
# Suppose an array is initialised and there are q queries of with lower and upper index.
# The goal is to find the minimum element within that range.
# Finding min can take O(n) time, therefore for q queries total time = O(q * n)
# To reduce this time complexity we use Segment Tree.
# Where finding min within a range takes O(logn) time.
# Hence the total time complexity reduces to O(q * logn).

import math, sys
# st stands for segment tree

def constructSegmentTree(ip, st, left, right, pos):
    if left != right:
        mid = int((left + right) / 2)
        constructSegmentTree(ip, st, left, mid, 2*pos+1)
        constructSegmentTree(ip, st, mid+1, right, 2*pos+2)
        st[pos] = min(st[2*pos+1], st[2*pos+2])
    else:
        st[pos] = ip[left]

def rangeMinQuery(ip, st, left, right, pos, qleft, qright):
    # for total overlap
    if left >= qleft and right <= qright:
        return st[pos]
    # for no overlap
    elif qleft > right or qright < left:
        return sys.maxsize
    # for partial overlap
    else:
        mid = int((left + right) / 2)
        x = rangeMinQuery(ip, st, left, mid, 2*pos+1, qleft, qright)
        y = rangeMinQuery(ip, st, mid+1, right, 2*pos+2, qleft, qright)
        return min(x, y)

ip = [int(x) for x in input().split()]
if math.floor(math.log2(len(ip))) == math.ceil(math.log2(len(ip))):
    n = (len(ip))*2 - 1
else:
    n = (2**math.ceil(math.log2(len(ip))))*2 - 1
st = [0] * n

constructSegmentTree(ip, st, 0, (len(ip)-1), 0)
print(st)
p = rangeMinQuery(ip, st, 0, (len(ip)-1), 0, 1, 4)
print(p)

    
    
         
