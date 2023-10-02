# Python program for implementation of Dutch National Flag algorithm

# Function to partition the array according to the pivot
# element and returns the index of the pivot element
def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] < pivot:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return (i + 1)

# Function to sort the input array using Dutch National Flag Algorithm
def dutch_national_flag_sort(arr, low, high):
	if (low < high):
		pivot = partition(arr, low, high)
		dutch_national_flag_sort(arr, low, pivot - 1)
		dutch_national_flag_sort(arr, pivot + 1, high)

# Driver code
arr = list(map(int,input().split()))
dutch_national_flag_sort(arr, 0, len(arr) - 1)
print("The sorted array is:")
print(*arr)
