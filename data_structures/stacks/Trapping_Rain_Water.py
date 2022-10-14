
def maxWater(height):

	stack = []
	n = len(height)
	ans = 0

	for i in range(n):

		while(len(stack) != 0 and (height[stack[-1]] < height[i])):

			pop_height = height[stack[-1]]
			stack.pop()

			if(len(stack) == 0):
				break

			distance = i - stack[-1] - 1

			min_height = min(height[stack[-1]], height[i])-pop_height

			ans += distance * min_height

		stack.append(i)

	return ans


if __name__ == '__main__':
	arr = [int(item) for item in input("Enter the Height of buildings : ").split()]
	print("Maximum Water Trappped : " + str(maxWater(arr)))

