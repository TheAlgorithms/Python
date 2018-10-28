# NguyenU

import math
def find_max(nums):
    max = 0
    for x in nums:
      if x > max:
        max = x
    print(max)
L=list(map(int,input().split()))
find_max(L)
