
def Next_smaller_element(arr, n):
	s = []
	mp = {}

	s.append(arr[0])

	for i in range(1, n):
		if (len(s) == 0):
			s.append(arr[i])
			continue

		while (len(s) != 0 and s[-1] > arr[i]):
			mp[s[-1]] = arr[i]
			s.pop()


		s.append(arr[i])

	while (len(s) != 0):
		mp[s[-1]] = -1
		s.pop()
    


	for i in range(n):
		print("Next smaller element of " + str(arr[i]) + " is " + str(mp[arr[i]]))


arr = [int(item) for item in input("Enter the array elements : ").split()]
n = len(arr)
Next_smaller_element(arr, n)

