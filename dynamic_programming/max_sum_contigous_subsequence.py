def maxSubArraySum(nums):
  if not nums: return 0
  n = len(nums)
  s = [0] * n
  res, s, s_pre = nums[0], nums[0], nums[0]
  for i in xrange(1, n):
      s = max(nums[i], s_pre + nums[i])
      s_pre = s
      res = max(res, s)
  return res

def main():
    nums = [6 , 9, -1, 3, -7, -5, 10]
    print(maxSubArraySum(nums))

if __name__ == '__main__':
    main()