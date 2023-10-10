def maxProoductSubarray(nums, n):
	ans = nums[0]

	for i in range(n):
		mul = nums[i]
		for j in range(i + 1, n):
			ans = max(ans, mul)
			mul *= nums[j]

		# changing the result for index n-1th
		ans = max(ans, mul)

	return ans


nums = [1, -2, -3, 0, 7, -8, -2]
n = len(nums)
print("Maximum Sub array is ", maxProoductSubarray(nums, n))

