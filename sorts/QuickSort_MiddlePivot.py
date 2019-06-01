# Author : Junth Basnet

"""
Implementation of Quick Sort Algorithm with middle element as pivot element
Time Complexity : O(nlogn) - O(n^2)
"""

def QuickSortFirst(array):
    return QuickSort(array, 0, len(array) - 1)

def QuickSort(array, left, right):
	if left >= right:
		return array
	pivot = array[(left + right) // 2]
	index = Partition(array, left, right, pivot)
	QuickSort(array, left, index - 1)
	QuickSort(array, index, right)
	return array

def Partition(array, left, right, pivot):
	while left <= right:
		while array[left] < pivot:
			left += 1
		while array[right] > pivot:
			right -= 1
		if left <= right:
			array[left], array[right] = array[right], array[left]
			left += 1
			right -= 1
	return left

array = [1, 6, 4, 10, 7, 30, 25]
print(array)
sorted_array = QuickSortFirst(array)
print(sorted_array)