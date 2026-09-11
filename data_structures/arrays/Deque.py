# Find maximum of every window of size k
from collections import deque

arr = [1,3,-1,-3,5,3,6,7]
k = 3
dq = deque()
res = []

for i, val in enumerate(arr):
    while dq and dq[0] <= i-k:
        dq.popleft()  # remove out-of-window indices
    while dq and arr[dq[-1]] < val:
        dq.pop()  # remove smaller elements
    dq.append(i)
    if i >= k-1:
        res.append(arr[dq[0]])

print(res)  # [3, 3, 5, 5, 6, 7]
