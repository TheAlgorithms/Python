'''
This is Booyer-Moore Majority Vote Algorithm. The problem statement goes like Given an integer array of size n, find all elements that appear more than ⌊ n/k ⌋ times.
We have to solve in O(n) time and O(1) Space. 
 
'''
import collections

def majorityElement(nums, k):
  ctr = collections.Counter()
  for n in nums:
      ctr[n] += 1
      if len(ctr) == k:
          ctr -= collections.Counter(set(ctr))
  ctr = collections.Counter(n for n in nums if n in ctr)
  return [n for n in ctr if ctr[n] > len(nums)/k]


nums = [1,2,2,3,1,3,2]
k = 3
print(majorityElement(nums,k))

'''
Output: [2]
'''
