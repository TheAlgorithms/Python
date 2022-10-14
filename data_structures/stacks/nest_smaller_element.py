
def next_smaller_element(arr, n):
	stack = []
	map = {}

	stack.append(arr[0])

	for i in range(1, n):
		if (len(stack) == 0):
			stack.append(arr[i])
			continue

		while (len(stack) != 0 and stack[-1] > arr[i]):
			map[stack[-1]] = arr[i]
			stack.pop()


		stack.append(arr[i])

	while (len(stack) != 0):
		map[stack[-1]] = -1
		stack.pop()
    


	for i in range(n):
		print("Next smaller element of " + str(arr[i]) + " is " + str(mp[arr[i]]))


arr = [int(item) for item in input("Enter the array elements : ").split()]
n = len(arr)
next_smaller_element(arr, n)

